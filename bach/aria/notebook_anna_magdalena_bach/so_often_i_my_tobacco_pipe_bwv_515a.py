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
        CreditWords('Aria', default_x=595.275, default_y=1627.09, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('\n', default_x=1133.86, default_y=1527.94, justify='right', valign='bottom', font_size='12')
        CreditWords('Johann Sebastian Bach \n')
        CreditWords('BWV 515 Anna Magdalena Bach')
    with Credit(page=2):
        CreditType('composer')
        CreditWords('\n', default_x=1133.86, default_y=1527.94, justify='right', valign='bottom', font_size='12')
        CreditWords('Johann Sebastian Bach \n')
        CreditWords('BWV 515 Anna Magdalena Bach')
    with Credit(page=2):
        CreditType('title')
        CreditWords('Aria', default_x=595.275, default_y=1627.09, justify='center', valign='top', font_size='24')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('brace')
        with ScorePart(id='P1'):
            PartName('Piano', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Piano', print_object='no')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=318.46):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=99.83, default_y=-45.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=172.17, default_y=-45.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=244.52, default_y=-45.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
        with Measure(number='2', width=257.91):
            with Note(default_x=12.0, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=128.05, default_y=-25.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=158.59, default_y=-20.0, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=189.13, default_y=-25.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='3', width=239.9):
            with Note(default_x=12.0, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.63, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=125.15, default_y=-40.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=168.67, default_y=-25.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('5')
        with Measure(number='4', width=239.9):
            with Note(default_x=12.0, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.63, default_y=-40.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=125.15, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=168.67, default_y=-45.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='5', width=313.6):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(139.09)
            with Note(default_x=82.58, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=159.05, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=235.53, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
        with Measure(number='6', width=274.68):
            with Note(default_x=12.0, default_y=-25.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=136.01, default_y=-20.0, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.65, default_y=-15.0, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=201.29, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='7', width=239.07):
            with Note(default_x=12.0, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=86.79, default_y=-40.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='8', width=228.81):
            with Note(default_x=12.0, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=313.69):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(139.09)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=106.14, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=174.79, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=243.44, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
        with Measure(number='10', width=221.55):
            with Note(default_x=13.64, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=151.3, default_y=-40.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='11', width=256.3):
            with Note(default_x=12.72, default_y=-25.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=81.86, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=125.07, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=168.28, default_y=-40.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=211.49, default_y=-45.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='12', width=264.61):
            with Note(default_x=20.67, default_y=-50.0, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
        with Measure(number='13', width=354.95):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(139.09)
            with Note(default_x=90.82, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=178.33, default_y=-50.0, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=265.84, default_y=-40.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
        with Measure(number='14', width=245.47):
            with Note(default_x=12.0, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=122.14, default_y=-25.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=151.12, default_y=-20.0, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.11, default_y=-25.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='15', width=230.17):
            with Note(default_x=12.0, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=84.19, default_y=-45.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=156.38, default_y=-50.0, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
        with Measure(number='16', width=225.57):
            with Note(default_x=12.0, default_y=-45.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=302.66):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    TopSystemDistance(170.0)
            with Note(default_x=78.78, default_y=-45.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=152.87, default_y=-45.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=226.97, default_y=-45.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
        with Measure(number='18', width=263.18):
            with Note(default_x=12.0, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=130.55, default_y=-25.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=161.75, default_y=-20.0, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=192.94, default_y=-25.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='19', width=245.16):
            with Note(default_x=12.0, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.25, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=127.78, default_y=-40.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=172.31, default_y=-25.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('5')
        with Measure(number='20', width=245.16):
            with Note(default_x=12.0, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.25, default_y=-40.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=127.78, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=172.31, default_y=-45.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='21', width=313.6):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(139.7)
            with Note(default_x=82.58, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=159.05, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=235.53, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
        with Measure(number='22', width=274.68):
            with Note(default_x=12.0, default_y=-25.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=136.01, default_y=-20.0, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.65, default_y=-15.0, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=201.29, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='23', width=239.07):
            with Note(default_x=12.0, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=86.79, default_y=-40.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='24', width=228.81):
            with Note(default_x=12.0, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=313.69):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(139.7)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=106.14, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=174.79, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=243.44, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
        with Measure(number='26', width=221.55):
            with Note(default_x=13.64, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=151.3, default_y=-40.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='27', width=256.3):
            with Note(default_x=12.72, default_y=-25.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=81.86, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=125.07, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=168.28, default_y=-40.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=211.49, default_y=-45.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='28', width=264.61):
            with Note(default_x=20.67, default_y=-50.0, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
        with Measure(number='29', width=354.95):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(139.7)
            with Note(default_x=90.82, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=178.33, default_y=-50.0, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=265.84, default_y=-40.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
        with Measure(number='30', width=245.47):
            with Note(default_x=12.0, default_y=-30.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=122.14, default_y=-25.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=151.12, default_y=-20.0, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.11, default_y=-25.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='31', width=230.17):
            with Note(default_x=12.0, default_y=-35.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=84.19, default_y=-45.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=156.38, default_y=-50.0, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
        with Measure(number='32', width=225.57):
            with Note(default_x=12.0, default_y=-45.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P2'):
        with Measure(number='1', width=318.46):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(71.04)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=99.83, default_y=-131.04, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=172.17, default_y=-96.04):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=244.52, default_y=-101.04, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=257.91):
            with Note(default_x=12.0, default_y=-106.04, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=79.19, default_y=-126.04, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=189.13, default_y=-121.04, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3')
        with Measure(number='3', width=239.9):
            with Note(default_x=12.0, default_y=-116.04, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.63, default_y=-111.04, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=168.67, default_y=-146.04, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=239.9):
            with Note(default_x=12.0, default_y=-131.04, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=81.63, default_y=-146.04, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=168.67, default_y=-156.04, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
        with Measure(number='5', width=313.6):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.85)
            with Note(default_x=82.58, default_y=-166.85, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=159.05, default_y=-131.85, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=235.53, default_y=-141.85, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
        with Measure(number='6', width=274.68):
            with Note(default_x=12.0, default_y=-121.85, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=83.8, default_y=-136.85, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=201.29, default_y=-131.85, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
        with Measure(number='7', width=239.07):
            with Note(default_x=12.0, default_y=-141.85, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=87.16, default_y=-136.85, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=162.31, default_y=-171.85, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=228.81):
            with Note(default_x=12.0, default_y=-156.85, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=313.69):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=106.14, default_y=-95.0, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=174.79, default_y=-120.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=243.44, default_y=-110.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3')
        with Measure(number='10', width=221.55):
            with Note(default_x=14.0, default_y=-100.0, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=82.65, default_y=-110.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=151.3, default_y=-95.0, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='11', width=256.3):
            with Note(default_x=12.36, default_y=-115.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=168.28, default_y=-110.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=264.61):
            with Note(default_x=21.03, default_y=-105.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=90.17, default_y=-110.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=133.38, default_y=-115.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=176.59, default_y=-120.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=219.8, default_y=-125.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=354.95):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.25)
            with Direction(placement='below'):
                with DirectionType():
                    Words('1. Sooft ich meine Tabakspfeife,\n', default_y=-40.0, relative_x=-80.91, relative_y=-35.38)
                    Words('Mit gutem Knaster angefüllt,\n')
                    Words('Zur Lust und Zeitvertreib ergreife,\n')
                    Words('So gibt sie mir ein Trauerbild -\n')
                    Words('Und füget diese Lehre bei,\n')
                    Words('Dass ich derselben ähnlich sei. \n')
                    Words('\n')
                    Words('2. Die Pfeife stammt von Ton und Erde,\n')
                    Words('Auch ich bin gleichfalls draus gemacht.\n')
                    Words('Auch ich muss einst zur Erde werden -\n')
                    Words("Sie fällt und bricht, eh ihr's gedacht,\n")
                    Words('Mir oftmals in der Hand entzwei,\n')
                    Words('Mein Schicksal ist auch einerlei.')
            with Note(default_x=90.82, default_y=-135.25, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=134.57, default_y=-140.25, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=178.33, default_y=-145.25, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=222.09, default_y=-140.25, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=265.84, default_y=-135.25, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=309.6, default_y=-130.25, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='14', width=245.47):
            with Direction(placement='below'):
                with DirectionType():
                    Words('3. Die Pfeife pflegt man nicht zu färben,\n', default_y=-40.0, relative_x=-4.5, relative_y=-35.38)
                    Words('Sie bleibet weiß. Also der Schluss,\n')
                    Words('Dass ich auch dermaleinst im Sterben\n')
                    Words('Dem Leibe nach erblassen muss.\n')
                    Words('Im Grabe wird der Körper auch\n')
                    Words('So schwarz wie sie nach langem Brauch.\n')
                    Words('\n')
                    Words('4. Wenn nun die Pfeife angezündet,\n')
                    Words('So sieht man, wie im Augenblick\n')
                    Words('Der Rauch in freier Luft verschwindet,\n')
                    Words('Nichts als die Asche bleibt zurück.\n')
                    Words('So wird des Menschen Ruhm verzehrt\n')
                    Words('Und dessen Leib in Staub verkehrt.')
            with Note(default_x=12.0, default_y=-125.25, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=75.76, default_y=-130.25, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=180.11, default_y=-135.25, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
        with Measure(number='15', width=230.17):
            with Note(default_x=12.0, default_y=-130.25, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Direction(placement='below'):
                with DirectionType():
                    Words("5. Wie oft geschieht's nicht bei dem Rauchen,\n", default_y=-40.0, relative_x=23.97, relative_y=-39.87)
                    Words('Dass, wenn der Stopfer nicht zur Hand,\n')
                    Words('Man pflegt den Finger zu gebrauchen.\n')
                    Words('Dann denk ich, wenn ich mich verbrannt:\n')
                    Words('O, macht die Kohle solche Pein,\n')
                    Words('Wie heiß mag erst die Hölle sein? \n')
                    Words('\n')
                    Words('6. Ich kann bei so gestalten Sachen\n')
                    Words('Mir bei dem Toback jederzeit\n')
                    Words('Erbauliche Gedanken machen.\n')
                    Words('Drum schmauch ich voll Zufriedenheit\n')
                    Words('Zu Land, zu Wasser und zu Haus\n')
                    Words('Mein Pfeifchen stets in Andacht aus.')
            with Note(default_x=84.19, default_y=-120.25, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=156.38, default_y=-110.25, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2')
        with Measure(number='16', width=225.57):
            with Note(default_x=12.36, default_y=-130.25, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=77.64, default_y=-145.25, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.92, default_y=-165.25, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=302.66):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.04)
            with Note(default_x=78.78, default_y=-131.04, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=152.87, default_y=-96.04):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=226.97, default_y=-101.04, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=263.18):
            with Note(default_x=12.0, default_y=-106.04, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=80.63, default_y=-126.04, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=192.94, default_y=-121.04, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3')
        with Measure(number='19', width=245.16):
            with Note(default_x=12.0, default_y=-116.04, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.25, default_y=-111.04, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=172.31, default_y=-146.04, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=245.16):
            with Note(default_x=12.0, default_y=-131.04, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=83.25, default_y=-146.04, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=172.31, default_y=-156.04, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
        with Measure(number='21', width=313.6):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.85)
            with Note(default_x=82.58, default_y=-166.85, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=159.05, default_y=-131.85, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=235.53, default_y=-141.85, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
        with Measure(number='22', width=274.68):
            with Note(default_x=12.0, default_y=-121.85, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=83.8, default_y=-136.85, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=201.29, default_y=-131.85, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
        with Measure(number='23', width=239.07):
            with Note(default_x=12.0, default_y=-141.85, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=87.16, default_y=-136.85, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=162.31, default_y=-171.85, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=228.81):
            with Note(default_x=12.0, default_y=-156.85, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=313.69):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=106.14, default_y=-95.0, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=174.79, default_y=-120.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=243.44, default_y=-110.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3')
        with Measure(number='26', width=221.55):
            with Note(default_x=14.0, default_y=-100.0, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=82.65, default_y=-110.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=151.3, default_y=-95.0, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='27', width=256.3):
            with Note(default_x=12.36, default_y=-115.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=168.28, default_y=-110.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='28', width=264.61):
            with Note(default_x=21.03, default_y=-105.0, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=90.17, default_y=-110.0, dynamics=138.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=133.38, default_y=-115.0, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=176.59, default_y=-120.0, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=219.8, default_y=-125.0, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='29', width=354.95):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(68.94)
            with Direction(placement='below'):
                with DirectionType():
                    Words('Kdykoli sáhnu pro dýmčičku\n', default_y=-40.0, relative_x=-80.91, relative_y=-35.38)
                    Words('tabákem pěkně nacpanou\n')
                    Words('a zadýmám si na chviličku,\n')
                    Words('chmurné mi věci vytanou\n')
                    Words('a napadá mi, jak já sám\n')
                    Words('se té své dýmce podobám:\n')
                    Words('\n')
                    Words('Co že je dýmka? Pouhá hlína!\n')
                    Words('A co je člověk? Hlína též!\n')
                    Words('A častokrát mi připomíná,\n')
                    Words('když se tak - než se naděješ -\n')
                    Words('při pádu na zem rozbíjí,\n')
                    Words('jak ten náš život pomíjí.')
            with Note(default_x=90.82, default_y=-133.94, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=134.57, default_y=-138.94, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=178.33, default_y=-143.94, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=222.09, default_y=-138.94, dynamics=138.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=265.84, default_y=-133.94, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=309.6, default_y=-128.94, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='30', width=245.47):
            with Direction(placement='below'):
                with DirectionType():
                    Words('Jindy po dýmky zapálení\n', default_y=-40.0, relative_x=61.43, relative_y=-35.38)
                    Words('spatřím jak v krátku, ve chvíli,\n')
                    Words('tabák se v pouhý popel změní,\n')
                    Words('dým v povětří se rozptýlí.\n')
                    Words('Tak také lidská sláva, ach,\n')
                    Words('zajde – a z těla zbude prach.\n')
                    Words('\n')
                    Words('Když, jak při kouření se stává,\n')
                    Words('ťapťátko nelze nalézti,\n')
                    Words('dusá se palcem dýmka žhavá.\n')
                    Words('Tu myslím při té bolesti:\n')
                    Words('malý-li uhlík takto žhne,\n')
                    Words('jak je ve výhni pekelné?')
            with Note(default_x=12.0, default_y=-123.94, dynamics=138.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=75.76, default_y=-128.94, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=180.11, default_y=-133.94, dynamics=138.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
        with Measure(number='31', width=230.17):
            with Note(default_x=12.0, default_y=-128.94, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Direction(placement='below'):
                with DirectionType():
                    Words('A tak mi dýmka napomáhá\n', default_y=-51.72, relative_x=80.91, relative_y=-27.88)
                    Words('k myšlenkám zbožným, plným krás,\n')
                    Words('a proto též je mi tak drahá\n')
                    Words('a proto též si v každý čas,\n')
                    Words('ať jsem, kde jsem, zde nebo tam,\n')
                    Words('s chutí a zbožně zadýmám.')
            with Note(default_x=84.19, default_y=-118.94, dynamics=138.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=156.38, default_y=-108.94, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2')
        with Measure(number='32', width=225.57):
            with Note(default_x=12.36, default_y=-128.94, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=77.64, default_y=-143.94, dynamics=138.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.92, default_y=-163.94, dynamics=138.89):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')