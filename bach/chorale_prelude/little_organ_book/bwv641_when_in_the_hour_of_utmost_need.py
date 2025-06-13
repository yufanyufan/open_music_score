with ScorePartwise(version='3.1'):
    MovementTitle('Höchsten Nöthen, LM')
    with Identification():
        Creator('Genevan French Psalter, 1542', type='composer')
        Rights('Public Domain')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(8.88888)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1336.17)
            PageWidth(945.262)
            with PageMargins(type='even'):
                LeftMargin(45.0001)
                RightMargin(45.0001)
                TopMargin(45.0001)
                BottomMargin(90.0001)
            with PageMargins(type='odd'):
                LeftMargin(45.0001)
                RightMargin(45.0001)
                TopMargin(45.0001)
                BottomMargin(90.0001)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Genevan French Psalter, 1542', default_x=900.262, default_y=1191.17, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Höchsten Nöthen, LM', default_x=472.631, default_y=1291.17, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Public Domain', default_x=472.631, default_y=90.0001, justify='center', valign='bottom', font_size='8')
    with PartList():
        with ScorePart(id='P1'):
            PartName(None)
            with ScoreInstrument(id='P1-I1'):
                InstrumentName(None)
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName(None)
            with ScoreInstrument(id='P2-I1'):
                InstrumentName(None)
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=128.58):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(1)
                    Mode('major')
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=102.27, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=102.27, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='2', width=59.26):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=10.0, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=33.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=33.83, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='3', width=67.24):
            with Note(default_x=13.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=13.8, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.72, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=67.24):
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=13.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.72, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='5', width=59.26):
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=33.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=33.83, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(2.0)
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(1.0)
        with Measure(number='6', width=67.24):
            with Note(default_x=13.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=13.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.72, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='7', width=63.06):
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=13.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.63, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=62.31):
            with Note(default_x=17.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=17.23, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.55, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='9', width=67.24):
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=13.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.72, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=67.24):
            with Note(default_x=13.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=13.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.72, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='11', width=66.11):
            with Note(default_x=21.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=21.03, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.35, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.35, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='12', width=80.48):
            with Note(default_x=13.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=13.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.11, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=49.11, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='13', width=236.28):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=81.21, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=157.95, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=157.95, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(2.0)
            with Note(default_x=81.21, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(1.0)
        with Measure(number='14', width=178.12):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=10.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=93.26, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=93.26, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='15', width=169.25):
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=10.0, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.83, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.83, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=165.07):
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=10.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.74, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.74, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='17', width=106.54):
            with Note(default_x=13.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=13.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=128.58):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(1)
                    Mode('major')
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=102.27, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=102.27, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=59.26):
            with Note(default_x=10.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=10.0, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=33.83, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=33.83, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=67.24):
            with Note(default_x=13.8, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=13.8, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.72, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.72, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=67.24):
            with Note(default_x=13.8, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=13.8, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.72, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.72, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=59.26):
            with Note(default_x=10.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=10.0, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=33.83, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=33.83, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=67.24):
            with Note(default_x=13.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=13.8, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.72, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.72, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=63.06):
            with Note(default_x=13.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=13.8, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.63, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.63, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=62.31):
            with Note(default_x=17.23, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=17.23, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.55, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.55, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='9', width=67.24):
            with Note(default_x=13.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=13.8, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.72, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.72, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=67.24):
            with Note(default_x=13.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=13.8, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.72, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.72, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='11', width=66.11):
            with Note(default_x=21.03, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=21.03, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=41.35, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.35, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=80.48):
            with Note(default_x=13.8, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=13.8, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.11, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.11, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=236.28):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.21, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.21, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=157.95, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=157.95, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='14', width=178.12):
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=10.0, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.4, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(2.0)
            with Forward():
                Duration(1.0)
            with Note(default_x=93.26, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=169.25):
            with Note(default_x=10.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=10.0, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.83, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.83, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=165.07):
            with Note(default_x=10.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=10.0, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.74, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.74, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='17', width=106.54):
            with Note(default_x=13.8, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=13.8, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')