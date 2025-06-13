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
        CreditWords('The Well-Tempered Clavier Part I Fuga XVIII', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('BWV 863', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J. S. Bach', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Harp', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Harp')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(47)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=308.49):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
                with StaffLayout(number=2):
                    StaffDistance(65.1)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(5)
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
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=171.64, default_y=-110.1, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=203.67, default_y=-115.1, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=226.53, default_y=-110.1, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=243.7, default_y=-105.1, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=260.87, default_y=-100.1, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=283.73, default_y=-105.1, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='2', width=212.85):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-110.1, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=47.83, default_y=-95.1, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=72.59, default_y=-90.1, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.69, default_y=-115.1, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=118.79, default_y=-110.1, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=141.89, default_y=-110.1, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=164.99, default_y=-105.1, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=188.09, default_y=-105.1, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='3', width=279.28):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=83.21, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=127.9, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=160.41, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=181.37, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=201.69, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=234.2, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=18.2, default_y=-125.1, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=50.7, default_y=-120.1, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=83.21, default_y=-115.1, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=127.9, default_y=-115.1, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=160.41, default_y=-120.1, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=181.37, default_y=-115.1, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=201.69, default_y=-110.1, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=234.2, default_y=-115.1, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=254.51, default_y=-110.1, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='4', width=254.37):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=18.2, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=50.23, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=85.15, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=113.09, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=141.02, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=168.96, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=196.9, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=224.83, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=18.2, default_y=-105.1, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=50.23, default_y=-110.1, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=67.69, default_y=-105.1, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=85.15, default_y=-100.1, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=113.09, default_y=-110.1, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=141.02, default_y=-105.1, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=196.9, default_y=-115.1, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='5', width=407.71):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(112.0)
                with StaffLayout(number=2):
                    StaffDistance(108.1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=193.24, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=242.22, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=277.83, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=302.6, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=324.86, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=360.68, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=122.01, default_y=-65.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=193.24, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=242.22, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=277.83, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=302.6, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=324.86, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=360.68, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=382.94, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=122.01, default_y=-153.1, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=157.63, default_y=-158.1, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=193.24, default_y=-163.1, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=242.22, default_y=-168.1, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=277.83, default_y=-153.1, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=360.68, default_y=-148.1, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='6', width=309.38):
            with Note(default_x=17.23, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=50.94, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=103.41, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=137.12, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=170.83, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=204.54, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=240.36, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=274.07, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=50.94, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=82.34, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.41, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=137.12, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=170.83, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=240.36, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-143.1, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=103.41, default_y=-148.1, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=170.47, default_y=-153.1, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='7', width=337.9):
            with Note(default_x=12.0, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=49.06, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=95.39, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=169.52, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=206.58, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=229.74, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=252.91, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=289.97, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=313.13, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=132.45, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=169.52, default_y=-65.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=289.97, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-153.1, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=49.06, default_y=-158.1, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=72.23, default_y=-153.1, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=95.39, default_y=-148.1, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=132.45, default_y=-158.1, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=169.52, default_y=-168.1, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=206.58, default_y=-163.1, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=289.97, default_y=-143.1, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=95.39, default_y=-168.1, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=169.52, default_y=-178.1, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=206.58, default_y=-173.1, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=229.74, default_y=-168.1, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=252.91, default_y=-163.1, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=289.97, default_y=-168.1, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='8', width=430.85):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(112.0)
                with StaffLayout(number=2):
                    StaffDistance(103.59)
            with Note(default_x=118.21, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=155.91, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=179.48, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=203.04, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=240.74, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=278.45, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=353.85, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=155.91, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=240.74, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=278.45, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=353.85, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-133.59, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=240.74, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=278.45, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=353.85, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-168.59, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=155.91, default_y=-153.59, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=203.04, default_y=-148.59, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=240.74, default_y=-173.59, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=278.45, default_y=-168.59, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=316.15, default_y=-168.59, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=353.85, default_y=-163.59, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=391.55, default_y=-163.59, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='9', width=287.2):
            with Note(default_x=15.8, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=49.53, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=83.25, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=150.7, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=218.15, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=116.98, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=150.7, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=218.15, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=116.98, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=150.7, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=218.15, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-183.59, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=116.98, default_y=-163.59, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=150.7, default_y=-158.59, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=184.43, default_y=-158.59, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=218.15, default_y=-153.59, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=251.88, default_y=-153.59, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='10', width=336.94):
            with Note(default_x=12.0, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=50.2, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=82.23, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=106.11, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=182.52, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=258.93, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=144.31, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=182.52, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=258.93, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=144.31, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=182.52, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=258.93, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-173.59, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=144.31, default_y=-153.59, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=182.52, default_y=-148.59, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=220.72, default_y=-148.59, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=258.93, default_y=-143.59, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=297.13, default_y=-143.59, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='11', width=474.02):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(112.0)
                with StaffLayout(number=2):
                    StaffDistance(74.91)
            with Note(default_x=118.21, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=156.76, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=195.32, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=284.73, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=323.29, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=348.05, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=378.38, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=416.93, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=448.33, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=156.76, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=195.32, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=233.87, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=257.96, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=284.73, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=323.29, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=378.38, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=416.93, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-99.91, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=195.32, default_y=-99.91, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=284.73, default_y=-109.91, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=323.29, default_y=-104.91, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=348.05, default_y=-99.91, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=378.38, default_y=-94.91, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=416.93, default_y=-99.91, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-134.91, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('6')
                Type('half')
                Staff(2)
        with Measure(number='12', width=313.76):
            with Note(default_x=15.8, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=51.63, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=73.87, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=98.64, default_y=15.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=134.22, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=169.81, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=240.99, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=98.64, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=169.45, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-104.91, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=51.63, default_y=-89.91, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=98.64, default_y=-84.91, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=134.22, default_y=-109.91, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=169.81, default_y=-104.91, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=205.4, default_y=-104.91, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=240.99, default_y=-99.91, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=276.57, default_y=-99.91, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='13', width=267.21):
            with Note(default_x=12.0, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=42.74, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=61.95, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=81.17, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=111.91, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=142.65, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=204.13, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=81.17, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=142.29, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-119.91, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=111.91, default_y=-119.91, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=142.65, default_y=-114.91, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=173.39, default_y=-114.91, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=204.13, default_y=-109.91, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=234.87, default_y=-109.91, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='14', width=407.74):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(112.0)
                with StaffLayout(number=2):
                    StaffDistance(73.59)
            with Note(default_x=118.21, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=151.86, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=172.88, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=204.28, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=237.92, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=271.56, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=338.85, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=204.28, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=271.2, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-128.59, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=237.92, default_y=-128.59, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=271.56, default_y=-123.59, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=305.21, default_y=-123.59, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=338.85, default_y=-118.59, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=372.49, default_y=-118.59, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='15', width=364.52):
            with Note(default_x=12.0, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
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
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=223.04, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=312.17, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=50.37, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=74.35, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=98.34, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=136.71, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=160.69, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=184.67, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=223.04, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=247.02, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=273.8, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=312.17, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=338.94, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-138.59, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=50.37, default_y=-133.59, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=98.34, default_y=-128.59, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=136.71, default_y=-123.59, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=184.67, default_y=-118.59, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=273.8, default_y=-118.59, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=312.17, default_y=-108.59, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(1)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=98.34, default_y=-138.59, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=184.67, default_y=-143.59, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=223.04, default_y=-138.59, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=247.02, default_y=-133.59, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=273.8, default_y=-128.59, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=312.17, default_y=-138.59, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='16', width=282.73):
            with Note(default_x=15.8, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=88.16, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=152.13, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.96, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=68.06, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=88.16, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=120.33, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=152.49, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=216.81, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-103.59, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=88.16, default_y=-108.59, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=120.33, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=152.49, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=216.81, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-138.59, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=47.96, default_y=-123.59, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=88.16, default_y=-118.59, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=120.33, default_y=-143.59, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=152.49, default_y=-138.59, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=184.65, default_y=-138.59, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=216.81, default_y=-133.59, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=248.97, default_y=-133.59, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='17', width=369.6):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(90.4)
            with Note(default_x=118.21, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=150.24, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=179.52, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=208.8, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=240.82, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=270.1, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=306.7, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=338.73, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=338.73, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-115.4, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=179.52, default_y=-135.4, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=240.82, default_y=-140.4, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=270.1, default_y=-135.4, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=288.4, default_y=-130.4, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=306.7, default_y=-125.4, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=338.73, default_y=-130.4, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-170.4, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=150.24, default_y=-165.4, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=179.52, default_y=-160.4, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=208.8, default_y=-155.4, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=240.82, default_y=-150.4, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=338.73, default_y=-150.4, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=261.74):
            with Note(default_x=17.23, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=53.06, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=81.79, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=110.52, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=141.92, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=170.65, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=202.68, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=231.41, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=110.52, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=141.92, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=231.41, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-135.4, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=53.06, default_y=-120.4, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=81.79, default_y=-115.4, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=110.52, default_y=-140.4, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=141.92, default_y=-135.4, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=170.65, default_y=-135.4, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.68, default_y=-130.4, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=231.41, default_y=-130.4, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-145.4, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=81.43, default_y=-150.4, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=202.68, default_y=-155.4, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
        with Measure(number='19', width=423.65):
            with Note(default_x=12.0, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=23.87, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=55.26, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=91.09, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=118.12, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=226.26, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=269.52, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=296.56, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=324.72, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=367.98, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-150.4, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=55.26, default_y=-145.4, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=118.12, default_y=-140.4, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=226.26, default_y=-140.4, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=269.52, default_y=-145.4, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=296.56, default_y=-140.4, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=324.72, default_y=-135.4, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=367.98, default_y=-140.4, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=395.01, default_y=-135.4, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-150.4, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Staff(2)
            with Note(default_x=145.16, default_y=-185.4, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=172.19, default_y=-180.4, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.23, default_y=-175.4, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=226.26, default_y=-170.4, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=269.52, default_y=-155.4, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=367.98, default_y=-150.4, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='20', width=526.68):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(91.62)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=122.01, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=170.87, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=231.94, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=280.79, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=329.65, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=378.51, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=427.36, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=476.22, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=122.01, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=170.87, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=201.4, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=231.94, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=280.79, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=329.65, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=427.36, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=122.01, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=231.94, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=329.29, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='21', width=528.32):
            with Note(default_x=15.8, default_y=-65.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=72.57, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=143.53, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=271.26, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=328.03, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=363.51, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=398.99, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=434.47, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=469.95, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-65.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=214.49, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=270.9, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=328.03, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=398.99, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=469.95, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=72.57, default_y=-135.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=108.05, default_y=-140.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=143.53, default_y=-135.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=179.01, default_y=-145.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=214.49, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=270.9, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='22', width=601.62):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(91.62)
                with StaffLayout(number=2):
                    StaffDistance(66.23)
            with Note(default_x=141.76, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=371.07, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=421.89, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=453.92, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=485.68, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=517.44, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=549.2, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=142.12, default_y=-121.23, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=192.94, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=256.46, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=320.25, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=370.71, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=421.89, default_y=-106.23, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=485.68, default_y=-101.23, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=549.2, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=142.12, default_y=-126.23, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=192.94, default_y=-131.23, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=224.7, default_y=-136.23, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=256.46, default_y=-131.23, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=288.22, default_y=-141.23, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=320.25, default_y=-126.23, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(2.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=370.71, default_y=-121.23, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='23', width=453.37):
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.59, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=227.52, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=273.49, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=306.5, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=336.83, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=365.56, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=394.3, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.59, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=227.52, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=273.49, default_y=-96.23, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=306.5, default_y=-101.23, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=336.83, default_y=-96.23, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=394.3, default_y=-106.23, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.59, default_y=-121.23, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=63.93, default_y=-126.23, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=92.67, default_y=-131.23, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=121.4, default_y=-126.23, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.8, default_y=-136.23, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=181.54, default_y=-121.23, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=227.52, default_y=-116.23, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=336.83, default_y=-116.23, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='stop')
                Voice('6')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=423.03, default_y=-121.23, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='24', width=596.48):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(91.62)
                with StaffLayout(number=2):
                    StaffDistance(74.91)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=254.14, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=380.22, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=429.55, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=465.38, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=496.21, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=545.55, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=179.88, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=210.71, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=254.14, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=284.97, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.0, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=347.83, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=379.86, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-114.91, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=149.05, default_y=-114.91, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.88, default_y=-99.91, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.71, default_y=-104.91, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=254.14, default_y=-109.91, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=284.97, default_y=-114.91, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=317.0, default_y=-109.91, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=380.22, default_y=-114.91, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=429.55, default_y=-109.91, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=465.38, default_y=-104.91, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=496.21, default_y=-99.91, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=545.55, default_y=-94.91, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-134.91, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=254.14, default_y=-129.91, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=380.22, default_y=-149.91, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='25', width=458.52):
            with Note(default_x=15.8, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=61.36, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=106.91, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.86, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=229.14, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=286.08, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=343.03, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=399.97, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=61.36, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=106.91, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.86, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=229.14, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=343.03, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=371.5, default_y=-114.91, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=399.97, default_y=-109.91, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=428.44, default_y=-104.91, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-89.91, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=106.91, default_y=-89.91, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=135.38, default_y=-84.91, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.86, default_y=-89.91, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.66, default_y=-94.91, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=229.14, default_y=-99.91, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=257.61, default_y=-104.91, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.08, default_y=-109.91, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.55, default_y=-114.91, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=343.03, default_y=-119.91, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=430.78):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(91.62)
                with StaffLayout(number=2):
                    StaffDistance(71.5)
            with Note(default_x=118.21, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=152.83, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=187.45, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=256.68, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=291.3, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=334.57, default_y=15.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-96.5, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=187.45, default_y=-101.5, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=222.07, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=256.68, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=356.21, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=384.37, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=406.01, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-121.5, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=152.83, default_y=-116.5, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=187.45, default_y=-111.5, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=222.07, default_y=-101.5, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=256.32, default_y=-96.5, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=187.45, default_y=-121.5, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=256.68, default_y=-131.5, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=291.3, default_y=-126.5, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=312.94, default_y=-121.5, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=334.57, default_y=-116.5, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=384.37, default_y=-121.5, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='27', width=274.57):
            with Note(default_x=15.8, default_y=15.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=46.97, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=78.14, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=140.13, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=109.32, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=140.49, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=171.66, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=191.14, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=210.62, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-101.5, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=109.32, default_y=-106.5, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=140.49, default_y=-106.5, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=210.62, default_y=-111.5, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-126.5, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=46.97, default_y=-111.5, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=78.14, default_y=-106.5, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=109.32, default_y=-131.5, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=140.49, default_y=-126.5, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=171.66, default_y=-126.5, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=210.62, default_y=-121.5, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=241.8, default_y=-121.5, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='28', width=349.65):
            with Note(default_x=12.0, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=90.87, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=180.83, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=215.88, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=237.79, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=259.7, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=281.6, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=313.0, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.05, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=68.96, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=90.87, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.77, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=145.78, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=180.47, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-106.5, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-141.5, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=47.05, default_y=-146.5, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=90.87, default_y=-151.5, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=145.78, default_y=-136.5, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=180.83, default_y=-156.5, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=215.88, default_y=-161.5, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=259.7, default_y=-166.5, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=313.0, default_y=-151.5, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='29', width=468.98):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(91.62)
                with StaffLayout(number=2):
                    StaffDistance(67.12)
            with Note(default_x=118.21, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=292.98, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=329.72, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=352.68, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=375.65, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=398.61, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=430.64, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.57, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=155.32, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=178.28, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=201.24, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=224.21, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=256.23, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=292.62, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=118.57, default_y=-132.12, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=155.32, default_y=-137.12, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=201.24, default_y=-142.12, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=256.23, default_y=-127.12, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=292.98, default_y=-147.12, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=329.72, default_y=-152.12, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=375.65, default_y=-157.12, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=430.64, default_y=-142.12, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='30', width=281.37):
            with Note(default_x=15.8, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.8, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=67.79, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=87.79, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=119.79, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=151.78, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=215.78, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=87.79, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=151.42, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-162.12, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=119.79, default_y=-127.12, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=151.78, default_y=-122.12, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=183.78, default_y=-122.12, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=215.78, default_y=-117.12, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=247.77, default_y=-117.12, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='31', width=304.64):
            with Note(default_x=12.0, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=45.97, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=67.2, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=99.23, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=133.2, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=167.17, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=235.11, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=99.23, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=166.81, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-137.12, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=133.2, default_y=-137.12, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=167.17, default_y=-132.12, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=201.14, default_y=-132.12, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=235.11, default_y=-127.12, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=269.08, default_y=-127.12, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='32', width=626.9):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(97.79)
            with Note(default_x=122.01, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=416.87, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=558.29, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=122.01, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=175.62, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=209.13, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=242.64, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=296.25, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=329.75, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=363.26, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=416.87, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=457.77, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=491.27, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=558.29, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=591.79, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=242.64, default_y=-142.79, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=363.26, default_y=-147.79, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=416.87, default_y=-142.79, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=457.77, default_y=-137.79, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=491.27, default_y=-132.79, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=558.29, default_y=-137.79, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=122.01, default_y=-177.79, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=175.62, default_y=-172.79, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=242.64, default_y=-167.79, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=296.25, default_y=-162.79, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=363.26, default_y=-157.79, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=428.73, default_y=-147.79, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=491.27, default_y=-147.79, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=524.78, default_y=-142.79, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=558.29, default_y=-147.79, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=591.79, default_y=-152.79, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='33', width=428.1):
            with Note(default_x=17.23, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=140.04, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=250.28, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=85.09, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.56, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=140.04, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=195.0, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=250.64, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=338.57, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-142.79, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=85.09, default_y=-127.79, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=140.04, default_y=-122.79, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=195.0, default_y=-147.79, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=250.64, default_y=-142.79, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=294.6, default_y=-142.79, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=338.57, default_y=-137.79, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=382.53, default_y=-137.79, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-157.79, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=49.26, default_y=-162.79, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.09, default_y=-167.79, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.56, default_y=-172.79, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=140.04, default_y=-177.79, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=167.52, default_y=-182.79, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.0, default_y=-177.79, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=222.47, default_y=-172.79, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=250.64, default_y=-167.79, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=338.57, default_y=-172.79, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=382.53, default_y=-177.79, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='34', width=398.04):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(97.79)
            with Note(default_x=118.21, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=200.41, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=265.4, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=150.88, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=175.65, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=200.41, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=233.09, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=265.76, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=331.1, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-157.79, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=233.09, default_y=-157.79, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=265.76, default_y=-152.79, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=298.43, default_y=-152.79, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=331.1, default_y=-147.79, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=363.77, default_y=-147.79, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-182.79, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=150.88, default_y=-172.79, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=200.41, default_y=-192.79, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(1)
                Duration(8.0)
                Voice('6')
                Type('half')
                Staff(2)
        with Measure(number='35', width=308.9):
            with Note(default_x=15.8, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=58.67, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=101.17, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=238.71, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=135.83, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=170.12, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=204.42, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=238.71, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=273.0, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-167.79, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.23, default_y=-157.79, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.67, default_y=-152.79, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.1, default_y=-147.79, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.17, default_y=-142.79, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=238.71, default_y=-147.79, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(1)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=135.83, default_y=-177.79, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=170.12, default_y=-172.79, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=204.42, default_y=-172.79, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=238.71, default_y=-167.79, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=273.0, default_y=-167.79, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='36', width=348.06):
            with Note(default_x=15.8, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=151.18, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=192.55, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=231.03, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=269.5, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=307.98, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.85, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.61, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.66, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.71, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=151.18, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=192.19, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-152.79, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=151.18, default_y=-132.79, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=192.55, default_y=-127.79, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=231.03, default_y=-127.79, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=269.5, default_y=-122.79, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=307.98, default_y=-122.79, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-187.79, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=112.35, default_y=-152.79, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=269.5, default_y=-157.79, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='37', width=523.1):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(103.59)
            with Note(default_x=118.57, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
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
            with Note(default_x=263.04, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=321.21, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=371.43, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=402.83, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=428.63, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=469.91, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.57, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=144.37, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.17, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.97, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=221.77, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=263.04, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=289.82, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=321.21, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=371.43, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=469.91, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=495.7, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.21, default_y=-148.59, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=321.21, default_y=-148.59, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=371.43, default_y=-143.59, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=402.83, default_y=-138.59, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=428.63, default_y=-133.59, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=469.91, default_y=-128.59, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.57, default_y=-168.59, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=170.17, default_y=-163.59, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=221.77, default_y=-158.59, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=263.04, default_y=-153.59, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=337.38, default_y=-148.59, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='38', width=275.42):
            with Note(default_x=15.8, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.83, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=86.79, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=117.96, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=149.13, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=180.3, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=211.47, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=242.65, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.83, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=67.31, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=86.79, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=117.96, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=149.13, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=211.47, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-123.59, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=86.79, default_y=-128.59, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=149.13, default_y=-123.59, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=211.47, default_y=-118.59, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.44, default_y=-148.59, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=211.47, default_y=-153.59, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='39', width=256.48):
            with Note(default_x=17.23, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=48.63, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=77.3, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=196.8, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=106.7, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=138.73, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=196.8, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=225.84, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-138.59, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=106.7, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=138.73, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=196.8, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-153.59, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=106.7, default_y=-158.59, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=138.73, default_y=-188.59, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=167.77, default_y=-188.59, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=196.8, default_y=-183.59, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=225.84, default_y=-183.59, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='40', width=667.3):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.03)
            with Note(default_x=122.01, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=257.93, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=325.89, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=393.85, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=461.81, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=597.73, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=122.01, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=189.97, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=257.93, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=393.85, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=461.81, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=529.77, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=122.01, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=325.89, default_y=-130.03, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=393.49, default_y=-125.03, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=122.01, default_y=-165.03, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=189.97, default_y=-160.03, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=257.93, default_y=-155.03, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=393.49, default_y=-160.03, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='41', width=387.7):
            with Note(default_x=24.35, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(16.0)
            with Note(default_x=24.35, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('whole')
                Accidental('sharp')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=24.35, default_y=-125.03, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-40.0, relative_y=-55.5)
            with Backup():
                Duration(16.0)
            with Note(default_x=24.35, default_y=-145.03, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('6')
                Type('whole')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')