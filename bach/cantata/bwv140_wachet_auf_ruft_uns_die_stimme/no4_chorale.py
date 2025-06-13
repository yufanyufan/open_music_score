with ScorePartwise(version='3.1'):
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
        CreditWords('Chorale: Zion hört die Wächter singen, adapted to keybaord (A = 415 Hz)', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_family='Times New Roman', font_size='16')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('From: Wachet auf, ruft uns die Stimme, BWV 140', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_family='Times New Roman', font_size='14')
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
        with Measure(number='0', implicit='yes', width=149.84):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    TopSystemDistance(170.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                Staves(3)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('C')
                    Line(3)
                with Clef(number=3):
                    Sign('F')
                    Line(4)
            with Note(default_x=114.01, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
        with Measure(number='1', width=216.14):
            with Note(default_x=15.8, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.97, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=50.13, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=73.41, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=96.68, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=119.95, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=143.23, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=166.5, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=191.27, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=73.41, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=119.95, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=166.5, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='2', width=236.43):
            with Note(default_x=12.0, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.17, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=46.33, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=72.29, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=98.24, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=124.19, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=150.15, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=202.06, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=72.29, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=124.19, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Staff(3)
        with Measure(number='3', width=216.14):
            with Note(default_x=15.8, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.97, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=50.13, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=73.41, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=96.68, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=119.95, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=143.23, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=166.5, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=191.27, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=73.41, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=119.95, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=166.5, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='4', width=236.43):
            with Note(default_x=12.0, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.17, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=46.33, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=72.29, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=98.24, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=124.19, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=150.15, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=202.06, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=72.29, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=124.19, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Staff(3)
        with Measure(number='5', width=425.67):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(91.09)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Attributes():
                with Key(number=1):
                    Fifths(2)
            with Note(default_x=89.15, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=142.24, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=166.37, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.5, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.63, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=238.76, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=262.9, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.03, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=311.79, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=336.56, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=375.17, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=399.93, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=142.24, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=238.76, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=336.56, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='6', width=320.62):
            with Note(default_x=12.0, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.32, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.64, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.96, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.28, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=118.6, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.92, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.25, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=182.57, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=216.68, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=284.91, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=97.28, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=182.57, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=250.79, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='7', width=308.71):
            with Note(default_x=12.0, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=53.01, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=123.1, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=158.15, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=180.06, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=201.96, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=272.06, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=88.05, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=158.15, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=237.01, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='8', width=325.13):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(91.09)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=101.19, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=127.97, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=179.18, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=204.78, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=225.75, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=246.71, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=297.92, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=101.19, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=153.57, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=204.78, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(3)
            with Note(default_x=272.32, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='9', width=353.7):
            with Note(default_x=12.0, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.07, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=54.14, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=87.86, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=119.25, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=140.33, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=174.04, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=195.11, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=216.18, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.26, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=258.33, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=279.4, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=304.17, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=328.93, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=87.86, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(3)
            with Note(default_x=174.04, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=258.33, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='10', width=376.17):
            with Note(default_x=15.8, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.57, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=63.01, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=93.88, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=111.04, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=132.01, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=154.46, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=185.32, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=216.72, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.17, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=261.62, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=284.06, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=306.51, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=328.96, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=351.41, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=93.88, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=185.32, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=284.06, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='11', width=542.41):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(91.09)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=89.15, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=132.67, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=176.19, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=197.16, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=218.12, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=239.09, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=263.86, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.51, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=327.16, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=358.81, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=390.46, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=422.12, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=453.77, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=497.29, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=132.67, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=176.19, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=263.86, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=327.16, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=390.46, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=453.77, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=497.29, default_y=-270.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='12', width=512.58):
            with Note(default_x=15.8, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.29, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=128.77, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=153.53, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=178.3, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=203.06, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=227.83, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=252.59, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=277.36, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=302.12, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=326.89, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=464.96, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=61.82, default_y=-275.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=128.77, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=326.89, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=372.91, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=418.94, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=464.96, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='13', width=328.97):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=89.15, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.2, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=125.24, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=154.12, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=182.99, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=211.87, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=240.75, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=269.62, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=298.5, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note(default_x=211.87, default_y=-155.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=269.62, default_y=-145.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=125.24, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=154.12, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=182.99, default_y=-270.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=211.87, default_y=-275.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=269.62, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='14', width=249.92):
            with Note(default_x=12.0, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.55, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=47.09, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=75.17, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=103.24, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=131.32, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=159.39, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=215.54, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=75.17, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=131.32, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=187.47, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=75.17, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=131.32, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=187.47, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='15', width=226.19):
            with Note(default_x=12.36, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.53, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=46.69, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=72.11, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=97.52, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=122.93, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=148.35, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=173.76, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=199.18, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=122.57, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.36, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=72.11, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=122.93, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=173.76, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='16', width=249.92):
            with Note(default_x=12.0, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.55, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=47.09, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=75.17, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=103.24, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=131.32, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=159.39, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=215.54, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=187.47, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=75.17, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=131.32, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=187.47, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='17', width=405.58):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=89.15, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=130.16, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=205.69, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=243.46, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=267.07, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=290.67, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=366.21, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=167.93, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=243.46, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=290.67, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=328.44, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=167.93, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=243.46, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=290.67, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=328.44, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
                with Notations():
                    Tied(type='start')
        with Measure(number='18', width=331.19):
            with Note(default_x=17.23, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=53.98, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=127.47, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=164.22, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=187.19, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=210.16, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=17.23, default_y=-115.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=127.47, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=164.22, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=246.9, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=269.87, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=292.84, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=17.23, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=53.98, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=90.73, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=127.47, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=164.22, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=210.16, default_y=-270.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=246.9, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=292.84, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='19', width=318.23):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=119.8, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=155.43, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=226.67, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=248.93, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=271.2, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=293.46, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.58, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.94, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=48.56, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=84.18, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=119.8, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=155.43, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=191.05, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=226.67, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='20', width=502.6):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=90.09, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=116.43, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.77, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.11, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=195.45, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=237.59, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=263.93, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=290.27, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=316.61, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=342.95, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=369.29, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=395.63, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=421.97, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=448.31, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=474.66, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=195.45, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=290.27, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=395.63, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=90.09, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=195.45, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=290.27, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=395.63, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='21', width=275.8):
            with Note(default_x=12.0, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=43.64, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=241.42, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=75.29, default_y=-145.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=106.93, default_y=-140.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.71, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=146.49, default_y=-140.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=178.13, default_y=-145.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=209.78, default_y=-150.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=43.64, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=75.29, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=146.49, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=209.78, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=241.42, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='22', width=276.6):
            with Note(default_x=16.16, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.77, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=55.38, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=86.75, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=118.13, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=149.5, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=180.88, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=212.25, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=243.63, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-155.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=16.16, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=86.75, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=149.5, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=212.25, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='23', width=310.45):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=89.15, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=106.32, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=123.48, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=148.91, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=174.34, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=199.78, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=225.21, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=276.07, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=148.91, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=199.78, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Staff(3)
        with Measure(number='24', width=213.01):
            with Note(default_x=15.8, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.97, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=50.13, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=72.8, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.47, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=118.14, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=140.81, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.48, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=188.24, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=72.8, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=118.14, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=163.48, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='25', width=233.3):
            with Note(default_x=12.0, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.17, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=46.33, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=71.76, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=97.19, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=122.63, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=148.06, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=198.92, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=71.76, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=122.63, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Staff(3)
        with Measure(number='26', width=298.24):
            with Note(default_x=12.0, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=53.55, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=72.44, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.33, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.22, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=129.1, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=147.99, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.96, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.72, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=218.49, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=248.71, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=273.48, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=53.55, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=129.1, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=218.49, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='27', width=408.96):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=89.15, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=111.25, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.35, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.44, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=177.54, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=199.64, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.74, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=243.83, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=265.93, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=301.29, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=372.0, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=177.54, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=265.93, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=336.65, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='28', width=339.47):
            with Note(default_x=12.0, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=53.01, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=126.36, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=163.03, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=180.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=201.17, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=227.84, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=301.19, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=89.68, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=163.03, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=264.52, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='29', width=306.57):
            with Note(default_x=17.23, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=49.53, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=114.14, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=146.44, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=163.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=184.57, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=208.06, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=272.66, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=17.23, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=81.83, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=146.44, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(3)
            with Note(default_x=240.36, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='30', width=593.53):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=89.15, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=119.56, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.97, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=168.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=187.99, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=206.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=226.0, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=245.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=276.41, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=306.82, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=348.63, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=379.04, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=409.46, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=439.87, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=470.28, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=500.69, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=531.1, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=561.51, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=226.0, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(3)
            with Note(default_x=348.63, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=470.28, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='31', width=461.47):
            with Note(default_x=15.8, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=45.09, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=74.37, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=114.64, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=132.95, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=153.91, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=183.2, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=223.47, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=254.86, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=284.15, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=313.44, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=342.72, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=372.01, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=401.3, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=430.58, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=114.64, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=223.47, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=342.72, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='32', width=556.53):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=89.15, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=134.36, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=179.57, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=200.53, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=221.5, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=242.47, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=267.23, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=300.11, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=332.99, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=365.87, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=398.75, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=431.63, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=464.51, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=509.72, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=134.36, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=179.57, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=267.23, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=332.99, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=398.75, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=464.51, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=509.72, default_y=-270.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='33', width=498.47):
            with Note(default_x=15.8, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.76, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=129.43, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=154.2, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=178.96, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=203.73, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=228.49, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.16, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=286.93, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=311.69, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=450.57, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=62.09, default_y=-275.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=129.43, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=311.69, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=357.98, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=404.28, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=450.57, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='34', width=328.97):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=89.15, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.2, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=125.24, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=154.12, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=182.99, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=211.87, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=240.75, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=269.62, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=298.5, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note(default_x=211.87, default_y=-155.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=269.62, default_y=-145.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=125.24, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=154.12, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=182.99, default_y=-270.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=211.87, default_y=-275.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=269.62, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='35', width=249.92):
            with Note(default_x=12.0, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.55, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=47.09, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=75.17, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=103.24, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=131.32, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=159.39, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=215.54, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=75.17, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=131.32, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=187.47, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=75.17, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=131.32, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=187.47, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='36', width=226.19):
            with Note(default_x=12.36, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.53, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=46.69, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=72.11, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=97.52, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=122.93, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=148.35, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=173.76, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=199.18, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=122.57, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.36, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=72.11, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=122.93, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=173.76, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='37', width=249.92):
            with Note(default_x=12.0, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.55, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=47.09, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=75.17, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=103.24, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=131.32, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=159.39, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=215.54, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=187.47, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=75.17, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=131.32, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=187.47, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='38', width=399.06):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=89.15, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=130.16, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=203.89, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=240.76, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=263.81, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=286.85, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=360.59, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=167.03, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=240.76, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=286.85, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=323.72, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=167.03, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=240.76, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=286.85, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=323.72, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
                with Notations():
                    Tied(type='start')
        with Measure(number='39', width=344.23):
            with Note(default_x=17.23, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=52.81, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=123.96, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=159.53, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=185.4, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=211.28, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=17.23, default_y=-115.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=123.96, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=159.53, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=246.85, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=264.02, default_y=-130.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=281.18, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=307.06, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=17.23, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=52.81, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=88.38, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=123.96, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=159.53, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=211.28, default_y=-270.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=246.85, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=307.06, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='40', width=311.7):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=117.32, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=152.11, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=221.7, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=243.45, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=265.19, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.94, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.58, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.94, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=47.73, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=82.53, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=117.32, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=152.11, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=186.91, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=221.7, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='41', width=472.92):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=90.09, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=114.45, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.81, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.57, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=188.34, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=227.31, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=252.08, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=276.44, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=300.8, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=325.16, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=349.52, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=373.88, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=398.24, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=422.6, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=446.96, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=188.34, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=276.44, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=373.88, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=90.09, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=188.34, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=276.44, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=373.88, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='42', width=246.12):
            with Note(default_x=12.0, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.55, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=211.75, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=67.1, default_y=-145.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=94.65, default_y=-140.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=111.87, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=129.09, default_y=-140.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=156.64, default_y=-145.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=184.2, default_y=-150.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=39.55, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=67.1, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=129.09, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=184.2, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=211.75, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='43', width=335.95):
            with Note(default_x=16.16, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=65.71, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=88.24, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.76, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.28, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=155.81, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=178.33, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.85, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=225.62, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=250.38, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=286.42, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=311.19, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-155.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=16.16, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=65.71, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=155.81, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=250.38, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='44', width=422.0):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=89.15, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.15, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.16, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.16, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=181.17, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=204.17, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.17, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=250.18, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=273.18, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=309.99, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=383.6, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=181.17, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=273.18, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=346.79, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='45', width=332.95):
            with Note(default_x=12.0, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=53.01, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=129.79, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=168.18, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=192.18, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=216.17, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=292.95, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=91.4, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=168.18, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=254.56, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='46', width=300.04):
            with Note(default_x=17.23, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=51.32, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=119.49, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=153.58, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.88, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=196.18, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=264.36, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=17.23, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=85.4, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=153.58, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(3)
            with Note(default_x=230.27, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='47', width=554.83):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=89.15, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=119.62, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=150.09, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=198.85, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=230.24, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=260.71, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=309.47, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=339.94, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=370.41, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=400.88, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=431.35, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=461.82, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=492.29, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=522.76, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=198.85, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(3)
            with Note(default_x=309.47, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=431.35, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='48', width=500.16):
            with Note(default_x=15.8, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=47.92, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=80.05, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=124.22, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=144.3, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=165.26, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=197.39, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=241.56, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=273.69, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.81, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=337.94, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=370.06, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=402.19, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=434.31, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=466.43, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=124.22, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=241.56, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=370.06, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='49', width=556.53):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=89.15, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=134.36, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=179.57, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=200.53, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=221.5, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=242.47, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=267.23, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=300.11, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=332.99, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=365.87, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=398.75, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=431.63, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=464.51, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=509.72, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=134.36, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=179.57, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=267.23, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=332.99, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=398.75, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=464.51, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=509.72, default_y=-270.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='50', width=498.47):
            with Note(default_x=15.8, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.76, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=129.43, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=154.2, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=178.96, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=203.73, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=228.49, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.16, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=286.93, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=311.69, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=450.57, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=404.28, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=62.09, default_y=-275.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=129.43, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=311.69, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=357.98, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=404.28, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=450.57, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='51', width=387.49):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=89.15, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=124.47, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=195.1, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=230.41, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=255.18, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=279.94, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=350.57, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=159.78, default_y=-140.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=230.41, default_y=-145.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=315.26, default_y=-150.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=124.47, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=159.78, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=195.1, default_y=-270.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=230.41, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=279.94, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=315.26, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=350.57, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='52', width=364.11):
            with Note(default_x=16.16, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=89.9, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.95, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.99, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.04, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=182.08, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=205.13, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.17, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=252.94, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=277.7, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=314.58, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=339.34, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-155.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=16.16, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=53.03, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=89.9, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=182.08, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=277.7, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='53', width=303.4):
            with Note(default_x=12.94, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.0, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.06, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.12, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=93.18, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.24, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.3, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.36, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=173.41, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=205.51, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=93.18, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=173.41, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=237.61, default_y=-140.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.94, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=93.18, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=173.41, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=205.51, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=237.61, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=269.7, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='54', width=395.96):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=200.73, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=237.61, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=260.66, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=283.71, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=320.6, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=357.48, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=90.09, default_y=-145.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=163.85, default_y=-150.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=237.25, default_y=-155.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=90.09, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=126.97, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=163.85, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=200.73, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=237.61, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=283.71, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=320.6, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=357.48, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='55', width=290.69):
            with Note(default_x=12.0, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=45.59, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=79.17, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=112.76, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=146.35, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=167.34, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=188.33, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=221.92, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=255.51, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=79.17, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=146.35, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=221.92, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='56', width=368.34):
            with Note(default_x=17.23, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=58.35, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=140.59, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=181.71, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=263.95, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=289.64, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=315.34, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=341.04, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=17.23, default_y=-150.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=99.47, default_y=-145.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=181.35, default_y=-140.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=17.23, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=58.35, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=99.47, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=140.59, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=181.71, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=222.83, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=263.95, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=315.34, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='57', width=533.09):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=101.19, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=127.42, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.22, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.03, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=227.26, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=269.22, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=295.45, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=321.68, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=347.9, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=374.13, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=400.36, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=426.58, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=452.81, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=479.04, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=505.27, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=100.83, default_y=-145.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=101.19, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=164.22, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=227.26, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=269.22, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=321.68, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=426.58, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='58', width=242.05):
            with Note(default_x=12.0, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=37.58, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=88.74, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=115.51, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=156.52, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=207.68, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=63.16, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(3)
            with Note(default_x=115.51, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=182.1, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(3)
        with Measure(number='59', width=279.85):
            with Note(default_x=17.23, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.0, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=66.76, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=121.84, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=162.85, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=190.39, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=245.47, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=17.23, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(3)
            with Note(default_x=94.3, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=162.85, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=217.93, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='60', width=523.96):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=104.99, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=134.54, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=164.09, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=258.64, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=305.92, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=337.31, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=366.86, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=414.14, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=443.69, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=475.09, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=104.99, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Note(default_x=211.36, default_y=-270.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=305.92, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=414.14, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(3)
        with Measure(number='61', width=531.03):
            with Note(default_x=12.0, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=45.85, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.69, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=113.54, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=147.39, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=181.23, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.04, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.89, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=285.73, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=319.58, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=353.43, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=407.58, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=441.43, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=475.28, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=147.39, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=285.73, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=407.58, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='62', width=575.51):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=101.19, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=134.2, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.46, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.86, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=220.12, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=247.38, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.78, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=306.04, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=333.31, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=370.79, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=408.28, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=433.05, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=457.81, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=482.58, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=519.38, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=546.65, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=101.19, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Note(default_x=220.12, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=333.31, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=370.79, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=408.28, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=519.38, default_y=-270.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='63', width=241.31):
            with Note(default_x=15.8, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=206.93, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=70.41, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=125.02, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=179.63, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=43.1, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=70.41, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=97.71, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=125.02, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=152.32, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=179.63, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=206.93, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='64', width=238.18):
            with Note(default_x=12.72, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.89, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=47.05, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=74.13, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=101.2, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=128.28, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=155.35, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=182.43, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=209.5, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.36, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.72, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=47.05, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=74.13, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=101.2, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=128.28, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=182.43, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='65', width=354.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=89.15, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=109.11, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=129.06, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=161.0, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=192.93, default_y=-70.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=224.86, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=256.79, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=288.72, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=161.0, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=224.86, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=256.79, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=288.72, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=320.65, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='66', width=285.77):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=107.44, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=138.94, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=201.94, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=221.63, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.31, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=261.0, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.94, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=75.94, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=138.58, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.94, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=44.44, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=75.94, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=107.44, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=138.94, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=170.44, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=201.94, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=241.31, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='67', width=415.04):
            with Note(default_x=12.0, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.73, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.47, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.2, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=114.93, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=156.11, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=181.84, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=207.57, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=233.31, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=259.04, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=284.77, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=310.51, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=336.24, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=361.97, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=387.71, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=63.47, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=114.93, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=156.11, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=207.57, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=310.51, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='68', width=266.48):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=90.09, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=110.9, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=152.51, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=179.29, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=200.1, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=241.72, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=131.71, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=179.29, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=220.91, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=90.09, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=110.9, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=131.71, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=179.29, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=220.91, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='69', width=216.58):
            with Note(default_x=12.0, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=29.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=46.33, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=63.5, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=106.27, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=127.65, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=149.04, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=191.81, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=84.88, default_y=-145.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=127.65, default_y=-140.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=149.04, default_y=-145.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=170.43, default_y=-150.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=84.88, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=127.65, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=170.43, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='70', width=263.78):
            with Note(default_x=19.12, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.29, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=53.45, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=106.3, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=133.07, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=150.24, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=167.4, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=193.83, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=214.79, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=235.76, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-155.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=19.12, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=79.87, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=133.07, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=193.83, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='71', width=308.15):
            with Note(default_x=12.0, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.17, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.93, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.68, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=96.44, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=115.2, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.96, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.72, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=171.48, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=190.24, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=209.0, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=239.02, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=257.78, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=276.54, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=58.93, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=96.44, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=133.96, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=171.48, default_y=-270.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=239.02, default_y=-260.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='72', width=509.09):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=89.15, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=116.67, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.19, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.72, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=199.24, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=226.76, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.28, default_y=-55.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=281.81, default_y=-60.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=309.33, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=353.36, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=397.4, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=424.92, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=452.44, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=479.97, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.15, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=144.19, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=199.24, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=254.28, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=309.33, default_y=-255.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=353.36, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=397.4, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=452.44, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='73', width=375.47):
            with Note(default_x=12.0, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.13, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.26, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.39, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.52, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=152.73, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=192.94, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=258.27, default_y=-50.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=283.41, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=348.74, default_y=-45.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=62.26, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=112.52, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=152.73, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=192.94, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=233.14, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=283.41, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=323.61, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='74', width=170.43):
            with Note(default_x=15.32, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.32, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(32.0)
                Voice('9')
                Type('whole')
                Staff(3)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')