with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Bach, Violin Sonata #2, Andante, BWV1003')
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
        CreditWords('Bach, Violin Sonata #2, Andante, BWV1003', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J. S. Bach', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Violin')
            PartAbbreviation('Vln.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Violin')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(41)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=360.8):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(71.6)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(48.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Slow', default_x=-31.8, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='12')
                Sound(tempo=60.0)
            with Note(default_x=72.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=197.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=239.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=265.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=292.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=333.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=72.06, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=113.97, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=155.89, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=197.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=239.71, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=303.97, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=301.48):
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.1, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=68.41, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=110.49, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=152.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=194.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=220.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=247.28, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.58, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=68.41, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=110.49, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=152.58, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=194.67, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=247.28, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='3', width=343.61):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=96.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=127.3, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=149.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=234.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=261.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=288.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=315.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.4, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=123.0, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=123.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=176.61, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=234.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=288.41, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=355.33):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(50.8)
                        RightMargin(0.0)
                    SystemDistance(112.9)
            with Note(default_x=59.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=111.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=195.84, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=222.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=248.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=274.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=301.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=327.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=59.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=59.0, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=111.63, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=153.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=195.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=248.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=301.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='5', width=311.39):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=144.35, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=171.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=199.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=227.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=23.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=100.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=144.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=199.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=254.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='6', width=359.97):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.73, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=98.59, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=131.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=156.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=242.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=271.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=300.64, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=329.51, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.73, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=127.46, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=127.46, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=185.19, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=242.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=300.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=366.97):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(50.8)
                        RightMargin(0.0)
                    SystemDistance(112.9)
            with Note(default_x=59.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=81.05, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.74, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=158.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=184.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.14, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=261.98, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=287.83, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=313.68, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=339.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=55.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.2, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=106.9, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=158.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=210.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=261.98, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=261.98, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=261.98, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=313.68, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=313.68, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=313.68, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='8', width=325.45):
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=15.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=15.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('16th')
            with Note(default_x=119.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=147.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=174.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=202.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=230.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=261.6, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=278.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=296.18, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.84, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=91.88, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=147.21, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=147.21, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=202.54, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=202.54, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=261.6, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='9', width=334.27):
            with Note(default_x=17.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=46.57, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.92, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.26, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=134.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=152.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=171.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=189.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=207.96, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=226.3, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=244.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=262.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=281.32, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=281.32, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=281.32, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(144.0)
            with Note(default_x=17.23, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(96.0)
                Voice('2')
                Type('half')
        with Measure(number='10', width=394.09):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(50.8)
                        RightMargin(0.0)
                    SystemDistance(116.53)
            with Note(default_x=59.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=86.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=106.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=126.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=146.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=166.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=193.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=228.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=248.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('begin', number=4)
            with Note(default_x=265.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('end', number=4)
            with Note(default_x=282.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=302.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=322.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=357.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Backup():
                Duration(144.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(48.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=193.26, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(96.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='11', width=297.17):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=29.8)
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
            with Note(default_x=114.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.39, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=184.88, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=208.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=231.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.37, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=90.94, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=137.91, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=184.88, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=231.84, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='discontinue')
                Repeat(direction='backward')
        with Measure(number='12', width=102.93):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=40.64)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(144.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(144.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='13', width=232.49):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=111.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=145.26, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=166.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=45.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=78.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=111.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=145.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=186.91, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue')
        with Measure(number='14', width=371.18):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(50.8)
                        RightMargin(0.0)
                    SystemDistance(112.9)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=87.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=139.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=181.46, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=223.27, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=265.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=291.2, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=343.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=87.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=139.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=181.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=223.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=223.27, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=265.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=265.07, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=317.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=295.77):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=64.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=106.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=147.86, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=189.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=215.79, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=268.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=64.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=106.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=147.86, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=189.66, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=241.92, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='16', width=359.74):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=48.81, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=80.2, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=176.88, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.09, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=237.3, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=267.51, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.72, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=327.93, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=80.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.2, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=128.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=176.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=237.3, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=297.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='17', width=358.38):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(50.8)
                        RightMargin(0.0)
                    SystemDistance(112.9)
            with Note(default_x=59.0, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=140.73, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=166.27, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.82, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=248.75, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=274.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=331.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=59.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=99.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=140.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=191.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=248.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=305.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='18', width=344.08):
            with Note(default_x=29.26, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=56.73, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=84.21, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=128.16, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=172.12, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=199.59, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=227.06, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=254.53, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.01, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=315.01, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=29.26, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=29.26, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=84.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=84.21, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=128.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=172.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=227.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=282.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='19', width=324.23):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=131.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=131.8, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=172.53, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=213.26, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=238.71, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.17, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=80.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=131.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=172.53, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=213.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=264.17, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='20', width=410.41):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(50.8)
                        RightMargin(0.0)
                    SystemDistance(112.9)
            with Note(default_x=67.24, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=117.66, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=218.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=259.4, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=290.91, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=322.42, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=358.39, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(144.0)
            with Note(default_x=79.11, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=117.66, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=168.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=230.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=290.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=358.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=307.98):
            with Note(default_x=17.23, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=61.72, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=150.69, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=195.17, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=222.97, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=250.78, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=61.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=106.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=150.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=195.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=250.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='22', width=308.3):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=57.34, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=148.02, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=176.35, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=204.69, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=233.02, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=261.36, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(144.0)
            with Note(default_x=23.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=57.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=102.68, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=148.02, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=204.69, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=204.69, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=261.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=261.36, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='23', width=323.69):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(50.8)
                        RightMargin(0.0)
                    SystemDistance(112.9)
            with Note(default_x=55.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=96.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=178.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=219.44, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=245.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=296.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=55.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=96.26, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=137.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=178.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=219.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=270.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='24', width=292.09):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('16th')
            with Note(default_x=116.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=191.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=215.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=240.76, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=265.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=51.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=91.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=141.3, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=191.03, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=240.76, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='25', width=410.91):
            with Note(default_x=20.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=51.53, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=83.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=146.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=211.82, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=243.35, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=275.31, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=275.31, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=275.31, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=275.31, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=306.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=326.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=346.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=377.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(144.0)
            with Note(default_x=20.0, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(12.0)
                Voice('2')
                Type('16th')
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
            with Note():
                Rest()
                Duration(96.0)
                Voice('2')
                Type('half')
        with Measure(number='26', width=409.0):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(50.8)
                        RightMargin(0.0)
                    SystemDistance(116.52)
            with Note(default_x=59.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=95.02, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=117.62, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=140.21, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('begin', number=4)
            with Note(default_x=157.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('end', number=4)
            with Note(default_x=174.55, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=197.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=219.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=264.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=281.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=299.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=317.15, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=361.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=384.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(144.0)
            with Note(default_x=59.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=59.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=59.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=219.73, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=219.73, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(48.0)
                Voice('2')
                Type('quarter')
        with Measure(number='27', width=238.53):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=40.63)
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(144.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=52.66, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=52.66, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=89.51, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=89.51, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=126.37, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=126.37, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=163.22, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=163.22, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=200.08, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=200.08, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='28', width=271.73):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=59.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=129.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=164.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(144.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=59.55, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=59.55, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=94.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=129.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=164.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=208.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='discontinue')
                Repeat(direction='backward')
        with Measure(number='29', width=107.43):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=29.8)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(144.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(144.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(144.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='2', type='discontinue')