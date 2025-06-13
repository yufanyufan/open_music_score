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
            Millimeters(7.056)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1683.25)
            PageWidth(1190.8)
            with PageMargins(type='even'):
                LeftMargin(56.6894)
                RightMargin(56.6894)
                TopMargin(56.6894)
                BottomMargin(113.379)
            with PageMargins(type='odd'):
                LeftMargin(56.6894)
                RightMargin(56.6894)
                TopMargin(56.6894)
                BottomMargin(113.379)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Bourrée in E minor', default_x=595.402, default_y=1626.56, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J. S. Bach', default_x=1134.12, default_y=1526.56, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('BWV 996', default_x=595.402, default_y=1569.88, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Guitar')
            PartAbbreviation('Guit.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Guitar')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(25)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=145.68):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(70.8)
                        RightMargin(0.0)
                    TopSystemDistance(188.85)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(1)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Allegretto', default_x=-33.11, default_y=72.45, font_weight='bold', font_family='Times New Roman', font_size='12')
                Sound(tempo=120.0)
            with Note(default_x=93.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Direction(placement='above'):
                with DirectionType():
                    Words('II', default_y=51.85, font_family='Times New Roman', font_size='7.9995')
            with Note(default_x=119.41, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(2.0)
            with Note(default_x=93.15, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=119.41, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
        with Measure(number='1', width=210.05):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=30.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=68.22, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=91.88, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=123.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=161.13, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=184.79, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(8.0)
            with Note(default_x=30.37, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=68.22, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=123.28, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=161.13, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
        with Measure(number='2', width=229.52):
            with Note(default_x=17.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('0')
            with Direction(placement='above'):
                with DirectionType():
                    Words('II', default_y=39.35, font_family='Times New Roman', font_size='7.9995')
            with Note(default_x=63.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=95.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=123.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
                        String(2)
            with Note(default_x=170.15, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=199.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(8.0)
            with Note(default_x=17.42, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=63.64, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=123.92, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=170.15, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
        with Measure(number='3', width=185.48):
            with Note(default_x=17.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=54.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=77.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=100.62, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=137.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=160.71, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Backup():
                Duration(8.0)
            with Note(default_x=17.42, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=54.4, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=100.62, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=137.6, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
        with Measure(number='4', width=235.89):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=43.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=70.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=97.74, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=125.05, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=179.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Direction(placement='above'):
                with DirectionType():
                    Words('II', default_y=51.85, font_family='Times New Roman', font_size='7.9995')
            with Note(default_x=206.98, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=70.42, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=125.05, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=152.36, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=179.67, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=206.98, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
        with Measure(number='5', width=278.55):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(56.8)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=80.06, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=122.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=149.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=180.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=223.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=250.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(8.0)
            with Note(default_x=80.06, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=122.77, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=180.86, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=223.56, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
        with Measure(number='6', width=246.71):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Words('II', default_y=39.35, font_family='Times New Roman', font_size='7.9995')
            with Note(default_x=66.76, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=98.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=130.45, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
                        String(2)
            with Note(default_x=181.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=213.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=66.76, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=130.45, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=181.41, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
        with Measure(number='7', width=216.93):
            with Note(default_x=17.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=60.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=86.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=113.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Technical():
                        String(4)
                        Fingering('2')
            with Note(default_x=182.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('0')
            with Backup():
                Duration(8.0)
            with Note(default_x=17.42, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=60.03, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=113.3, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        String(5, placement='below')
                        Fingering('3', placement='below')
            with Note(default_x=155.92, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        String(5, placement='below')
        with Measure(number='8', width=152.92):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=72.75)
            with Note(default_x=17.06, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=83.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Direction(placement='above'):
                with DirectionType():
                    Words('II', default_y=51.85, font_family='Times New Roman', font_size='7.9995')
            with Note(default_x=108.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(8.0)
            with Note(default_x=17.06, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=17.06, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=17.06, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=83.08, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=108.82, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='discontinue', relative_x=-9.5)
                Repeat(direction='backward')
        with Measure(number='9', width=125.52):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=37.75)
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=76.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=100.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=15.8, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=15.8, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=76.56, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue', relative_x=-1.0)
        with Measure(number='10', width=321.98):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(56.8)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=108.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=155.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=185.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=214.5, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=261.56, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=290.97, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(8.0)
            with Note(default_x=108.62, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=155.68, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=214.5, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=261.56, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
        with Measure(number='11', width=257.93):
            with Note(default_x=17.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=70.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
                        String(3)
            with Note(default_x=103.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
                        String(2)
            with Note(default_x=136.88, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        String(3)
                        Fingering('3')
            with Note(default_x=189.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
                        String(3)
            with Note(default_x=223.15, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(8.0)
            with Note(default_x=17.42, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=70.51, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=136.88, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=189.97, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
        with Measure(number='12', width=201.54):
            with Note(default_x=17.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=57.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=83.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
                        String(3)
            with Note(default_x=108.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
                        String(3)
            with Note(default_x=149.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('4')
                        String(3)
            with Note(default_x=174.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Backup():
                Duration(8.0)
            with Note(default_x=17.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=57.83, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=108.58, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=149.18, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
        with Measure(number='13', width=239.18):
            with Note(default_x=16.66, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=179.53, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=208.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Backup():
                Duration(8.0)
            with Note(default_x=17.02, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=46.04, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=75.06, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=104.08, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=133.1, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=179.53, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
        with Measure(number='14', width=287.28):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(56.8)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=80.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=126.06, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=154.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=183.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=228.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
                        String(3)
            with Note(default_x=257.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(8.0)
            with Note(default_x=80.46, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=126.06, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=183.07, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=228.67, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
        with Measure(number='15', width=212.23):
            with Note(default_x=16.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=59.89, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=86.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
                        String(2)
            with Note(default_x=113.72, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
                        String(2)
            with Note(default_x=156.79, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=183.71, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Backup():
                Duration(8.0)
            with Note(default_x=16.82, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=59.89, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=113.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=156.79, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
        with Measure(number='16', width=246.95):
            with Note(default_x=16.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
            with Direction(placement='above'):
                with DirectionType():
                    Words('<font size="7.9995"/><font face="Times New Roman"/>II')
                with DirectionType():
                    Dashes(type='start', number=1)
            with Note(default_x=59.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=85.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('4')
                        String(3)
            with Direction(placement='above'):
                with DirectionType():
                    Words('tr', default_y=65.41, font_style='italic', font_family='Times New Roman', font_size='7.9995')
            with Note(default_x=109.79, default_y=-20.0):
                Grace()
                with Pitch():
                    Step('B')
                    Octave(3)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=143.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=212.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('0')
            with Backup():
                Duration(8.0)
            with Note(default_x=16.82, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=59.04, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=143.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Direction(placement='above'):
                with DirectionType():
                    Dashes(type='stop', number=1)
            with Note(default_x=186.18, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
        with Measure(number='17', width=274.17):
            with Note(default_x=17.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=211.1, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=241.83, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        String(2)
                        Fingering('3')
            with Backup():
                Duration(8.0)
            with Note(default_x=17.42, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('2', placement='below')
                        String(6, placement='below')
            with Note(default_x=61.37, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=92.1, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=128.91, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=161.92, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
                        String(5, placement='below')
            with Note(default_x=211.1, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        String(6, placement='below')
                        Fingering('2', placement='below')
        with Measure(number='18', width=286.25):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(56.8)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=87.08, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
                        String(2)
            with Note(default_x=128.38, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=154.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=189.38, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=230.68, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
                        String(2)
            with Note(default_x=258.84, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(8.0)
            with Note(default_x=87.08, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
                        String(5, placement='below')
            with Note(default_x=128.38, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=189.38, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=230.68, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
        with Measure(number='19', width=226.54):
            with Note(default_x=15.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=62.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=91.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=120.38, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
            with Direction(placement='above'):
                with DirectionType():
                    Words('<font size="7.9995"/><font face="Times New Roman"/>III')
                with DirectionType():
                    Dashes(type='start', number=1)
            with Note(default_x=166.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=195.89, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Direction(placement='above'):
                with DirectionType():
                    Dashes(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.82, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=62.29, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('natural', parentheses='yes')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=120.38, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=166.85, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
        with Measure(number='20', width=261.4):
            with Note(default_x=17.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
                        String(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('<font size="7.9995"/><font face="Times New Roman"/>V')
                with DirectionType():
                    Dashes(type='start', number=1)
            with Note(default_x=69.31, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Direction(placement='above'):
                with DirectionType():
                    Dashes(type='stop', number=1)
            with Note(default_x=101.87, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=142.58, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp', parentheses='yes')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
                        String(2)
            with Note(default_x=194.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=227.24, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Backup():
                Duration(8.0)
            with Note(default_x=17.22, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=69.31, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=142.58, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=194.68, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
        with Measure(number='21', width=246.45):
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=63.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('3')
                        String(3)
            with Note(default_x=187.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('4')
                        String(2)
            with Note(default_x=215.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
                        String(3)
            with Backup():
                Duration(8.0)
            with Note(default_x=17.23, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=92.4, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=121.31, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=150.22, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=187.03, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
        with Measure(number='22', width=362.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(56.8)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('<font size="7.9995"/><font face="Times New Roman"/>½ II')
                with DirectionType():
                    Dashes(type='start', number=1)
            with Note(default_x=93.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural', parentheses='yes')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=162.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural', parentheses='yes')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Direction(placement='above'):
                with DirectionType():
                    Dashes(type='stop', number=1)
            with Note(default_x=194.66, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=232.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=296.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=328.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('0')
            with Backup():
                Duration(8.0)
            with Note(default_x=93.02, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=125.17, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=162.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=232.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Accidental('natural', parentheses='yes')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=264.15, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=296.3, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
        with Measure(number='23', width=257.79):
            with Note(default_x=15.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Direction(placement='above'):
                with DirectionType():
                    Words('<font size="7.9995"/><font face="Times New Roman"/>IV')
                with DirectionType():
                    Dashes(type='start', number=1)
            with Note(default_x=84.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
                        String(3)
            with Note(default_x=114.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
                        String(4)
            with Direction(placement='above'):
                with DirectionType():
                    Dashes(type='stop', number=1)
            with Note(default_x=145.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('0')
            with Note(default_x=194.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=225.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(8.0)
            with Note(default_x=15.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=51.01, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=84.02, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
                        String(5, placement='below')
            with Note(default_x=145.51, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
                        String(5, placement='below')
            with Note(default_x=194.7, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
        with Measure(number='24', width=187.71):
            with Note(default_x=17.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=54.76, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=78.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Direction(placement='above'):
                with DirectionType():
                    Words('<font size="7.9995"/><font face="Times New Roman"/>II')
                with DirectionType():
                    Dashes(type='start', number=1)
            with Note(default_x=101.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=139.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Direction(placement='above'):
                with DirectionType():
                    Dashes(type='stop', number=1)
            with Note(default_x=162.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(8.0)
            with Note(default_x=17.23, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=54.76, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=101.31, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
        with Measure(number='25', width=134.79):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=33.4)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=71.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=93.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Technical():
                        Fingering('0', placement='below')
            with Note(default_x=71.55, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='discontinue', relative_x=-10.0)
                Repeat(direction='backward')
        with Measure(number='26', width=78.14):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=29.8)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='2', type='discontinue')