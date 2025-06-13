with ScorePartwise(version='3.1'):
    with Identification():
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-15')
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
    with PartList():
        with ScorePart(id='P1'):
            PartName('Grand Piano')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName(None)
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=275.32):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('8')
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
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('140')
                Staff(1)
                Sound(tempo=140.0)
            with Note(default_x=176.48, default_y=-45.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=176.48, default_y=-20.0, dynamics=94.44):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=219.9, default_y=-25.0, dynamics=104.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=246.81, default_y=-30.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(default_x=219.54, default_y=-50.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=176.48, default_y=-145.0, dynamics=80.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=176.48, default_y=-110.0, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=219.54, default_y=-140.0, dynamics=85.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=219.54, default_y=-115.0, dynamics=76.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
        with Measure(number='2', width=267.75):
            with Note(default_x=10.58, default_y=-10.0, dynamics=125.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=77.74, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=44.52, default_y=-50.0, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=78.1, default_y=-45.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=111.68, default_y=-45.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=111.68, default_y=-20.0, dynamics=103.33):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=144.9, default_y=-40.0, dynamics=93.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=144.9, default_y=-25.0, dynamics=102.22):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=198.99, default_y=-20.0, dynamics=110.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=232.57, default_y=-15.0, dynamics=118.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=10.58, default_y=-135.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=10.58, default_y=-110.0, dynamics=82.22):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=10.58, default_y=-100.0, dynamics=83.33):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=77.74, default_y=-145.0, dynamics=84.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=77.74, default_y=-110.0, dynamics=75.56):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=144.9, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=144.9, default_y=-110.0, dynamics=82.22):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=198.99, default_y=-125.0, dynamics=86.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=198.99, default_y=-115.0, dynamics=76.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=198.99, default_y=-90.0, dynamics=82.22):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=232.57, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=232.57, default_y=-110.0, dynamics=77.78):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=232.57, default_y=-95.0, dynamics=76.67):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=188.97):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=84.91, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=20.55, default_y=-35.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('whole')
                Accidental('sharp')
                Staff(1)
            with Note(default_x=85.27, default_y=-65.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=85.27, default_y=-45.0, dynamics=81.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=114.81, default_y=-65.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=114.81, default_y=-45.0, dynamics=81.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=114.81, default_y=-25.0, dynamics=117.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=142.36, default_y=-45.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=142.36, default_y=-20.0, dynamics=116.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=20.55, default_y=-125.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=20.55, default_y=-105.0, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=20.55, default_y=-90.0, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=85.27, default_y=-135.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=114.81, default_y=-140.0, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=142.36, default_y=-145.0, dynamics=81.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=142.36, default_y=-110.0, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='4', width=235.84):
            with Note(default_x=44.77, default_y=-5.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=44.77, default_y=10.0, dynamics=81.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=44.77, default_y=20.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=97.3, default_y=-10.0, dynamics=72.22):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=97.3, default_y=5.0, dynamics=84.44):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=97.3, default_y=15.0, dynamics=101.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=137.24, default_y=5.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=149.83, default_y=10.0, dynamics=105.56):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=191.86, default_y=-10.0, dynamics=82.22):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=191.86, default_y=0.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=191.86, default_y=25.0, dynamics=120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=71.4, default_y=-105.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=97.66, default_y=-125.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=123.93, default_y=-120.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=149.83, default_y=-115.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=191.86, default_y=-150.0, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(8.0)
            with Note(default_x=44.77, default_y=-130.0, dynamics=91.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('6')
                Type('half')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='5', width=88.61):
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('4')
            with Note(default_x=31.0, default_y=-10.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=31.0, default_y=5.0, dynamics=87.78):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=31.0, default_y=15.0, dynamics=101.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=31.0, default_y=-135.0, dynamics=86.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='6', width=199.33):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note(default_x=138.29, default_y=-25.0, dynamics=104.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=90.38, default_y=-45.0, dynamics=95.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=90.38, default_y=-20.0, dynamics=130.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=138.29, default_y=-50.0, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=168.01, default_y=-50.0, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=168.01, default_y=-30.0, dynamics=102.22):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=90.38, default_y=-145.0, dynamics=84.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=90.38, default_y=-110.0, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=137.93, default_y=-140.0, dynamics=85.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=137.93, default_y=-115.0, dynamics=76.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
        with Measure(number='7', width=270.62):
            with Attributes():
                with Time():
                    Beats('8')
                    BeatType('4')
            with Note(default_x=31.58, default_y=-10.0, dynamics=126.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=93.97, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=63.13, default_y=-50.0, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=94.33, default_y=-45.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=125.52, default_y=-45.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=125.52, default_y=-20.0, dynamics=98.89):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=156.36, default_y=-40.0, dynamics=90.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=156.36, default_y=-25.0, dynamics=96.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=206.63, default_y=-20.0, dynamics=114.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=237.83, default_y=-15.0, dynamics=116.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=31.58, default_y=-135.0, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=31.58, default_y=-110.0, dynamics=83.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=31.58, default_y=-100.0, dynamics=85.56):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=93.97, default_y=-145.0, dynamics=81.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=93.97, default_y=-110.0, dynamics=81.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=156.36, default_y=-130.0, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=156.36, default_y=-110.0, dynamics=81.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=206.63, default_y=-125.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=206.63, default_y=-115.0, dynamics=76.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=206.63, default_y=-90.0, dynamics=83.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=237.83, default_y=-120.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=237.83, default_y=-110.0, dynamics=86.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=237.83, default_y=-95.0, dynamics=78.89):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='8', width=170.85):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=76.6, default_y=-30.0, dynamics=110.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=20.55, default_y=-35.0, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('whole')
                Accidental('sharp')
                Staff(1)
            with Note(default_x=76.96, default_y=-65.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=76.96, default_y=-45.0, dynamics=84.44):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=106.51, default_y=-65.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=106.51, default_y=-45.0, dynamics=84.44):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=106.51, default_y=-25.0, dynamics=116.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=130.28, default_y=-45.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=130.28, default_y=-20.0, dynamics=112.22):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=20.55, default_y=-125.0, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=20.55, default_y=-105.0, dynamics=83.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=20.55, default_y=-90.0, dynamics=87.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=76.96, default_y=-135.0, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=106.51, default_y=-140.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=130.28, default_y=-145.0, dynamics=84.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=130.28, default_y=-110.0, dynamics=76.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='9', width=217.71):
            with Note(default_x=44.77, default_y=-5.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=44.77, default_y=10.0, dynamics=83.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=44.77, default_y=20.0, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=92.27, default_y=-10.0, dynamics=72.22):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=92.27, default_y=5.0, dynamics=85.56):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=92.27, default_y=15.0, dynamics=101.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=127.17, default_y=5.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=139.76, default_y=10.0, dynamics=104.44):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=177.76, default_y=-10.0, dynamics=85.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=177.76, default_y=0.0, dynamics=85.56):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=177.76, default_y=25.0, dynamics=118.89):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=68.88, default_y=-105.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=92.63, default_y=-125.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=116.38, default_y=-120.0, dynamics=85.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=139.76, default_y=-115.0, dynamics=82.22):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=177.76, default_y=-150.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(8.0)
            with Note(default_x=44.77, default_y=-130.0, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('6')
                Type('half')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='10', width=75.57):
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('4')
            with Note(default_x=31.0, default_y=15.0, dynamics=105.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=31.0, default_y=-135.0, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=31.0, default_y=-115.0, dynamics=77.78):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=31.0, default_y=-100.0, dynamics=84.44):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='11', width=122.41):
            with Note(default_x=43.2, default_y=-10.0, dynamics=135.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=71.3, default_y=-35.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=43.2, default_y=-135.0, dynamics=87.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=43.2, default_y=-115.0, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=43.2, default_y=-100.0, dynamics=86.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=71.3, default_y=-125.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=71.3, default_y=-115.0, dynamics=73.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=71.3, default_y=-100.0, dynamics=85.56):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=356.71):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('8')
                    BeatType('4')
            with Note(default_x=124.03, default_y=-65.0, dynamics=82.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=124.03, default_y=-50.0, dynamics=94.44):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=124.03, default_y=-40.0, dynamics=94.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=188.12, default_y=-70.0, dynamics=78.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=188.12, default_y=-50.0, dynamics=82.22):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=188.12, default_y=-35.0, dynamics=112.22):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=239.39, default_y=-45.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=239.39, default_y=-20.0, dynamics=123.33):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=291.03, default_y=-25.0, dynamics=105.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=323.07, default_y=-30.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=124.4, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=156.44, default_y=-135.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=188.12, default_y=-140.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=239.39, default_y=-145.0, dynamics=81.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=239.39, default_y=-115.0, dynamics=81.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=290.66, default_y=-130.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=290.66, default_y=-120.0, dynamics=76.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=290.66, default_y=-95.0, dynamics=77.78):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=203.28):
            with Note(default_x=13.8, default_y=-50.0, dynamics=92.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=13.8, default_y=-25.0, dynamics=120.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=86.76, default_y=-25.0, dynamics=108.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=138.04, default_y=-20.0, dynamics=114.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=169.86, default_y=-15.0, dynamics=113.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=13.8, default_y=-150.0, dynamics=77.78):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=13.8, default_y=-115.0, dynamics=81.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=86.76, default_y=-115.0, dynamics=78.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=86.76, default_y=-95.0, dynamics=82.22):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=137.68, default_y=-120.0, dynamics=82.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=137.68, default_y=-110.0, dynamics=84.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=137.68, default_y=-95.0, dynamics=81.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=379.83):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note(default_x=108.31, default_y=-45.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=108.31, default_y=-10.0, dynamics=125.56):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1.0)
            with Attributes():
                with Clef(number=1):
                    Sign('F')
                    Line(4)
            with Forward():
                Duration(1.0)
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=21.39, default_y=-60.0, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=21.39, default_y=-45.0, dynamics=87.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=21.39, default_y=-35.0, dynamics=94.44):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=162.13, default_y=-25.0, dynamics=84.44):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=221.42, default_y=-20.0, dynamics=95.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=291.32, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=334.77, default_y=-30.0, dynamics=102.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=21.75, default_y=-125.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=65.21, default_y=-130.0, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=108.31, default_y=-135.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=108.31, default_y=-110.0, dynamics=76.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=221.42, default_y=-125.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=221.42, default_y=-110.0, dynamics=74.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=221.42, default_y=-90.0, dynamics=82.22):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=291.32, default_y=-95.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=334.77, default_y=-100.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('6')
                Type('whole')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('6')
                Type('half')
                Staff(2)
            with Note(default_x=290.95, default_y=-125.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=290.95, default_y=-115.0, dynamics=82.22):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=116.67):
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('4')
            with Note(default_x=34.8, default_y=-65.0, dynamics=82.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=34.8, default_y=-55.0, dynamics=83.33):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=34.8, default_y=-30.0, dynamics=104.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=34.8, default_y=-145.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')