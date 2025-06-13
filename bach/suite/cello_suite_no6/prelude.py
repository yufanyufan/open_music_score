with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Cello Suite 6')
    with Identification():
        Creator('Bach', type='composer')
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
            Millimeters(4.28)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2611.21)
            PageWidth(2017.76)
            with PageMargins(type='even'):
                LeftMargin(93.4579)
                RightMargin(93.4579)
                TopMargin(93.4579)
                BottomMargin(186.916)
            with PageMargins(type='odd'):
                LeftMargin(93.4579)
                RightMargin(93.4579)
                TopMargin(93.4579)
                BottomMargin(186.916)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Cello Suite 6', default_x=1008.88, default_y=2517.76, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Prelude', default_x=1008.88, default_y=2424.3, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Bach', default_x=1924.3, default_y=2417.76, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Piano')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=372.61):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('12')
                    BeatType('8')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=121.99, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=139.46, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=164.73, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=182.2, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=199.66, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=224.93, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=242.4, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=259.86, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=285.14, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=302.6, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=320.06, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=347.84, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=139.46, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=199.66, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=259.86, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=320.06, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(6.0)
        with Measure(number='2', width=262.61):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=29.46, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=54.74, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=72.2, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=89.67, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=114.94, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=132.41, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=149.87, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=175.14, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=192.61, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=210.07, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=237.85, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=29.46, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=89.67, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=149.87, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=210.07, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(6.0)
        with Measure(number='3', width=240.68):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=29.24, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=46.48, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=63.72, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=83.18, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.45, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=123.69, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=140.93, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=158.17, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=175.41, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=192.64, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=215.91, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='4', width=240.68):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=29.24, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=46.48, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=63.72, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=83.18, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.45, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=123.69, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=140.93, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=158.17, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=175.41, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=192.64, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=215.91, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='5', width=221.68):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=28.81, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=45.62, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=62.43, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=79.24, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.05, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=112.86, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=129.67, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=146.48, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=163.29, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=180.1, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=196.91, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='6', width=221.68):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=28.81, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=45.62, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=62.43, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=79.24, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.05, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=112.86, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=129.67, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=146.48, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=163.29, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=180.1, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=196.91, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='7', width=250.14):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=41.9, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=58.96, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=76.03, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=93.09, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=110.15, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=127.22, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=144.28, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=161.35, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=178.41, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=208.31, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=225.37, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='8', width=340.81):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(-0.0)
                    SystemDistance(97.84)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=89.61, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=108.13, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=126.64, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=145.16, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=163.68, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=193.57, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=212.09, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=230.6, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=249.12, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=279.02, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=297.53, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=316.05, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='9', width=302.81):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=15.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.6, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=66.49, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=87.29, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=108.08, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=131.35, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=154.62, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=175.41, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=196.21, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=219.47, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=242.74, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=278.05, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='10', width=257.54):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=30.87, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=54.14, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=77.4, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=96.28, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=115.15, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=138.41, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=157.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=176.16, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=195.03, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=213.9, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=232.77, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='11', width=253.74):
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=34.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=52.83, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=76.1, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=94.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=113.13, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=136.39, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=154.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=173.43, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=191.94, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=210.46, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=228.97, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='12', width=327.58):
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=41.26, default_y=-60.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=69.04, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=94.5, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=119.96, default_y=-60.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=147.74, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=173.2, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=198.66, default_y=-60.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=224.13, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=249.59, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=275.05, default_y=-60.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=300.51, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=41.26, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=119.96, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=198.66, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=275.05, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(66.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='13', width=327.58):
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=41.26, default_y=-60.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=69.04, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=94.5, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=119.96, default_y=-60.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=147.74, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=173.2, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=198.66, default_y=-60.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=224.13, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=249.59, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=275.05, default_y=-60.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=300.51, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=41.26, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=119.96, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=198.66, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=275.05, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(66.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='14', width=360.9):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(0.0)
                    SystemDistance(97.84)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=89.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=110.05, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=130.48, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=150.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=180.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=201.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=221.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=242.11, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=265.37, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=285.81, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=315.7, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=336.14, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='15', width=283.29):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=32.43, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=52.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=73.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=103.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=123.63, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=144.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=164.49, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=187.76, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=208.19, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=238.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=258.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='16', width=291.86):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=15.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=37.46, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=59.11, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=82.38, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=104.04, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=125.69, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=148.96, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=178.86, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=200.51, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=223.78, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=245.43, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=267.09, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='17', width=272.86):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=15.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.04, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=56.28, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=76.52, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=106.42, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=126.65, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=146.89, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=167.13, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=187.37, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=207.61, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=227.85, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=248.09, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='18', width=293.46):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=17.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=47.7, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=68.87, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=90.04, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=111.21, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=132.38, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=153.55, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=174.72, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=205.18, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=226.35, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=247.52, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=268.69, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='19', width=307.7):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=34.02, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=56.04, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=78.07, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=100.09, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=135.39, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=158.66, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=180.68, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.7, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=236.4, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=259.67, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=282.93, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='20', width=357.96):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(0.0)
                    SystemDistance(97.84)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=89.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=109.85, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=141.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=161.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=181.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=202.09, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=222.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=242.57, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=262.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=283.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=303.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=333.2, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='21', width=250.28):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=31.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=50.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=70.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=89.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=109.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=128.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=147.87, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=167.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=186.69, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=206.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=225.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='22', width=250.28):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=31.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=50.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=70.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=89.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=109.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=128.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=147.87, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=167.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=186.69, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=206.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=225.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='23', width=317.18):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=33.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=73.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=94.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=116.16, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=141.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=162.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=184.53, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=209.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=231.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=252.91, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=292.41, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=33.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=116.16, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=184.53, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=252.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(66.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='24', width=317.18):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=33.55, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=73.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=94.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=116.16, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=141.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=162.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=184.53, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=209.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=231.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=252.91, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=292.41, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=33.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=116.16, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=184.53, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=252.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(66.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='25', width=317.18):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=35.78, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=61.06, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=90.95, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=114.73, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=140.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=163.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=187.57, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=212.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=242.74, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=266.52, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=291.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=35.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=114.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=187.57, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=266.52, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(66.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='26', width=359.78):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(0.0)
                    SystemDistance(97.84)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=89.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=110.23, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=135.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=156.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=176.73, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=202.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=222.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=243.23, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=268.51, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=289.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=309.74, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=335.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=110.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=176.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=243.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=309.74, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(66.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='27', width=282.16):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=32.61, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=57.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=78.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=99.12, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=124.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=145.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=165.62, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=190.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=211.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=232.12, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=257.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=32.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=99.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=165.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=232.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(66.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='28', width=282.16):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=32.61, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=57.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=78.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=99.12, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=124.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=145.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=165.62, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=190.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=211.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=232.12, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=257.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=32.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=99.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=165.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=232.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(66.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='29', width=282.16):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=32.61, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=57.89, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=78.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=99.12, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=124.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=145.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=165.62, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=190.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=211.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=232.12, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=257.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=32.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=99.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=165.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=232.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(66.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='30', width=310.63):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=32.61, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=57.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=78.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=99.12, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=138.62, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=159.24, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=179.85, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=205.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=225.74, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=246.35, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=285.86, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=32.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=99.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=179.85, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=246.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(66.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='31', width=293.16):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=33.44, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=58.71, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=85.38, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=106.82, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=132.09, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=153.53, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=174.97, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=200.25, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=221.68, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=243.12, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=268.4, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=33.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=106.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=174.97, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=243.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(66.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='32', width=382.2):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(0.0)
                    SystemDistance(97.84)
                with StaffLayout(number=2):
                    StaffDistance(68.09)
            with Note(default_x=105.45, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=127.58, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=152.86, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=176.12, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=198.25, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=223.53, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=246.79, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=268.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=291.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=313.18, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=335.3, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=357.43, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=127.58, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(12.0)
            with Note(default_x=198.25, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(30.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='33', width=269.53):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=32.95, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=53.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=74.85, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=116.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=137.7, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=158.65, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=181.91, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=202.86, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=223.81, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=244.76, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='34', width=276.16):
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.07, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=59.34, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=79.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=99.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=129.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=150.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=170.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=190.58, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=210.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=231.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=251.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='35', width=266.19):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=36.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=56.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=75.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=94.95, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=114.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=144.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=163.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=183.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=202.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=221.99, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=241.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='36', width=271.96):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=31.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=51.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=71.54, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=91.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=111.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=131.09, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=150.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=177.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=207.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=227.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=247.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='37', width=344.03):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=21.03, default_y=-88.09):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=53.1, default_y=-93.09):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=78.0, default_y=-98.09):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=102.9, default_y=-93.09):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=132.8, default_y=-113.09):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=157.7, default_y=-118.09):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=182.61, default_y=-113.09):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=207.51, default_y=-93.09):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=232.41, default_y=-98.09):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=257.32, default_y=-93.09):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=292.62, default_y=-88.09):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=317.53, default_y=-93.09):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='38', width=385.73):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(0.0)
                    SystemDistance(97.84)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=89.61, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=121.68, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=144.94, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=168.21, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=191.47, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=214.73, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=244.62, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=267.87, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=291.13, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=314.38, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=337.63, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=360.88, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='39', width=258.09):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=31.47, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=50.93, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=77.6, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=97.06, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=116.53, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=135.99, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=155.46, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=174.93, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=194.39, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=213.86, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=233.32, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='40', width=277.55):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=17.23, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=37.12, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=57.01, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=76.89, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=96.78, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=116.67, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=136.56, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=156.45, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=183.11, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=213.01, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=232.9, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=252.78, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='41', width=290.96):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=21.03, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=41.92, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=62.81, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=83.7, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=104.59, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=125.48, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=146.38, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=167.27, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=190.53, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=213.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=245.3, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=266.19, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='42', width=281.93):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=32.89, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=53.78, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=74.67, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=95.56, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=116.45, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=137.34, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=158.23, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=181.5, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=204.77, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=236.27, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=257.16, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='43', width=315.8):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=34.63, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=57.26, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=79.9, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=102.53, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=125.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=149.06, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=180.57, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=203.2, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=236.9, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=268.4, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=291.03, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='44', width=393.09):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(-0.0)
                    SystemDistance(97.84)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=89.61, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=114.14, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=138.67, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=163.2, default_y=-65.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=187.73, default_y=-70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=212.25, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=236.78, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=261.31, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=285.84, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=317.91, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=342.43, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=366.96, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='45', width=257.34):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=17.23, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=43.9, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=61.54, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=79.18, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=96.82, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=114.47, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=132.11, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=149.75, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=167.39, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=185.04, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=202.68, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=232.58, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='46', width=226.88):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=29.28, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=46.57, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=63.85, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=81.13, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=98.42, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=115.7, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=132.98, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=150.26, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=167.55, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=184.83, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.11, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='47', width=241.11):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=29.44, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=46.89, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=64.33, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=81.78, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=99.22, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=116.67, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=134.11, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=151.56, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=169.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=186.45, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=216.34, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='48', width=226.88):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=29.28, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=46.57, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=63.85, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=81.13, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=98.42, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=115.7, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=132.98, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=150.26, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=167.55, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=184.83, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.11, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='49', width=237.88):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.67, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=56.11, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=73.56, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=91.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=108.44, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=125.89, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=143.33, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=160.78, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=178.22, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=195.67, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=213.11, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='50', width=226.88):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=29.28, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=46.57, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=63.85, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=81.13, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=98.42, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=115.7, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=132.98, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=150.26, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=167.55, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=184.83, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.11, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='51', width=318.18):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(-0.0)
                    SystemDistance(97.84)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=102.21, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=118.29, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=134.36, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=150.43, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=166.51, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=182.58, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=198.65, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=214.73, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=230.8, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=246.88, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=262.95, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=293.41, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='52', width=266.37):
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.07, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=62.33, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=85.6, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=105.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=124.53, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=147.79, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=165.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=183.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=202.67, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=222.14, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=241.6, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='53', width=273.97):
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.07, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=62.33, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=85.6, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=105.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=124.53, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=147.79, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=165.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=183.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=202.67, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=225.94, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=249.2, default_y=-80.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='54', width=251.6):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=28.25, default_y=-145.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=53.52, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=69.77, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=86.02, default_y=-145.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=111.3, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=127.54, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=143.79, default_y=-145.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=169.07, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=185.32, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=201.56, default_y=-145.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=226.84, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=28.25, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=86.02, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=143.79, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=201.56, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(6.0)
        with Measure(number='55', width=251.6):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=28.25, default_y=-145.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=53.52, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=69.77, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=86.02, default_y=-145.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=111.3, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=127.54, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=143.79, default_y=-145.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=169.07, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=185.32, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=201.56, default_y=-145.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=226.84, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=28.25, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=86.02, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=143.79, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=201.56, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(6.0)
        with Measure(number='56', width=224.17):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=28.07, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=54.74, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=70.81, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=86.89, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=102.96, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=119.03, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=135.11, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=151.18, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=167.25, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=183.33, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=199.4, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='57', width=224.17):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=28.07, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=54.74, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=70.81, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=86.89, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=102.96, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=119.03, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=135.11, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=151.18, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=167.25, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=183.33, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=199.4, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='58', width=335.13):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=98.41, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=116.94, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=135.47, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=154.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=172.53, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.06, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=209.59, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=228.12, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=246.64, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=273.31, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=291.84, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=310.37, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='59', width=267.32):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=15.8, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=35.27, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=54.51, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=81.18, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=100.42, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=119.67, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=138.91, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=158.16, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=177.4, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=196.64, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=215.89, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=242.56, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='60', width=237.72):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=30.27, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=48.54, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=66.81, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=85.07, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=103.34, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=121.61, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=139.88, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=158.15, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=176.42, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=194.69, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=212.96, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='61', width=237.72):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=30.27, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=48.54, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=66.81, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=85.07, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=103.34, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=121.61, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=139.88, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=158.15, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=176.42, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=194.69, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=212.96, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='62', width=237.72):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=30.27, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=48.54, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=66.81, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=85.07, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=103.34, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=121.61, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=139.88, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=158.15, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=176.42, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=194.69, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=212.96, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='63', width=256.72):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=31.24, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=50.49, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=69.73, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=88.98, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=108.22, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=127.47, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=146.71, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=165.96, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=185.42, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=208.69, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=231.96, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='64', width=237.72):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=30.27, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=48.54, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=66.81, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=85.07, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=103.34, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=121.61, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=139.88, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=158.15, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=176.42, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=194.69, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=212.96, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='65', width=303.09):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(0.0)
                    SystemDistance(147.26)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=89.61, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=106.54, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=123.46, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=140.39, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=157.31, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=174.23, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=191.16, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=208.08, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=225.01, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=241.93, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=258.85, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=278.32, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='66', width=256.34):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=17.23, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=34.69, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=52.16, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=69.62, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=87.09, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.55, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=129.82, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=149.28, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=166.75, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=196.64, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=214.11, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=231.57, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='67', width=288.35):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=17.23, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.04, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=54.86, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=73.67, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=92.48, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=111.95, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=135.21, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=158.48, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=181.74, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=217.05, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=240.31, default_y=-70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=263.58, default_y=-65.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='68', width=263.07):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.07, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=62.33, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=85.6, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=103.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=121.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=147.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=165.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=183.32, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=202.78, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=220.54, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=238.31, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='69', width=248.27):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.07, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=62.33, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=85.6, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=102.84, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=120.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=137.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=154.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=171.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=189.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=206.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=223.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='70', width=225.47):
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=32.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=49.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=66.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=83.04, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=99.85, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=116.66, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=133.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=150.28, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=167.09, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=183.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=200.71, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='71', width=225.47):
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=32.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=49.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=66.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=83.04, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=99.85, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=116.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=133.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=150.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=167.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=183.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=200.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='72', width=312.9):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(0.0)
                    SystemDistance(147.26)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=93.41, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=111.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=128.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=146.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=164.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=181.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=199.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=217.32, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=235.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=252.73, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=270.43, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=288.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='73', width=235.28):
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=33.5, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=51.2, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=68.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=86.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=104.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=122.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=139.71, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=157.41, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=175.11, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=192.82, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=210.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='74', width=235.28):
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=33.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=51.2, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=68.9, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=86.61, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=104.31, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=122.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=139.71, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=157.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=175.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=192.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=210.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='75', width=231.48):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=29.7, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=47.4, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=65.1, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=82.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=100.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=118.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=135.91, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=153.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=171.31, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=189.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=206.72, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='76', width=231.48):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=29.7, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=47.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=65.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=82.81, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=100.51, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=118.21, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=135.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=153.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=171.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=189.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=206.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='77', width=231.48):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=29.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=47.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=65.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=82.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=100.51, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=118.21, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=135.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=153.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=171.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=189.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=206.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='78', width=332.15):
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=34.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=53.53, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=72.4, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=91.26, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=110.13, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=133.39, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=156.66, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=179.92, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.19, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=222.65, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=238.32, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=269.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=288.52, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=307.38, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='79', width=394.6):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(0.0)
                    SystemDistance(147.26)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=93.41, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=109.86, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=126.31, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=142.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=159.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=178.67, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=201.93, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=225.2, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=248.46, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=271.73, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=294.99, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=330.13, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=346.57, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=369.84, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='80', width=283.58):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=28.45, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=51.71, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=74.98, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=94.44, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=110.89, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=127.34, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=143.79, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=159.45, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=175.12, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=190.78, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.45, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=225.92, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=242.36, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=258.81, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='81', width=212.99):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=28.02, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=44.04, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=60.06, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=76.08, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.1, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=108.13, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=124.15, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=140.17, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=156.19, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=172.21, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=188.23, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='82', width=212.99):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=28.02, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=44.04, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=60.06, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=76.08, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.1, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=108.13, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=124.15, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=140.17, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=156.19, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=172.21, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=188.23, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='83', width=256.48):
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.07, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=62.33, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=78.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=94.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=111.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=127.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=153.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=169.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.71, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=216.04, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=231.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='84', width=449.41):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=27.91, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=43.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.64, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.1, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=111.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.92, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.83, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.3, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.57, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.83, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest()
                Duration(24.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=224.74, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=248.01, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=267.47, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=283.38, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=313.28, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=329.19, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=345.1, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=361.01, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=376.92, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=392.83, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=408.74, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=424.65, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='85', width=498.97):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(0.0)
                    SystemDistance(147.26)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(print_object='no'):
                Rest()
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Staff(1)
            with Note(default_x=137.91, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=154.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=186.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=202.3, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=225.56, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note(default_x=338.25, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=354.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=370.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=386.54, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=402.64, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=425.91, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=89.61, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=105.71, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.81, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=241.66, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=257.76, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.86, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=289.96, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=306.05, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=322.15, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=442.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=458.1, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=474.2, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='86', width=423.35):
            with Note(print_object='no'):
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=62.29, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=78.39, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=110.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.69, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.95, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=262.64, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=278.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=310.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=327.03, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=350.29, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=14.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.1, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=46.2, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=166.05, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=182.15, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.25, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=214.34, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=230.44, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=246.54, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=366.39, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=382.49, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=398.59, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='87', width=443.35):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=28.17, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=44.34, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.01, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.18, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=103.35, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.52, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=135.69, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.86, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.03, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.2, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.37, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=216.54, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=232.71, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=248.88, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=279.34, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=298.81, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.98, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=331.15, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=347.32, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=363.49, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=382.95, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=402.42, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=418.59, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='88', width=444.39):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.47, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.53, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=99.14, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.28, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=131.43, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=147.57, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.71, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.86, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.14, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=228.29, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=244.43, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.57, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.72, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=292.86, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=322.76, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=338.9, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=355.05, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=371.19, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=387.33, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=403.48, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=419.62, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='89', width=575.77):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(0.0)
                    SystemDistance(147.26)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=98.41, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=116.88, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.35, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.82, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.28, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.75, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=220.65, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=239.12, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=257.59, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=284.25, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.72, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=321.19, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=339.66, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=358.12, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=376.59, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=403.26, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=421.73, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=440.19, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=458.66, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=477.13, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=495.6, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=514.07, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=532.53, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=551.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='90', width=311.07):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=35.61, default_y=-105.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=60.88, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=84.49, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=108.1, default_y=-105.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=135.88, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=159.49, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=183.1, default_y=-105.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=210.87, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=234.48, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=258.09, default_y=-105.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=285.86, default_y=-70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=35.61, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=108.1, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=183.1, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=258.09, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(6.0)
        with Measure(number='91', width=311.07):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=35.61, default_y=-105.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=60.88, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=84.49, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=108.1, default_y=-105.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=135.88, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=159.49, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=183.1, default_y=-105.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=210.87, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=234.48, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=258.09, default_y=-105.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=285.86, default_y=-70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=35.61, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=108.1, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=183.1, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=258.09, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(6.0)
        with Measure(number='92', width=306.07):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=35.61, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=60.88, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=84.49, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=108.1, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.38, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=156.99, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=180.6, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=205.87, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=229.48, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=253.09, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=280.86, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=35.61, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=108.1, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=180.6, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=253.09, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(6.0)
        with Measure(number='93', width=306.07):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=35.61, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=60.88, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=84.49, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=108.1, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.38, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=156.99, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=180.6, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=205.87, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=229.48, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=253.09, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=280.86, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=35.61, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=108.1, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=180.6, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=253.09, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(6.0)
        with Measure(number='94', width=522.95):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(0.0)
                    SystemDistance(147.26)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=93.41, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=116.68, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.94, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.21, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=182.67, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.28, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=215.89, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=232.49, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.1, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=265.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=298.92, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=315.52, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=332.13, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=348.73, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=365.34, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=381.95, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=398.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=415.16, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=431.76, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=448.37, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=464.97, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=481.58, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=498.19, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='95', width=443.54):
            with Note(default_x=17.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.07, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.33, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=100.4, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=117.01, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=136.47, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=153.08, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.69, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.29, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.9, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.5, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=236.11, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=252.72, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=269.32, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.53, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.14, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=335.74, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=352.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=368.96, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=385.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=402.17, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=418.77, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='96', width=272.55):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=31.91, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=55.18, default_y=-70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=78.44, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=101.71, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=121.62, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=141.53, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=161.44, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=184.7, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=207.97, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=227.88, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=247.79, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='97', width=263.18):
            with Note(print_object='no'):
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=65.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=113.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=131.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=149.29, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=175.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=193.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=211.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=238.42, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=29.9, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=47.8, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='98', width=307.83):
            with Note(default_x=14.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=33.24, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=62.1, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=81.34, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=115.04, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=134.51, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(print_object='no'):
                Rest()
                Duration(12.0)
                Voice('3')
                Type('quarter')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(24.0)
                Voice('3')
                Type('half')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest()
                Duration(24.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=153.74, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', default_y=39.65, relative_y=10.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=231.56, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', default_y=39.65, relative_y=10.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=170.23, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=248.04, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(60.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=161.99, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=239.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
        with Measure(number='99', width=431.6):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.78)
                        RightMargin(0.0)
                    SystemDistance(147.26)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=89.61, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', default_y=39.65, relative_y=10.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=173.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', default_y=39.65, relative_y=10.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=264.74, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', default_y=39.65, relative_y=10.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=347.37, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', default_y=34.65, relative_y=10.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(72.0)
            with Note(default_x=106.1, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=190.29, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=281.23, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=363.86, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(60.0)
            with Note(default_x=97.85, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=182.05, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=272.99, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=355.62, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(12.0)
        with Measure(number='100', width=282.99):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=33.58, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=55.15, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=76.73, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=98.3, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=119.88, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=141.46, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=163.03, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=184.61, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=215.07, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=236.65, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=258.23, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='101', width=279.59):
            with Note(print_object='no'):
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=144.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=166.53, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=188.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=210.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=232.75, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=254.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=34.08, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=56.15, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=78.23, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=100.3, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=122.38, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(24.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='102', width=271.99):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=36.84, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=57.88, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=78.92, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=99.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=120.99, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=142.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=163.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=184.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=205.15, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=226.19, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=247.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='103', width=287.19):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=34.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=57.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=80.15, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=102.86, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=125.58, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=148.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=171.01, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=193.73, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=216.44, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=239.16, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=262.43, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='104', width=256.69):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=33.47, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=54.94, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=76.4, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=97.87, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=119.34, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=140.81, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=162.27, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=183.74, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=205.21, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', default_y=14.42, relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')