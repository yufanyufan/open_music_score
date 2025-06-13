with ScorePartwise(version='3.1'):
    with Identification():
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
            PageHeight(1683.78)
            PageWidth(1190.55)
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
        CreditWords('The Well-Tempered Clavier Book I - VIII', default_x=595.275, default_y=1627.09, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('BWV 853    (A = 415 Hz)', default_x=595.275, default_y=1570.39, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J. S. Bach', default_x=1133.86, default_y=1527.09, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('ハープシーコード', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('ハープシーコード')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(7)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=365.79):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(180.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(-6)
                with Time():
                    Beats('3')
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
                    Words('Praeludium', relative_x=-99.0, relative_y=56.5, font_size='14')
                Staff(1)
            with Note(default_x=147.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=258.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=286.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=331.42, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=147.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=198.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=285.82, default_y=-30.0):
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
                Duration(144.0)
            with Note(default_x=147.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=198.04, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=285.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
        with Measure(number='2', width=233.28):
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=124.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=153.56, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=198.9, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=12.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=63.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=63.49, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=153.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=12.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=63.49, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=153.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=153.2, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
        with Measure(number='3', width=455.59):
            with Note(default_x=15.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=160.95, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=198.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=216.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=233.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=250.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=268.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=285.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=302.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=319.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=336.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=354.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=371.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=398.89, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=426.44, default_y=-20.0):
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
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=15.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=74.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=198.47, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=3.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=15.95, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=74.49, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=74.49, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=198.47, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
        with Measure(number='4', width=565.25):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(132.11)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=127.74, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=145.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=162.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=179.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=196.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=213.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=231.09, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=248.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=265.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=282.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=299.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=316.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=334.09, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=357.4, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=380.41, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=485.32, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Backup():
                Duration(144.0)
            with Note(default_x=127.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(default_x=485.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.45)
            with Note(default_x=485.32, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.45)
            with Note(default_x=485.32, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.45)
            with Backup():
                Duration(144.0)
            with Note():
                Rest()
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=453.62, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=485.68, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=531.59, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=275.64):
            with Note(default_x=16.87, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=124.66, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=155.03, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=172.55, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=199.71, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=241.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=16.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-4.55)
            with Note(default_x=16.87, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-4.55)
            with Note(default_x=16.87, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-4.55)
            with Note(default_x=62.45, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45, relative_x=-13.83, relative_y=7.55)
            with Note(default_x=62.45, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45, relative_x=-13.83, relative_y=7.55)
            with Note(default_x=171.83, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45, relative_x=-13.83, relative_y=7.55)
            with Note(default_x=171.83, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45, relative_x=-13.83, relative_y=7.55)
            with Backup():
                Duration(144.0)
            with Note(default_x=16.87, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=62.45, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=-14.55)
            with Note(default_x=62.45, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=-14.55)
            with Note(default_x=171.83, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=-14.55)
            with Note(default_x=171.83, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=-14.55)
        with Measure(number='6', width=213.78):
            with Note(default_x=25.09, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=0.45)
            with Note(default_x=68.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=0.45)
            with Note(default_x=140.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=0.45)
            with Backup():
                Duration(144.0)
            with Note(default_x=25.09, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55)
            with Note(default_x=25.09, default_y=-30.0):
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
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55)
            with Note(default_x=25.09, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55)
            with Note(default_x=68.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55)
            with Note(default_x=68.79, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55)
            with Note(default_x=140.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55)
            with Note(default_x=140.29, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55)
            with Backup():
                Duration(144.0)
            with Note(default_x=25.09, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.45)
            with Note(default_x=25.09, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.45)
            with Note(default_x=25.09, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.45)
            with Note(default_x=25.09, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.45)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=120.79, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=140.65, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=179.4, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='7', width=494.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(132.11)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=140.47, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=20.45, relative_x=-13.83, relative_y=14.55)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=313.32, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=339.46, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=365.96, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=393.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=459.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=140.47, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.45)
            with Note(default_x=140.47, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.45)
            with Note(default_x=213.65, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.81, default_y=0.45, relative_x=-20.79, relative_y=-5.45)
            with Note(default_x=213.65, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.81, default_y=0.45, relative_x=-20.79, relative_y=-5.45)
            with Note(default_x=365.24, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=0.45, relative_x=-13.83, relative_y=-0.95)
            with Note(default_x=365.24, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=0.45, relative_x=-13.83, relative_y=-0.95)
            with Backup():
                Duration(144.0)
            with Note(default_x=140.47, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=213.65, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=-24.55, relative_x=-19.83, relative_y=-25.95)
            with Note(default_x=213.65, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=-24.55, relative_x=-19.83, relative_y=-25.95)
            with Note(default_x=365.24, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=-24.55)
            with Note(default_x=365.24, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=-24.55)
        with Measure(number='8', width=560.47):
            with Note(default_x=25.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=44.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=63.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=83.11, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=102.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=121.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=140.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=160.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=179.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=198.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=217.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=236.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=256.11, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=317.26, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.45)
            with Note(default_x=317.26, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.45)
            with Note(default_x=317.26, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.45)
            with Note(default_x=455.66, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.45)
            with Note(default_x=455.66, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.45)
            with Note(default_x=455.66, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.45)
            with Backup():
                Duration(144.0)
            with Note(default_x=25.09, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.45)
            with Note(default_x=25.09, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.45)
            with Note(default_x=25.09, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.45)
            with Note(default_x=25.09, default_y=-105.0):
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
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.45)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=413.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=456.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=516.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
        with Measure(number='9', width=1054.66):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(132.11)
                with StaffLayout(number=2):
                    StaffDistance(70.08)
            with Note(default_x=140.47, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=25.45)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=462.79, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=516.45, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=570.11, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=623.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=677.44, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=731.1, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=784.76, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=838.42, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=892.08, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=945.74, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=999.4, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=140.47, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.45)
            with Note(default_x=140.47, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.45)
            with Note(default_x=290.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55)
            with Note(default_x=290.72, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55)
            with Note(default_x=623.41, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55)
            with Note(default_x=623.41, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55)
            with Backup():
                Duration(144.0)
            with Note(default_x=140.47, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=290.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-39.55, relative_x=-13.06, relative_y=-45.45)
            with Note(default_x=623.41, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-39.55, relative_x=-11.56, relative_y=-48.45)
        with Measure(number='10', width=670.58):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(132.11)
                with StaffLayout(number=2):
                    StaffDistance(70.17)
            with Note(default_x=140.83, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=161.79, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=182.76, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=203.72, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=224.69, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=245.65, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=266.62, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=287.59, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=308.55, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=329.52, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=350.48, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=371.45, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=388.72, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=416.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=446.61, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=20.45)
            with Note(default_x=576.18, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=20.45, relative_x=-25.83, relative_y=14.55)
            with Backup():
                Duration(144.0)
            with Note(default_x=140.47, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55)
            with Note(default_x=446.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.45)
            with Note(default_x=446.61, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.45)
            with Note(default_x=446.61, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.45)
            with Note(default_x=563.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-25.68, default_y=10.45, relative_x=-24.21, relative_y=3.05)
            with Note(default_x=576.18, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-25.68, default_y=10.45, relative_x=-24.21, relative_y=3.05)
            with Note(default_x=576.18, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-25.68, default_y=10.45, relative_x=-24.21, relative_y=3.05)
            with Backup():
                Duration(144.0)
            with Note(default_x=140.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-24.55, relative_x=-14.56, relative_y=-24.45)
            with Note(default_x=140.47, default_y=-30.0):
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
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-24.55, relative_x=-14.56, relative_y=-24.45)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=533.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=576.54, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=630.97, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
        with Measure(number='11', width=384.09):
            with Note(default_x=56.67, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-28.61, default_y=25.45, relative_x=-25.79, relative_y=22.55)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=186.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=205.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=225.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=243.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=263.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=301.61, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=320.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=340.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=359.32, default_y=-15.0):
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
            with Backup():
                Duration(144.0)
            with Note(default_x=56.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=10.45)
            with Note(default_x=56.67, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=10.45)
            with Note(default_x=56.67, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=10.45)
            with Note(default_x=112.71, default_y=-100.17):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-28.61, default_y=30.45, relative_x=-24.29, relative_y=36.55)
            with Note(default_x=112.71, default_y=-85.17):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-28.61, default_y=30.45, relative_x=-24.29, relative_y=36.55)
            with Note(default_x=224.29, default_y=-100.17):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=30.45, relative_x=-10.83, relative_y=36.55)
            with Note(default_x=224.29, default_y=-85.17):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=30.45, relative_x=-10.83, relative_y=36.55)
            with Backup():
                Duration(144.0)
            with Note(default_x=56.67, default_y=-110.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=112.71, default_y=-110.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.45, relative_x=-25.06, relative_y=2.55)
            with Note(default_x=224.29, default_y=-110.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.45)
        with Measure(number='12', width=1054.66):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(70.17)
            with Note(default_x=141.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=165.94, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=191.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=216.17, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=241.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=266.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=291.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=316.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=341.75, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=366.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=391.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=417.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=445.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=485.45, default_y=-20.0):
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
                Beam('end', number=2)
            with Note(default_x=526.0, default_y=-20.0):
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
                    Arpeggiate(default_x=-13.45, default_y=5.51)
            with Note(default_x=526.0, default_y=-10.0):
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
                with Notations():
                    Arpeggiate(default_x=-13.45, default_y=5.51)
            with Note(default_x=526.0, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.45, default_y=5.51)
            with Note(default_x=595.96, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=636.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=676.33, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=716.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=757.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=796.88, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=837.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=877.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=917.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=972.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=1012.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=140.47, default_y=-85.17):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=30.45, relative_x=-15.33, relative_y=35.05)
            with Note(default_x=525.27, default_y=-85.17):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=30.45, relative_x=-12.33, relative_y=36.55)
            with Note(default_x=756.34, default_y=-85.17):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=30.45, relative_x=-13.83, relative_y=35.05)
            with Backup():
                Duration(144.0)
            with Note(default_x=140.47, default_y=-105.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.45)
            with Note(default_x=140.47, default_y=-95.17):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.45)
            with Note(default_x=525.27, default_y=-105.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.45)
            with Note(default_x=525.27, default_y=-95.17):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.45)
            with Note(default_x=756.34, default_y=-105.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.45)
            with Note(default_x=756.34, default_y=-95.17):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.45)
        with Measure(number='13', width=549.83):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(99.35)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=141.19, default_y=-40.0):
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
                    Arpeggiate(default_x=-13.45, default_y=-24.49)
            with Note(default_x=141.19, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Arpeggiate(default_x=-13.45, default_y=-24.49)
            with Note(default_x=181.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=213.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=236.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=260.27, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=300.57, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=323.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=347.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=370.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=398.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=435.48, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=452.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=469.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=493.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=516.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(144.0)
            with Note(default_x=140.47, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=20.45, relative_x=-13.83, relative_y=25.05)
            with Note(default_x=259.54, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-28.61, default_y=15.45, relative_x=-19.79, relative_y=18.55)
            with Note(default_x=398.08, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=15.45, relative_x=-15.33, relative_y=23.05)
            with Backup():
                Duration(144.0)
            with Note(default_x=140.47, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.45)
            with Note(default_x=140.47, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.45)
            with Note(default_x=259.54, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.45, relative_x=-20.56, relative_y=9.05)
            with Note(default_x=259.54, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.45, relative_x=-20.56, relative_y=9.05)
            with Note(default_x=398.08, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.45)
            with Note(default_x=398.08, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.45)
        with Measure(number='14', width=504.83):
            with Note(default_x=57.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=100.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=129.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=146.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=163.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=180.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=197.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=215.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=232.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=249.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=266.77, default_y=-25.0):
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
            with Note(default_x=283.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(96.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(144.0)
            with Note(default_x=56.67, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-28.61, default_y=15.45, relative_x=-25.79, relative_y=21.55)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=373.29, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=411.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=465.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=56.67, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.81, default_y=5.45)
            with Note(default_x=286.89, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Note(default_x=286.89, default_y=-100.0):
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
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Note(default_x=410.79, default_y=-100.0):
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
                Duration(144.0)
            with Note(default_x=56.67, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55, relative_x=-19.06, relative_y=-7.95)
            with Note(default_x=286.89, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55)
            with Note(default_x=410.79, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=722.41):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(99.35)
                with StaffLayout(number=2):
                    StaffDistance(66.8)
            with Note(default_x=139.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(96.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=539.33, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=539.33, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=143.3, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=192.06, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=219.93, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=247.79, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.66, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=303.52, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=331.39, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=359.25, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=387.12, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=414.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=442.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=470.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=498.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=527.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=588.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=605.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=623.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=640.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=658.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=675.53, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=692.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=142.94, default_y=-116.8):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=303.16, default_y=-116.8):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=539.33, default_y=-116.8):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(144.0)
            with Note(default_x=142.94, default_y=-116.8):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=303.16, default_y=-151.8):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=539.33, default_y=-151.8):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=332.25):
            with Note(default_x=12.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=69.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=109.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=-4.55)
            with Note(default_x=225.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=-4.55)
            with Backup():
                Duration(144.0)
            with Note(default_x=12.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=69.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=109.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55)
            with Note(default_x=109.24, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55)
            with Note(default_x=225.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55)
            with Note(default_x=225.75, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55)
            with Backup():
                Duration(144.0)
            with Note(default_x=12.36, default_y=-116.8):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=12.36, default_y=-101.8):
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
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=185.1, default_y=-141.8):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=226.11, default_y=-131.8):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=272.57, default_y=-131.8):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=301.61, default_y=-116.8):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(144.0)
            with Note(default_x=12.36, default_y=-136.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(96.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='17', width=540.07):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(99.35)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=136.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=202.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=228.79, default_y=-20.0):
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
                Beam('end', number=2)
            with Note(default_x=258.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=420.24, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=486.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=512.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=136.54, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=136.54, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=258.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=258.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=420.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=420.24, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=136.18, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=259.16, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=316.32, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=342.3, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=368.28, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=394.26, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=419.88, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='18', width=514.59):
            with Note(default_x=13.64, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=135.05, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=257.62, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=283.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=308.34, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(144.0)
            with Note(default_x=13.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=13.64, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=135.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=135.05, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=308.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=308.34, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=14.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(36.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=79.14, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=104.68, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=135.05, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=175.91, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=216.76, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=257.62, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=308.7, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=334.23, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=359.77, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=385.31, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=410.84, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=436.38, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=461.92, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=487.46, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='19', width=1054.66):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(99.35)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=138.58, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
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
            with Note(default_x=184.92, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=231.25, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=298.64, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=366.03, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=390.79, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=415.56, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=440.32, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=465.09, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=489.85, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=514.62, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=539.39, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=564.15, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=588.92, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=613.68, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=638.45, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=663.21, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=687.98, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=712.75, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=737.51, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=762.28, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=787.04, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=811.81, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=836.57, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=861.34, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=886.1, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=910.87, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=935.64, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=960.4, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note():
                Rest()
                Duration(48.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(default_x=362.71, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(96.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=138.58, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=231.25, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=264.94, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=298.64, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=332.33, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=365.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=761.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(48.0)
                Voice('6')
                Type('half')
                Staff(2)
            with Note(default_x=365.67, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(36.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=663.21, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=761.92, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(36.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=1006.73, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='20', width=442.94):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(99.35)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=131.18, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=183.93, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=217.02, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=295.6, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=316.57, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=344.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=397.49, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=418.17, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=131.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=131.18, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(96.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=130.82, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=295.6, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=344.74, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=397.49, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=418.17, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='21', width=319.25):
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=70.55, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=114.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=171.43, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=193.6, default_y=0.0):
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
            with Note(default_x=215.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=272.32, default_y=-15.0):
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
            with Note(default_x=294.48, default_y=-10.0):
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
            with Backup():
                Duration(144.0)
            with Note(default_x=14.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=70.55, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=92.72, default_y=-115.0):
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
            with Note(default_x=114.88, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=171.43, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=215.77, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=272.32, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=294.48, default_y=-115.0):
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
        with Measure(number='22', width=292.48):
            with Note(default_x=12.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=65.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=96.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=116.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=203.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note():
                Rest()
                Duration(96.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Note(default_x=203.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=203.61, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=12.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=117.07, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=170.48, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=203.97, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=257.38, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='23', width=452.41):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=127.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=186.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=209.09, default_y=-20.0):
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
                Beam('end', number=2)
            with Note(default_x=231.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=355.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=-9.55)
            with Backup():
                Duration(144.0)
            with Note(default_x=127.74, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=127.74, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(default_x=355.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.55)
            with Note(default_x=355.35, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.55)
            with Backup():
                Duration(144.0)
            with Note(default_x=127.38, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=319.06, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=355.71, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=414.15, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='24', width=602.26):
            with Note(default_x=37.78, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=103.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=170.66, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=236.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=282.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=303.54, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=324.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=345.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=366.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=387.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=408.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=429.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=450.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=470.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=491.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=512.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=533.7, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=567.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=37.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49)
            with Note(default_x=37.78, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(96.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=37.42, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=5.45, relative_x=-21.33, relative_y=7.05)
            with Note(default_x=37.42, default_y=-105.0):
                Chord()
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
                    Arpeggiate(default_x=-13.81, default_y=5.45, relative_x=-21.33, relative_y=7.05)
            with Note(default_x=170.3, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Note(default_x=170.3, default_y=-100.0):
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
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Note(default_x=282.26, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Note(default_x=282.26, default_y=-100.0):
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
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Backup():
                Duration(144.0)
            with Note(default_x=37.42, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=-14.55)
            with Note(default_x=170.3, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55)
            with Note(default_x=282.26, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55)
        with Measure(number='25', width=659.42):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(99.18)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=140.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=-24.55)
            with Note(default_x=140.47, default_y=-30.0):
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
                    Arpeggiate(default_x=-13.81, default_y=-24.55)
            with Note(default_x=217.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=245.02, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=272.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=299.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=327.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=354.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=382.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=411.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=438.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=465.88, default_y=0.0):
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
            with Note(default_x=493.3, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=520.72, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=548.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=575.56, default_y=0.0):
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
            with Note(default_x=602.98, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=630.4, default_y=-5.0):
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
            with Backup():
                Duration(144.0)
            with Note(default_x=140.47, default_y=-110.0):
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
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Note(default_x=140.47, default_y=-100.0):
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
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Note(default_x=217.24, default_y=-110.0):
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
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Note(default_x=217.24, default_y=-100.0):
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
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Note(default_x=438.09, default_y=-110.0):
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
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Note(default_x=438.09, default_y=-100.0):
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
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Backup():
                Duration(144.0)
            with Note(default_x=140.47, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55)
            with Note(default_x=217.24, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55)
            with Note(default_x=438.09, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55)
        with Measure(number='26', width=395.25):
            with Note(default_x=41.51, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=5.51)
            with Note(default_x=104.88, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat-flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=167.53, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=230.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=255.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=280.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=343.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=368.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=41.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=41.51, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=41.51, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(96.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=41.15, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.01, default_y=5.45)
            with Note(default_x=41.15, default_y=-105.0):
                Chord()
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
                    Arpeggiate(default_x=-27.01, default_y=5.45)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Backup():
                Duration(144.0)
            with Note(default_x=41.15, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.55, relative_x=-25.06, relative_y=-17.95)
            with Note(default_x=41.15, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.55, relative_x=-25.06, relative_y=-17.95)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Staff(2)
        with Measure(number='27', width=575.13):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(99.18)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=136.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=217.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=281.96, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=363.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=395.71, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=427.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=509.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=541.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=135.82, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=135.82, default_y=-100.0):
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
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Backup():
                Duration(144.0)
            with Note(default_x=135.82, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Staff(2)
        with Measure(number='28', width=479.54):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=68.61, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=153.11, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=205.55, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=0.45)
            with Note(default_x=322.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.45, default_y=-4.49)
            with Note(default_x=425.13, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note():
                Rest()
                Duration(48.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(default_x=205.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55)
            with Note(default_x=205.55, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55)
            with Note(default_x=321.74, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55, relative_x=-20.56, relative_y=-15.95)
            with Note(default_x=321.74, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.55, relative_x=-20.56, relative_y=-15.95)
            with Backup():
                Duration(144.0)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note(default_x=205.55, default_y=-110.0):
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
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Note(default_x=205.55, default_y=-100.0):
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
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45)
            with Note(default_x=321.74, default_y=-105.0):
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
                    Arpeggiate(default_x=-13.81, default_y=10.45, relative_x=-13.83, relative_y=6.05)
            with Note(default_x=334.32, default_y=-100.0):
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
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=10.45, relative_x=-13.83, relative_y=6.05)
            with Backup():
                Duration(144.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Staff(2)
            with Note(default_x=205.55, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55)
            with Note(default_x=205.55, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55)
            with Note(default_x=321.74, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55)
            with Note(default_x=321.74, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55)
        with Measure(number='29', width=1054.66):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(99.18)
                with StaffLayout(number=2):
                    StaffDistance(72.81)
            with Note(default_x=127.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(144.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Dot()
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(144.0)
            with Note(default_x=130.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=130.7, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=230.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
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
            with Note(default_x=269.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=308.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
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
            with Note(default_x=347.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=852.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=952.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=1002.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=130.34, default_y=-102.81):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=348.23, default_y=-87.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=379.76, default_y=-92.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=411.3, default_y=-87.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=442.83, default_y=-92.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=474.37, default_y=-87.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=505.9, default_y=-92.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=537.44, default_y=-87.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=568.97, default_y=-92.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=600.51, default_y=-87.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=632.04, default_y=-92.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=663.58, default_y=-87.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=695.11, default_y=-92.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=726.65, default_y=-87.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=758.18, default_y=-92.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=789.72, default_y=-87.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=821.25, default_y=-92.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=852.43, default_y=-92.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(144.0)
            with Note(default_x=130.34, default_y=-137.81):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=347.87, default_y=-102.81):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=852.43, default_y=-102.81):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='30', width=394.28):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(99.18)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=136.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=188.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=228.44, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
            with Note(default_x=257.85, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=276.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=312.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=359.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=133.22, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(144.0)
                Voice('2')
                Type('whole')
                Dot()
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=136.18, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=136.18, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=187.64, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=187.64, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=294.25, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=294.25, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(144.0)
            with Note(default_x=136.18, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=187.64, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=294.25, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='31', width=307.51):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=77.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
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
            with Note(default_x=126.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=148.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=214.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=270.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=77.85, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=126.32, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=148.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.39, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.42, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=214.45, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=270.66, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=15.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=77.49, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=214.09, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(144.0)
            with Note(default_x=15.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(96.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='32', width=352.88):
            with Note(default_x=13.64, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=13.64, default_y=-25.0):
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
            with Note(default_x=72.47, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=72.47, default_y=-25.0):
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
            with Note(default_x=202.73, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=202.73, default_y=-25.0):
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
                Duration(144.0)
            with Note(default_x=26.23, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=85.05, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=215.31, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=13.64, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=72.83, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=119.05, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=140.06, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.07, default_y=-115.0):
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
            with Note(default_x=182.08, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=203.09, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=244.08, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=265.09, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=286.1, default_y=-115.0):
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
            with Note(default_x=307.1, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=328.11, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='33', width=583.15):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(99.18)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=136.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=136.18, default_y=-25.0):
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
            with Note(default_x=214.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=214.24, default_y=-25.0):
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
            with Note(default_x=387.39, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=387.39, default_y=-25.0):
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
                Duration(144.0)
            with Note(default_x=136.18, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=214.24, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=387.39, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=136.18, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=214.6, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=275.94, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=303.82, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=331.7, default_y=-125.0):
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
            with Note(default_x=359.87, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=387.75, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=442.14, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=470.02, default_y=-115.0):
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
            with Note(default_x=497.9, default_y=-125.0):
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
            with Note(default_x=525.78, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=553.66, default_y=-115.0):
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
        with Measure(number='34', width=471.52):
            with Note(default_x=14.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=14.36, default_y=-25.0):
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
            with Note(default_x=89.33, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=89.33, default_y=-25.0):
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
            with Note(default_x=255.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=255.35, default_y=-25.0):
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
                Duration(144.0)
            with Note(default_x=14.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=89.33, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=255.35, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=14.36, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=89.7, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=148.6, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=175.38, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.16, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.93, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=255.71, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=282.48, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=309.26, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.04, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=362.81, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=389.59, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=416.37, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=443.14, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='35', width=675.89):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=174.48, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Arpeggiate(default_x=-13.09, default_y=-9.55, relative_x=-25.06, relative_y=-9.45)
            with Note(default_x=248.7, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=275.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=301.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=327.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=354.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=380.57, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=408.74, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=435.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=461.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=487.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=516.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=542.41, default_y=0.0):
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
            with Note(default_x=568.78, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=595.16, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=621.54, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=647.91, default_y=-10.0):
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
            with Backup():
                Duration(144.0)
            with Note(default_x=174.48, default_y=-45.0):
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
                    Arpeggiate(default_x=-24.09, default_y=-19.55, relative_x=-23.02, relative_y=-17.95)
            with Note(default_x=174.48, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=-19.55, relative_x=-23.02, relative_y=-17.95)
            with Note(default_x=174.48, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=-19.55, relative_x=-23.02, relative_y=-17.95)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Backup():
                Duration(144.0)
            with Note(default_x=174.48, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(48.0)
                Voice('6')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Staff(2)
        with Measure(number='36', width=378.78):
            with Note(default_x=12.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=103.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=132.85, default_y=-25.0):
                Grace()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=152.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=214.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=232.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=250.71, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=268.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=286.84, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=326.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=103.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=152.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=214.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=103.27, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=152.79, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=152.79, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=214.22, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=214.22, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(144.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=103.27, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=152.79, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=214.22, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='37', width=572.87):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=170.03, default_y=-40.0):
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
            with Note(default_x=241.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=297.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=323.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=351.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=376.97, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=402.45, default_y=-20.0):
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
            with Note(default_x=458.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=488.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=514.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=545.78, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=170.03, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-35.2, default_y=20.45)
            with Note(default_x=170.03, default_y=-100.0):
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
                with Notations():
                    Arpeggiate(default_x=-35.2, default_y=20.45)
            with Note(default_x=170.03, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-35.2, default_y=20.45)
            with Note(default_x=241.39, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.81, default_y=20.45)
            with Note(default_x=241.39, default_y=-100.0):
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
                with Notations():
                    Arpeggiate(default_x=-30.81, default_y=20.45)
            with Note(default_x=241.39, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.81, default_y=20.45)
            with Note(default_x=402.09, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.81, default_y=20.45)
            with Note(default_x=402.09, default_y=-100.0):
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
                with Notations():
                    Arpeggiate(default_x=-30.81, default_y=20.45)
            with Note(default_x=402.09, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.81, default_y=20.45)
            with Backup():
                Duration(144.0)
            with Note(default_x=170.03, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55, relative_x=-29.56, relative_y=-13.95)
            with Note(default_x=241.39, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55, relative_x=-25.06, relative_y=-10.95)
            with Note(default_x=402.09, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.55, relative_x=-25.06, relative_y=-12.45)
        with Measure(number='38', width=481.8):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
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
            with Note(default_x=73.61, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=116.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=143.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=171.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=225.99, default_y=-20.0):
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
                Beam('end', number=2)
            with Note(default_x=253.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=290.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=307.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=324.53, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=354.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=372.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=399.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=426.13, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=453.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=15.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=73.25, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=252.66, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(144.0)
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=73.25, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=252.66, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='39', width=512.08):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=136.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(96.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('natural')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=401.28, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=468.39, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=239.47, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=265.77, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=292.08, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=359.19, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=400.92, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=139.14, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=291.72, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=400.92, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(144.0)
            with Note(default_x=151.72, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=304.31, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(48.0)
                Voice('6')
                Type('half')
                Staff(2)
        with Measure(number='40', width=204.77):
            with Note(default_x=15.6, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(144.0)
                Voice('1')
                Type('whole')
                Dot()
                Accidental('natural')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=15.6, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(144.0)
                Voice('1')
                Type('whole')
                Dot()
                Staff(1)
            with Note(default_x=15.6, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(144.0)
                Voice('1')
                Type('whole')
                Dot()
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note(default_x=15.6, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(144.0)
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=15.6, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(144.0)
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
            with Note(default_x=15.6, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(144.0)
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
        with Measure(number='41', width=337.81):
            with Note():
                Rest(measure='yes')
                Duration(144.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(144.0)
            with Note():
                Rest(measure='yes')
                Duration(144.0)
                Voice('5')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='42', width=286.16):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    TopSystemDistance(82.8)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                with Key():
                    Fifths(6)
                with Time():
                    Beats('4')
                    BeatType('4')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Fuga', relative_x=-87.0, relative_y=64.0, font_size='14')
                Staff(1)
            with Note():
                Rest()
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=155.47, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=186.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=223.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=242.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=261.4, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='43', width=139.74):
            with Note():
                Rest()
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=18.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=35.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=53.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=81.7, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=109.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='44', width=162.26):
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note(default_x=84.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=117.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=32.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=52.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=84.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=137.5, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='45', width=201.4):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
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
            with Note(default_x=35.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=58.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=81.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=104.92, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=130.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=153.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=58.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=104.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=176.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='46', width=265.09):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=69.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=161.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=202.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=40.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=69.11, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=97.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=115.51, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=133.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=161.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=234.94, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='47', width=380.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(96.12)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=128.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=159.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=190.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=253.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=345.81, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=190.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=221.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=253.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=284.14, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=314.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='48', width=249.92):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=80.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=134.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
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
            with Note(default_x=162.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=193.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=221.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=23.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=52.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=80.07, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=107.24, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=134.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=193.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=221.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='49', width=200.1):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=65.91, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=87.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=109.68, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=131.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=153.45, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=175.33, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=33.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=65.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=87.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=109.68, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=131.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=153.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=175.33, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=65.91, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=131.56, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=153.45, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=175.33, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='50', width=224.45):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.74, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=63.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=95.7, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=119.64, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=174.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=198.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=63.68, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=95.7, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=119.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=151.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=174.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=39.74, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=63.68, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=119.64, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=174.98, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='51', width=402.59):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(96.12)
                with StaffLayout(number=2):
                    StaffDistance(75.32)
            with Note(default_x=141.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=173.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=238.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=271.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=303.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=336.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=141.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=206.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=271.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=336.06, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=368.52, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=141.27, default_y=-120.32):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=173.74, default_y=-125.32):
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
            with Note(default_x=206.2, default_y=-125.32):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=271.13, default_y=-135.32):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=336.06, default_y=-100.32):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='52', width=381.75):
            with Note(default_x=21.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=58.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=84.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=111.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=147.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=207.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=244.39, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=270.94, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=297.49, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=339.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(96.0)
            with Note(default_x=21.66, default_y=-95.32):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=147.77, default_y=-100.32):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.32, default_y=-95.32):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=207.88, default_y=-90.32):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=244.39, default_y=-85.32):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=270.94, default_y=-80.32):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=297.49, default_y=-95.32):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=339.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=356.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(96.0)
            with Note(default_x=21.66, default_y=-105.32):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=111.27, default_y=-105.32):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=207.88, default_y=-105.32):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=297.49, default_y=-110.32):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='53', width=270.33):
            with Note(default_x=17.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=79.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=110.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=141.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=171.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=207.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=238.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=48.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=79.08, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=110.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=141.08, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=207.52, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=238.12, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.86, default_y=-115.32):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=48.47, default_y=-150.32):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=79.08, default_y=-135.32):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=141.08, default_y=-135.32):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=171.69, default_y=-125.32):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=207.52, default_y=-130.32):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=238.12, default_y=-135.32):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='54', width=399.48):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(96.12)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=141.27, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=170.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=206.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=272.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=302.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=320.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=339.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=368.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=141.27, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=170.71, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=206.54, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=243.34, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=272.78, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=339.01, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=368.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=141.27, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=170.71, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=206.54, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=272.78, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=339.01, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='55', width=231.29):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=62.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=87.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=104.46, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=121.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=196.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=62.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=87.29, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=121.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=146.72, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=171.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.1, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=61.83, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=171.82, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='56', width=209.84):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=36.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=60.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=85.49, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=109.99, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=134.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=158.98, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=183.74, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=60.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=158.98, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.5, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=60.99, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=85.49, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=109.99, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=134.48, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=158.98, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=183.74, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='57', width=214.05):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=40.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=64.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=163.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=40.57, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=65.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=89.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=114.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=138.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=187.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=40.57, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=65.12, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=89.68, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=114.23, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=163.34, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='58', width=347.34):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(96.12)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=128.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=179.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=205.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=236.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=268.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=294.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=320.05, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=153.9, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=179.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=205.26, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=236.66, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=268.69, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=294.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=320.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=179.58, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=236.66, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=268.69, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=294.37, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=320.05, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='59', width=220.65):
            with Note(default_x=17.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=73.59, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=97.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=122.08, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=146.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=170.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=194.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=41.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=73.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=170.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=17.23, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=41.47, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=73.59, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=97.83, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=122.08, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=146.32, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=170.56, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=194.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='60', width=237.65):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=65.54, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=119.09, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=65.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=119.09, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=177.88, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.77, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=65.54, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.31, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=119.09, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=151.11, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=177.88, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=209.28, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='61', width=249.03):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=70.68, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=125.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
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
            with Note(default_x=152.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=179.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=207.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=43.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=70.68, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=97.96, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=125.25, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=152.53, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=179.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=43.4, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=70.68, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=97.96, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=125.25, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=152.53, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=179.82, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=207.1, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=224.26, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='62', width=411.51):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(96.12)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=128.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=170.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=205.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=273.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=375.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=239.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=273.33, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=307.47, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=341.62, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=149.55, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=170.89, default_y=-115.0):
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
            with Note(default_x=205.04, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=273.33, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=341.62, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='63', width=299.67):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
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
            with Note(default_x=47.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=82.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=152.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=263.04, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=117.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=163.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=193.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=228.02, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=47.02, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=82.05, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=117.07, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=152.1, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=193.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=263.04, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='64', width=343.49):
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
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
            with Note(default_x=53.89, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=91.99, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=168.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=191.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.01, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=247.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=271.63, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=318.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=130.08, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=168.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=224.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=271.63, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=53.89, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.99, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=130.08, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=168.17, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=224.01, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=271.63, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='65', width=334.59):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=141.27, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=183.88, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=226.48, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
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
            with Note(default_x=253.11, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=279.73, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=306.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=141.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=183.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=226.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=306.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=141.27, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
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
            with Note(default_x=226.48, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=279.73, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='66', width=259.53):
            with Note(default_x=17.86, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.3, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=76.74, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=137.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=199.05, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=17.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=106.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=137.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=228.49, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.86, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.3, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=76.74, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.19, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=137.58, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=169.61, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=199.05, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=228.49, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='67', width=243.97):
            with Note(default_x=17.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
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
            with Note(default_x=44.45, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=71.32, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=187.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=71.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=128.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.23, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=71.68, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=101.44, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=128.67, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=155.89, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=187.92, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=215.14, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='68', width=216.58):
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=66.67, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=140.82, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=165.54, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=190.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=116.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=165.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.23, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=41.95, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=66.67, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.39, default_y=-115.0):
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
            with Note(default_x=116.11, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=140.82, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=165.54, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=190.26, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='69', width=336.38):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(100.16)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=128.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=153.7, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=179.18, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=230.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=281.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=153.7, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=179.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=204.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=230.15, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=255.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=281.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=153.7, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=179.18, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=204.67, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=230.15, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=255.64, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=281.12, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=309.29, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='70', width=275.87):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=43.43, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=74.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=106.3, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=137.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=178.63, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=241.49, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=74.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=149.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=178.63, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=210.06, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=43.43, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=74.87, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.3, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=137.73, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=178.63, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=210.06, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=241.49, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='71', width=234.8):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=66.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=120.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
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
            with Note(default_x=147.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=174.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=206.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.11, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=66.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=93.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=120.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=147.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=174.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=206.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=39.11, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=66.23, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=93.34, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=120.46, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=147.57, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=174.68, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=206.08, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='72', width=207.62):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=36.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=60.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=109.01, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=157.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=36.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=84.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=109.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=133.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=157.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=181.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=60.14, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=157.52, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='73', width=352.38):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(100.16)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=128.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
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
            with Note(default_x=153.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=179.24, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=236.24, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
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
            with Note(default_x=128.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=236.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=268.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=294.05, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=325.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.57, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=153.91, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=179.24, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=211.27, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=236.6, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=294.05, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=325.45, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='74', width=245.81):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=37.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=63.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=88.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=120.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=193.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=63.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=132.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=161.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=193.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=218.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=63.16, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=120.13, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=193.06, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='75', width=231.52):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=115.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=36.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=60.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=128.54, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=157.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=181.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=205.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.36, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=60.35, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=84.35, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=116.32, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=181.93, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='76', width=224.95):
            with Note(default_x=12.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=37.92, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=62.97, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=91.13, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=116.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=141.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=173.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=198.3, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(72.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=173.26, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.72, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=37.92, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=62.97, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.13, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=116.18, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
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
            with Note(default_x=198.3, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='77', width=424.47):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(100.16)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=128.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=164.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=201.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=238.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=274.97, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=349.49, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=386.18, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=201.59, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=274.97, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=312.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=349.49, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=386.18, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=164.9, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=201.59, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=238.28, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=274.97, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=312.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=349.49, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=386.18, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='78', width=346.4):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=91.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=130.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=170.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=265.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
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
            with Note(default_x=305.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=51.53, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=91.06, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=170.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=265.74, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=91.06, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=209.64, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=241.04, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=265.74, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='79', width=283.8):
            with Note(default_x=17.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=50.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=83.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=215.96, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.23, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=50.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=83.47, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=149.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.23, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=50.35, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.47, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=116.59, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=149.71, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=182.84, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=215.96, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=249.08, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='80', width=447.81):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(100.16)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=128.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=222.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=260.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=297.27, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=334.5, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=371.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=408.97, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=176.25, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=222.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=260.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=297.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=334.5, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=371.74, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=408.97, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=151.48, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.25, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.52, default_y=-100.0):
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
            with Note(default_x=222.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=297.27, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=334.5, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=371.74, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=408.97, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='81', width=283.15):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=48.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=80.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=112.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=152.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=184.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=217.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=249.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=112.44, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=152.7, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=217.13, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=249.34, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=48.01, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=80.23, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=152.7, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=217.13, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='82', width=323.7):
            with Note(default_x=21.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=56.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=94.48, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=130.1, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=165.71, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=201.33, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=250.86, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=286.48, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=21.03, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=56.65, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=94.48, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=165.71, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=201.33, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=226.1, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=250.86, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=21.03, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=56.65, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=94.48, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=153.85, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=201.33, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=250.86, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=286.48, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='83', width=421.76):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(100.16)
                with StaffLayout(number=2):
                    StaffDistance(67.92)
            with Note(default_x=128.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=201.2, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=274.18, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=310.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=347.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=383.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-92.92):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=164.71, default_y=-97.92):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=201.2, default_y=-102.92):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=237.69, default_y=-107.92):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=274.18, default_y=-102.92):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=310.68, default_y=-92.92):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=347.17, default_y=-77.92):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-107.92):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=201.2, default_y=-127.92):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=274.18, default_y=-112.92):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=310.68, default_y=-107.92):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=347.17, default_y=-102.92):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='84', width=324.4):
            with Note(default_x=17.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=94.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=170.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
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
            with Note(default_x=208.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=246.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=284.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.86, default_y=-77.92):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=55.98, default_y=-82.92):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=94.1, default_y=-87.92):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=132.22, default_y=-92.92):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=170.33, default_y=-87.92):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=246.57, default_y=-82.92):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.5, default_y=-107.92):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='85', width=308.5):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.73, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=83.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=155.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=190.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=213.1, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=235.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=271.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.73, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=83.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=119.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=155.03, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=235.44, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=271.17, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note(default_x=155.03, default_y=-142.92):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=235.44, default_y=-162.92):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='86', width=451.01):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=132.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=212.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=289.29, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=329.42, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=367.66, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=401.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=132.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=170.26, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=208.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=246.75, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=284.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=325.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=363.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=401.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=425.51, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(96.0)
            with Note(default_x=132.01, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=170.26, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=208.5, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=246.75, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=284.99, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=325.12, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=363.36, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='87', width=340.13):
            with Note(default_x=21.66, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=62.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=94.43, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=185.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=262.65, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=21.66, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=58.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=130.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=153.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=185.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=221.97, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=258.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=302.15, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=21.66, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=94.43, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=185.58, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=221.97, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=258.35, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
        with Measure(number='88', width=263.52):
            with Note(default_x=15.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=46.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=78.41, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=139.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=200.75, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=46.38, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=78.41, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=109.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=139.58, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=200.75, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=78.41, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=139.58, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=170.17, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=200.75, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=231.34, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='89', width=362.16):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(98.06)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=128.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=214.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=249.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=327.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=160.24, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=186.5, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=214.67, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=249.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=275.26, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=301.53, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=160.24, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=186.5, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=214.67, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=231.83, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=249.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=301.53, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=327.79, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='90', width=238.92):
            with Note(default_x=15.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=100.1, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=126.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=179.15, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=73.97, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=126.88, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=153.01, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=179.15, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=47.83, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=73.97, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=100.1, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=126.88, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=153.01, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=179.15, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=211.18, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='91', width=243.74):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=92.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=133.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=159.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=191.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=216.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=41.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=66.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=92.14, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=133.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=159.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=191.25, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=216.69, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=41.25, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=66.69, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.14, default_y=-115.0):
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
            with Note(default_x=133.77, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=159.22, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.25, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=216.69, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='92', width=209.84):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=35.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=58.25, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=81.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=104.5, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=127.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=161.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=185.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=35.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=58.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=81.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=104.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=127.62, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=144.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=161.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=185.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=35.12, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=58.25, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=81.37, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=104.5, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=127.62, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=161.95, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='93', width=322.91):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(98.06)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=141.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=219.66, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=268.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=141.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=180.47, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=219.66, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=296.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=141.27, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=180.47, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=244.16, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=268.65, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=296.82, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='94', width=236.04):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
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
            with Note(default_x=40.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=67.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=95.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=123.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=151.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=178.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=40.17, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=67.92, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.67, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=123.43, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=178.93, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=206.69, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=40.17, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=67.92, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=123.43, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=151.18, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=178.93, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='95', width=258.85):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=41.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=59.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=77.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=107.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=136.55, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=195.17, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=77.94, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=136.55, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=224.47, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=77.94, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=136.55, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=165.86, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=195.17, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=224.47, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='96', width=236.86):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=39.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=67.74, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=95.91, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=123.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=151.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=179.52, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=39.87, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=67.74, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=95.91, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=123.78, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=179.52, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=207.39, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=39.87, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=67.74, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.91, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=123.42, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='97', width=338.36):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(98.06)
                with StaffLayout(number=2):
                    StaffDistance(65.3)
            with Note(default_x=137.01, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=233.0, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=265.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=288.94, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=137.73, default_y=-110.3):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=185.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=232.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=137.37, default_y=-125.3):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=161.28, default_y=-130.3):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=185.19, default_y=-135.3):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=209.1, default_y=-140.3):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=233.0, default_y=-135.3):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=288.94, default_y=-100.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=312.85, default_y=-105.3):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='98', width=253.53):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
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
            with Note(default_x=40.35, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=68.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=97.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=129.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=157.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=195.24, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=40.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=68.69, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=97.04, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=129.07, default_y=-85.3):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=157.41, default_y=-90.3):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=195.24, default_y=-95.3):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=223.59, default_y=-90.3):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-110.3):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=40.35, default_y=-105.3):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=68.69, default_y=-100.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=97.04, default_y=-110.3):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=129.07, default_y=-105.3):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=223.59, default_y=-110.3):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='99', width=250.62):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
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
            with Note(default_x=44.54, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=73.28, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=102.02, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=130.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=159.5, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=191.53, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-105.3):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=44.54, default_y=-75.3):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=73.28, default_y=-80.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=102.02, default_y=-85.3):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=130.76, default_y=-90.3):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=191.53, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=220.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-115.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=44.54, default_y=-110.3):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=73.28, default_y=-105.3):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=130.76, default_y=-125.3):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=159.5, default_y=-120.3):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=191.53, default_y=-115.3):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
        with Measure(number='100', width=212.16):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=59.58, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=115.4, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
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
            with Note(default_x=139.19, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=162.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=35.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=59.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=83.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=115.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=139.19, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=186.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-110.3):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=35.79, default_y=-115.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=59.58, default_y=-120.3):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.37, default_y=-125.3):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=115.4, default_y=-130.3):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=139.19, default_y=-125.3):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=162.98, default_y=-140.3):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=186.77, default_y=-105.3):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='101', width=408.57):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(98.06)
                with StaffLayout(number=2):
                    StaffDistance(67.81)
            with Note(default_x=128.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=203.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=271.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=339.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=140.08, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=169.11, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=237.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=305.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=372.99, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-102.81):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=169.11, default_y=-127.81):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=203.09, default_y=-122.81):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=237.07, default_y=-117.81):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=271.05, default_y=-112.81):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=305.03, default_y=-122.81):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=339.01, default_y=-132.81):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=372.99, default_y=-127.81):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='102', width=316.49):
            with Note(default_x=17.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=94.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=168.17, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
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
                Type('eighth')
                Staff(1)
            with Note(default_x=278.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=29.1, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=58.13, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=131.49, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=168.17, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=204.85, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=241.53, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=17.23, default_y=-137.81):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=58.13, default_y=-132.81):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=94.81, default_y=-127.81):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=131.49, default_y=-162.81):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=168.17, default_y=-142.81):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
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
        with Measure(number='103', width=329.61):
            with Note(default_x=17.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=53.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=88.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=158.53, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
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
            with Note(default_x=193.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=228.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=250.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=272.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=304.84, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=53.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=88.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=123.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=158.53, default_y=-82.81):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=193.69, default_y=-77.81):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=228.86, default_y=-72.81):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.5, default_y=-107.81):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=158.16, default_y=-92.81):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='104', width=460.03):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(98.06)
                with StaffLayout(number=2):
                    StaffDistance(75.32)
            with Note(default_x=128.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.32, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=177.09, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=254.23, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=278.34, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=302.45, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=341.02, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=379.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=419.86, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-100.32):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=215.66, default_y=-85.32):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=302.45, default_y=-85.32):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=341.02, default_y=-90.32):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=379.6, default_y=-95.32):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=419.86, default_y=-95.32):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-100.32):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=215.66, default_y=-95.32):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=302.45, default_y=-100.32):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=379.6, default_y=-105.32):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='105', width=344.53):
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=160.89, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=259.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-100.32):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=51.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=87.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=123.06, default_y=-85.32):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=160.89, default_y=-90.32):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=196.65, default_y=-100.32):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=221.41, default_y=-95.32):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=259.24, default_y=-90.32):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=294.99, default_y=-85.32):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=319.76, default_y=-80.32):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-110.32):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=87.31, default_y=-105.32):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=160.53, default_y=-100.32):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='106', width=250.11):
            with Note(default_x=12.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
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
            with Note(default_x=41.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=70.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=100.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=129.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=161.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=190.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=100.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=129.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=161.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=190.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=219.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-120.32):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=128.79, default_y=-105.32):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='107', width=465.33):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=128.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=207.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=286.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
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
            with Note(default_x=335.44, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=374.92, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=140.08, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=167.69, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=207.16, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=246.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=286.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=310.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=335.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=414.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=439.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=207.16, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=285.74, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='108', width=267.08):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=43.68, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=75.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=107.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=139.1, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=170.42, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=202.11, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=138.38, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=75.37, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=138.74, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=170.42, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.11, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=233.79, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='109', width=322.25):
            with Note(default_x=12.72, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
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
            with Note(default_x=47.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=82.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=117.87, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.77, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=161.68, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=183.58, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=205.49, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=275.58, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=297.49, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(72.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=240.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.72, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=47.77, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=82.82, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=161.68, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=240.54, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='110', width=436.59):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(99.54)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=128.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=164.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=236.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=272.27, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=308.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=344.29, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=200.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=272.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=344.29, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=164.23, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=200.24, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=272.27, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=308.28, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=344.29, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=366.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=389.31, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=411.82, default_y=-120.0):
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
        with Measure(number='111', width=292.98):
            with Note(default_x=12.72, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=46.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=79.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=113.24, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=146.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=180.26, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=213.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=146.39, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.72, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=46.23, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=79.74, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=113.24, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=146.75, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=180.26, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=213.77, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=247.27, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=268.21, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='112', width=325.1):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=92.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=179.58, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=215.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=251.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=28.17, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(72.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=251.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=47.98, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=70.47, default_y=-100.0):
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
            with Note(default_x=92.95, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=128.93, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=157.1, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=179.58, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=215.56, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=287.52, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
        with Measure(number='113', width=374.1):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(99.54)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=128.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=190.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=249.69, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=281.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=311.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=249.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=311.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=128.57, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=160.6, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=190.3, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=219.99, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=249.69, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=281.71, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=311.41, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=342.81, default_y=-115.0):
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
                Beam('end', number=1)
        with Measure(number='114', width=308.79):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=79.01, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=146.02, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
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
            with Note(default_x=181.85, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=240.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=273.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=45.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=79.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=112.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=146.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=181.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=240.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=45.5, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=79.01, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=112.51, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=146.02, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=181.85, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=206.61, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=240.18, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=273.68, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='115', width=371.77):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=46.89, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=154.83, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=189.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=224.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=300.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=154.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=236.48, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=265.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=300.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=46.89, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=79.9, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=100.86, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=133.87, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=154.83, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=189.72, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=224.61, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=265.51, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=335.28, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='116', width=423.34):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(99.54)
                with StaffLayout(number=2):
                    StaffDistance(68.13)
            with Note(default_x=128.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=204.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=239.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=274.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=351.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=386.45, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=140.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=169.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=204.4, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=286.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=315.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=351.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=128.21, default_y=-113.13):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=169.11, default_y=-118.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=204.4, default_y=-123.13):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=239.69, default_y=-128.13):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=274.98, default_y=-133.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=315.87, default_y=-133.13):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=351.16, default_y=-128.13):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=386.45, default_y=-143.13):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='117', width=312.14):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=169.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=202.6, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=223.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=244.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=277.33, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=24.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=67.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=100.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=133.56, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=169.39, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=244.12, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-138.13):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=67.14, default_y=-138.13):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=100.35, default_y=-133.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.56, default_y=-148.13):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=169.03, default_y=-143.13):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='118', width=319.18):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=187.14, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.83, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=84.63, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=122.46, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=154.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=187.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=285.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-143.13):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.83, default_y=-123.13):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=122.46, default_y=-108.13):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=187.5, default_y=-108.13):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=220.02, default_y=-103.13):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=252.54, default_y=-108.13):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=285.06, default_y=-113.13):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='119', width=372.37):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(99.54)
                with StaffLayout(number=2):
                    StaffDistance(67.89)
            with Note(default_x=132.01, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(72.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=312.98, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=132.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=219.06, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=247.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=341.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=132.37, default_y=-117.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=161.27, default_y=-112.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=190.17, default_y=-107.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=247.96, default_y=-127.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=276.86, default_y=-122.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=294.92, default_y=-117.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=312.98, default_y=-112.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='120', width=320.4):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=88.22, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=160.64, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=246.38, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=160.64, default_y=-92.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=246.38, default_y=-77.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-112.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=52.01, default_y=-117.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=88.22, default_y=-122.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=124.43, default_y=-97.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=160.64, default_y=-92.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=196.85, default_y=-87.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=221.61, default_y=-82.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=246.38, default_y=-87.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=282.59, default_y=-92.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='121', width=361.89):
            with Note(default_x=21.3, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=181.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=22.02, default_y=-77.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=61.67, default_y=-82.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=101.68, default_y=-87.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=182.06, default_y=-82.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=221.71, default_y=-107.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=280.28, default_y=-92.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=21.66, default_y=-97.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=61.67, default_y=-92.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=141.69, default_y=-97.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=181.7, default_y=-97.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=221.71, default_y=-92.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=255.27, default_y=-87.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=280.28, default_y=-92.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=320.29, default_y=-97.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='122', width=357.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(99.54)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=128.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(72.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=300.62, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.93, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=162.5, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=189.99, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=217.48, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=244.96, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=272.45, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=300.62, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=128.57, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=162.5, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=189.99, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=217.48, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=244.96, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=272.45, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=300.62, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=328.11, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='123', width=255.87):
            with Note(default_x=13.64, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=141.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
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
            with Note(default_x=14.36, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=82.91, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=142.28, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=168.91, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=195.89, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=14.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=40.98, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=61.95, default_y=-100.0):
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
            with Note(default_x=82.91, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=109.9, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=141.92, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=168.91, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=227.29, default_y=-115.0):
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
        with Measure(number='124', width=209.76):
            with Note(default_x=12.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
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
            with Note(default_x=34.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=56.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=118.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=140.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=162.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=12.72, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=78.85, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=118.87, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=140.91, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=162.95, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=184.99, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=118.87, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=140.91, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=162.95, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=184.99, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='125', width=231.84):
            with Note(default_x=18.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=41.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=65.33, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=128.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=152.1, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=175.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=18.58, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=88.71, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=128.73, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=152.1, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=175.47, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=206.87, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=18.22, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=128.73, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=152.1, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=175.47, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=206.87, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='126', width=459.98):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(67.8)
            with Note(default_x=141.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=180.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=220.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=300.05, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=339.63, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=379.21, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=418.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=141.27, default_y=-132.8):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=260.03, default_y=-127.8):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=300.05, default_y=-122.8):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=379.21, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=418.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=140.91, default_y=-142.8):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=300.05, default_y=-142.8):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=339.63, default_y=-147.8):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=379.21, default_y=-152.8):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=418.8, default_y=-157.8):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='127', width=349.18):
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=57.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=98.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=140.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=181.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=223.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=264.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=306.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=57.27, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=98.74, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=140.22, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=181.69, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=223.16, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=264.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=306.1, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=-162.8):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=57.27, default_y=-132.8):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=98.74, default_y=-137.8):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=140.22, default_y=-142.8):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=181.69, default_y=-147.8):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=223.16, default_y=-117.8):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=264.63, default_y=-122.8):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=306.1, default_y=-127.8):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='128', width=245.51):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=83.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=153.97, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=13.4, relative_y=10.0)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=83.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=118.75, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=153.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-107.8):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=83.16, default_y=-142.8):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=153.97, default_y=-162.8):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')