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
    with PartList():
        with ScorePart(id='P1'):
            PartName('Bright Piano')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName(None)
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(2)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Bright Piano')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName(None)
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(2)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=205.07):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(151.4)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('100')
                Sound(tempo=100.0)
            with Note(default_x=178.14, default_y=-45.0, dynamics=70.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=178.14, default_y=-35.0, dynamics=93.33):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='2', width=135.36):
            with Note(default_x=10.0, default_y=-35.0, dynamics=96.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=10.0, default_y=-20.0, dynamics=121.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=40.94, default_y=-35.0, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=40.94, default_y=-15.0, dynamics=116.67):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.88, default_y=-35.0, dynamics=83.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.88, default_y=-10.0, dynamics=117.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=102.82, default_y=-35.0, dynamics=85.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=102.82, default_y=-20.0, dynamics=101.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='3', width=172.57):
            with Note(default_x=10.0, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=70.83, default_y=-30.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=96.1, default_y=-45.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=96.1, default_y=-35.0, dynamics=102.22):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=133.53, default_y=-60.0, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=133.53, default_y=-25.0, dynamics=115.56):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=10.0, default_y=-40.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.43, default_y=-50.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('half')
        with Measure(number='4', width=180.47):
            with Note(default_x=13.8, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=13.8, default_y=-45.0, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=72.11, default_y=-50.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=97.39, default_y=-55.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=97.39, default_y=-45.0, dynamics=113.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=133.28, default_y=-40.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='5', width=149.03):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=34.8, default_y=-50.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=34.8, default_y=-35.0, dynamics=117.78):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=110.0, default_y=-50.0, dynamics=82.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=110.0, default_y=-35.0, dynamics=110.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=83.6):
            with Attributes():
                with Time():
                    Beats('1')
                    BeatType('4')
            with Note(default_x=31.0, default_y=-45.0, dynamics=91.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=31.0, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='7', width=220.39):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('4')
            with Note(default_x=112.27, default_y=-35.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.27, default_y=-20.0, dynamics=123.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.17, default_y=-35.0, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.17, default_y=-15.0, dynamics=120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=167.71, default_y=-35.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=167.71, default_y=-10.0, dynamics=114.44):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=193.25, default_y=-35.0, dynamics=83.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=193.25, default_y=-20.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=155.33):
            with Note(default_x=10.0, default_y=-25.0, dynamics=104.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=63.1, default_y=-30.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=88.38, default_y=-45.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.38, default_y=-35.0, dynamics=101.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=121.05, default_y=-60.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=121.05, default_y=-25.0, dynamics=114.44):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=10.0, default_y=-40.0, dynamics=81.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.68, default_y=-50.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('half')
        with Measure(number='9', width=163.23):
            with Note(default_x=13.8, default_y=-55.0, dynamics=86.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=13.8, default_y=-45.0, dynamics=96.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=63.28, default_y=-50.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=88.55, default_y=-55.0, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.55, default_y=-45.0, dynamics=115.56):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=119.0, default_y=-40.0, dynamics=113.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='10', width=136.1):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=34.8, default_y=-50.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=34.8, default_y=-35.0, dynamics=116.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=101.39, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=101.39, default_y=-35.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='11', width=74.68):
            with Attributes():
                with Time():
                    Beats('1')
                    BeatType('4')
            with Note(default_x=31.0, default_y=-45.0, dynamics=86.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=31.0, default_y=-25.0, dynamics=116.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='12', width=131.16):
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('4')
            with Note(default_x=31.0, default_y=-35.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=31.0, default_y=-10.0, dynamics=124.44):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.64, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=80.28, default_y=-30.0, dynamics=81.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=80.28, default_y=-20.0, dynamics=114.44):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=104.92, default_y=-45.0, dynamics=66.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=104.92, default_y=-25.0, dynamics=97.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='13', width=175.6):
            with Note(default_x=10.0, default_y=-30.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=63.69, default_y=-25.0, dynamics=115.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=88.97, default_y=-45.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.97, default_y=-35.0, dynamics=101.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=122.01, default_y=-25.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=150.83, default_y=-40.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=150.83, default_y=-25.0, dynamics=117.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(8.0)
            with Note(default_x=10.0, default_y=-45.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=43.04, default_y=-50.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=122.01, default_y=-35.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='14', width=297.39):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=91.21, default_y=-45.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=91.21, default_y=-10.0, dynamics=125.56):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.36, default_y=-45.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.36, default_y=-25.0, dynamics=95.56):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=193.5, default_y=-45.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=193.5, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=244.64, default_y=-50.0, dynamics=76.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=244.64, default_y=-25.0, dynamics=102.22):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='15', width=232.22):
            with Note(default_x=10.58, default_y=-30.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Backup():
                Duration(8.0)
            with Note(default_x=10.94, default_y=-45.0, dynamics=86.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=94.93, default_y=-25.0, dynamics=115.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=127.24, default_y=-45.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=127.24, default_y=-35.0, dynamics=97.78):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=178.93, default_y=-45.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=178.93, default_y=-35.0, dynamics=112.22):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('3')
                Type('quarter')
            with Note(default_x=62.63, default_y=-40.0, dynamics=91.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('3')
                Type('half')
        with Measure(number='16', width=323.35):
            with Note(default_x=17.23, default_y=-40.0, dynamics=93.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=17.23, default_y=-30.0, dynamics=110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=95.64, default_y=-40.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=95.64, default_y=-25.0, dynamics=112.22):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=160.24, default_y=-20.0, dynamics=114.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=200.62, default_y=-10.0, dynamics=121.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=241.0, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=281.38, default_y=-20.0, dynamics=104.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('half')
            with Note(default_x=160.24, default_y=-35.0, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=241.0, default_y=-30.0, dynamics=90.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
        with Measure(number='17', width=203.54):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=43.04, default_y=-35.0, dynamics=81.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=43.04, default_y=-25.0, dynamics=101.11):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=143.09, default_y=-35.0, dynamics=81.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=143.09, default_y=-20.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=205.07):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                Staves(2)
                with Clef(number=1):
                    Sign('F')
                    Line(4)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=178.14, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=178.14, default_y=-240.0, dynamics=78.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='2', width=135.36):
            with Note(default_x=10.0, default_y=-100.0, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=40.94, default_y=-105.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=71.88, default_y=-100.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=102.82, default_y=-100.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=10.0, default_y=-230.0, dynamics=86.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=40.94, default_y=-220.0, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=71.88, default_y=-240.0, dynamics=76.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=102.82, default_y=-230.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=172.57):
            with Note(default_x=10.0, default_y=-120.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=47.43, default_y=-105.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=96.1, default_y=-105.0, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=133.53, default_y=-120.0, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=10.0, default_y=-235.0, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=47.43, default_y=-245.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=96.1, default_y=-230.0, dynamics=86.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=133.53, default_y=-235.0, dynamics=84.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='4', width=180.47):
            with Note(default_x=13.8, default_y=-115.0, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=72.11, default_y=-140.0, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=97.39, default_y=-100.0, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=133.28, default_y=-95.0, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=155.7, default_y=-100.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=49.69, default_y=-115.0, dynamics=81.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=13.44, default_y=-240.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=97.39, default_y=-250.0, dynamics=81.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=133.28, default_y=-215.0, dynamics=90.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=149.03):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=35.16, default_y=-100.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=72.58, default_y=-110.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=110.0, default_y=-105.0, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=34.8, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=110.0, default_y=-220.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='6', width=83.6):
            with Attributes():
                with Time():
                    Beats('1')
                    BeatType('4')
            with Note(default_x=31.0, default_y=-100.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=31.0, default_y=-240.0, dynamics=78.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='7', width=220.39):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('4')
            with Note(default_x=112.27, default_y=-100.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=142.17, default_y=-105.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=167.71, default_y=-100.0, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=193.25, default_y=-100.0, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=112.27, default_y=-230.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=142.17, default_y=-220.0, dynamics=95.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=167.71, default_y=-240.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=193.25, default_y=-230.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='8', width=155.33):
            with Note(default_x=10.0, default_y=-120.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=42.68, default_y=-105.0, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=88.38, default_y=-105.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=121.05, default_y=-120.0, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=10.0, default_y=-235.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=42.68, default_y=-245.0, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=88.38, default_y=-230.0, dynamics=91.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=121.05, default_y=-235.0, dynamics=84.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='9', width=163.23):
            with Note(default_x=13.8, default_y=-115.0, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=63.28, default_y=-140.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=88.55, default_y=-100.0, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=119.0, default_y=-95.0, dynamics=82.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=138.47, default_y=-100.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=44.25, default_y=-115.0, dynamics=77.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=13.44, default_y=-240.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=88.55, default_y=-250.0, dynamics=83.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=119.0, default_y=-215.0, dynamics=96.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=136.1):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=35.16, default_y=-100.0, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=68.27, default_y=-110.0, dynamics=76.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=101.39, default_y=-105.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=34.8, default_y=-220.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=101.39, default_y=-220.0, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=74.68):
            with Attributes():
                with Time():
                    Beats('1')
                    BeatType('4')
            with Note(default_x=31.0, default_y=-105.0, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=31.0, default_y=-220.0, dynamics=81.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=49.92, default_y=-225.0, dynamics=85.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='12', width=131.16):
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('4')
            with Note(default_x=31.0, default_y=-105.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=55.64, default_y=-90.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=80.28, default_y=-90.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=104.92, default_y=-105.0, dynamics=67.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=31.0, default_y=-230.0, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=55.64, default_y=-220.0, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=80.28, default_y=-215.0, dynamics=87.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=104.92, default_y=-220.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=175.6):
            with Note(default_x=10.0, default_y=-100.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=43.04, default_y=-105.0, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=88.97, default_y=-105.0, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=122.01, default_y=-105.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=10.0, default_y=-225.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=43.04, default_y=-245.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=88.97, default_y=-230.0, dynamics=86.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=122.01, default_y=-230.0, dynamics=91.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=150.83, default_y=-235.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='14', width=297.39):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=91.21, default_y=-100.0, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=142.36, default_y=-115.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=193.5, default_y=-110.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=244.64, default_y=-120.0, dynamics=74.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=91.21, default_y=-240.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=142.36, default_y=-230.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=193.5, default_y=-250.0, dynamics=78.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=244.64, default_y=-245.0, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='15', width=232.22):
            with Note(default_x=10.94, default_y=-100.0, dynamics=87.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=62.63, default_y=-105.0, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=127.24, default_y=-105.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=178.93, default_y=-100.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=10.94, default_y=-240.0, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=62.63, default_y=-235.0, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=127.24, default_y=-230.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=178.93, default_y=-240.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='16', width=323.35):
            with Note(default_x=17.23, default_y=-100.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Note(default_x=95.64, default_y=-155.0, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=160.24, default_y=-160.0, dynamics=76.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=241.0, default_y=-145.0, dynamics=91.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=281.38, default_y=-150.0, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=17.23, default_y=-225.0, dynamics=85.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=95.64, default_y=-235.0, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=160.24, default_y=-230.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=241.0, default_y=-225.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=203.54):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=43.04, default_y=-155.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=143.09, default_y=-150.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=43.4, default_y=-220.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=93.25, default_y=-255.0, dynamics=73.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=143.09, default_y=-240.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')