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
        Source('https://musescore.com/score/4430776')
    with Defaults():
        with Scaling():
            Millimeters(5.6)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2120.93)
            PageWidth(1500.43)
            with PageMargins(type='even'):
                LeftMargin(71.4286)
                RightMargin(71.4286)
                TopMargin(71.4286)
                BottomMargin(142.857)
            with PageMargins(type='odd'):
                LeftMargin(71.4286)
                RightMargin(71.4286)
                TopMargin(71.4286)
                BottomMargin(142.857)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('SUITE II.', default_x=750.213, default_y=2049.5, justify='center', valign='top', font_weight='bold', font_size='24')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Violoncello')
            PartAbbreviation('Vc.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Violoncello')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(43)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=354.01):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(50.0)
                        RightMargin(0.0)
                    TopSystemDistance(140.7)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.0, relative_x=-33.5, relative_y=50.0):
                        BeatUnit('quarter')
                        PerMinute('54')
                Sound(tempo=54.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Prélude', default_y=15.0, font_weight='bold', font_size='14')
            with Note(default_x=98.23, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=141.5, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=184.76, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=244.25, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=271.29, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=298.33, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=325.37, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='2', width=309.04):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.68, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.13, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.59, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=131.04, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=193.63, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=222.08, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=250.53, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.99, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='3', width=359.63):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=43.39, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.77, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.47, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=139.86, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=201.1, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=232.48, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=263.87, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.26, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=326.64, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='4', width=284.89):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.09, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.17, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.26, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=116.34, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=158.08, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=199.82, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=241.55, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='5', width=373.79):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(110.54)
            with Note(default_x=77.18, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=104.12, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=131.06, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.99, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=184.93, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=237.49, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=264.43, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=291.37, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=318.31, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=345.25, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='6', width=344.14):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.55, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.09, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.64, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=122.18, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=149.73, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.27, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=204.82, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=232.36, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=259.91, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.45, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=315.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='7', width=304.24):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.54, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.08, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.62, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=118.16, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=169.94, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=196.48, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=223.02, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.56, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.1, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='8', width=335.4):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.82, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.63, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.45, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=119.27, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=146.08, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.9, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.72, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=226.54, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=253.35, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=280.17, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=306.99, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='9', width=356.33):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(110.54)
            with Note(default_x=77.18, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=102.52, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.87, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.21, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=178.56, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=228.01, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=253.35, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=278.7, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=304.04, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=329.39, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='10', width=333.13):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.42, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.85, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.27, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=117.7, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=144.12, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.55, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.97, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=223.39, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=249.82, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.24, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.11, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='11', width=322.32):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=37.73, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.45, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.18, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.91, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=140.63, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.36, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.09, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=217.81, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=243.54, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=269.27, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.99, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=345.78):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.57, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.15, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.72, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=122.3, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=149.87, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.45, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.02, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=233.88, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=261.46, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=289.03, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=316.61, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='13', width=313.76):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(110.54)
            with Note(default_x=77.18, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=117.18, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=157.17, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=212.17, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=237.17, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=262.17, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.16, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='14', width=374.54):
            with Note(default_x=17.23, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=46.85, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.47, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.09, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=135.71, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=165.33, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.94, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.56, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=254.46, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=284.08, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=313.7, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=343.32, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='15', width=284.61):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=38.57, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.14, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.71, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=118.28, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=176.73, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=203.3, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=229.87, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=256.44, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='16', width=384.66):
            with Note(default_x=17.23, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=47.72, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.2, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.69, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=139.17, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=169.66, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.14, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.63, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=261.11, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=291.6, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=322.09, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=352.57, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='17', width=392.4):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(110.54)
            with Note(default_x=77.18, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=103.84, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=129.55, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.26, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=180.96, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=206.67, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=232.38, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.27, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=287.98, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=313.69, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=339.39, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=365.1, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='18', width=337.66):
            with Note(default_x=14.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=43.3, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.2, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.5, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=131.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=188.96, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=218.26, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=247.56, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.46, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=306.76, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='19', width=311.01):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.73, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.46, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.19, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=118.92, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=171.06, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=199.33, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=226.06, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.95, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.68, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=316.5):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.6, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.2, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.79, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=122.39, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=176.24, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=203.84, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=231.43, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=259.7, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.3, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='21', width=391.69):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(110.54)
            with Note(default_x=77.18, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=102.65, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=128.13, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.39, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=181.87, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.34, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=232.82, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.29, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=283.77, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=309.25, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=334.72, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=364.62, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='22', width=311.56):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.14, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=62.81, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.95, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=116.84, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.98, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=165.12, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.26, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=213.4, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=237.54, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=261.68, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.82, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='23', width=329.45):
            with Note(default_x=17.23, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.5, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=67.76, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.03, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=119.69, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=144.96, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=170.22, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.49, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=225.38, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=250.65, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=275.91, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.58, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='24', width=324.87):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=38.67, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.36, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.06, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=115.76, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.42, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.12, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.82, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=219.51, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=245.21, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.91, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.57, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='25', width=385.54):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(110.54)
            with Note(default_x=89.22, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=115.7, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.17, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.65, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=197.51, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=249.17, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=275.64, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=304.51, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.99, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=357.46, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='26', width=319.94):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=37.22, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.45, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=87.67, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.9, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.76, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=166.99, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.21, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=217.44, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=242.66, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=267.89, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=293.11, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='27', width=321.12):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=37.24, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.48, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=87.72, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.95, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.19, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=163.43, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.67, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=218.57, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=243.81, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=269.04, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.28, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=330.98):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.45, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.9, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=91.34, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=117.79, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=144.24, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=170.69, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.14, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=223.58, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=250.03, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=276.48, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.93, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='29', width=386.81):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(110.54)
            with Note(default_x=77.18, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=102.85, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.52, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=154.19, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=179.86, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=205.52, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=231.19, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=256.86, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=282.53, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=308.2, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=333.87, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=359.54, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='30', width=333.7):
            with Note(default_x=21.03, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=45.7, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=70.37, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.04, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=119.71, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=144.38, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=169.05, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.72, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=227.41, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=258.09, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=282.76, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=307.43, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='31', width=316.15):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=36.44, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=60.88, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=94.58, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.02, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=143.46, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=167.9, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.34, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=216.78, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=241.22, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=265.67, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=290.11, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='32', width=320.92):
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.78, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=66.34, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.89, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=115.44, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.99, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=164.55, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.1, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=219.0, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=245.66, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=270.21, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.77, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='33', width=388.5):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(110.54)
            with Note(default_x=89.22, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=115.88, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.52, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=165.16, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=189.8, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=214.44, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=239.07, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=263.71, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=288.35, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=312.99, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=337.62, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=362.26, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='34', width=303.0):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=36.12, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=60.23, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=84.35, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=108.47, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.58, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=156.7, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.82, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=204.93, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=229.05, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=253.17, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.28, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='35', width=336.85):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.32, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.65, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=98.34, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=124.67, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=150.99, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.31, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.63, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=229.96, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=256.28, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=282.6, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=308.92, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='36', width=329.22):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.3, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.6, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.91, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=117.21, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=143.51, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.81, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.11, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=222.41, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=248.72, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.02, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=301.32, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='37', width=419.22):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(110.54)
            with Note(default_x=77.18, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=105.07, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.96, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=160.85, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=189.72, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=217.61, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.5, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.39, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=301.28, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=329.17, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=361.84, default_y=20.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=389.73, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='38', width=335.68):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.56, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.12, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.02, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=121.58, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=148.14, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=174.71, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.27, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=227.83, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=254.39, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=280.95, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=307.52, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='39', width=363.51):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=41.09, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.18, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=99.28, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=128.37, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=157.46, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.36, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=216.45, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=245.54, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=274.63, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=303.72, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=332.82, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='40', width=239.17):
            with Note(default_x=21.03, default_y=-60.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=57.86, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=94.7, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=145.34, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=168.36, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=191.38, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.4, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='41', width=371.74):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(110.54)
            with Note(default_x=77.18, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=101.59, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=126.01, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=150.42, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=174.83, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=199.25, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=223.66, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=248.07, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=272.49, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=296.9, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=321.31, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=345.73, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='42', width=261.05):
            with Note(default_x=17.23, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=58.46, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=99.69, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=156.38, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=182.14, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.91, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=233.68, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='43', width=334.45):
            with Note(default_x=21.03, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=49.3, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.07, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=100.85, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=126.63, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.41, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.19, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.96, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=229.74, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=255.52, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=281.3, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=307.07, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='44', width=390.33):
            with Note(default_x=15.8, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=46.19, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.5, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.89, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=142.29, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=175.98, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.37, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.77, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=267.16, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=297.55, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=327.95, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=358.34, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='45', width=444.96):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(110.54)
            with Note(default_x=77.18, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=106.9, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.2, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.92, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=201.64, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=235.34, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=265.05, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.77, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=324.49, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=354.21, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=383.93, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=413.64, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='46', width=361.72):
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=51.11, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.37, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.45, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=135.52, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=163.6, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.67, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.74, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=247.82, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=275.89, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=303.97, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=332.04, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='47', width=397.7):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=47.31, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=78.82, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.33, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=141.84, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=173.35, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=204.85, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=238.55, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=270.06, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=301.57, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=333.08, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=364.59, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='48', width=153.19):
            with Note(default_x=21.03, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=28.4, relative_y=10.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(24.0)
            with Note(default_x=26.39, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=23.71, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Forward():
                Duration(16.0)
        with Measure(number='49', width=514.41):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=88.38, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.75, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=159.12, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.49, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=229.86, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=265.23, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=300.6, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=335.97, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=371.34, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=406.71, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=442.08, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=477.44, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='50', width=413.94):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=53.31, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.39, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.47, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=161.55, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=231.94, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=268.02, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=304.1, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=340.18, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=376.26, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='51', width=429.22):
            with Note(default_x=14.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=48.47, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=82.94, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=117.4, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=151.87, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.34, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.81, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.28, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=289.75, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=324.21, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=358.68, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=393.15, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='52', width=398.1):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(125.72)
            with Note(default_x=77.18, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=103.23, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=129.29, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.35, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=185.24, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=211.3, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.36, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.22, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=292.28, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=318.33, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=344.39, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=370.44, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='53', width=337.29):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.11, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.01, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.12, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=126.79, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.9, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.01, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.13, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=231.24, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=257.35, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=283.47, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=309.58, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='54', width=317.0):
            with Note(default_x=21.03, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=72.86, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=99.43, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.9, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=182.56, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=209.13, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=235.7, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.26, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=288.83, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=26.39, default_y=-60.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=23.71, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Forward():
                Duration(16.0)
        with Measure(number='55', width=305.18):
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=39.78, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.76, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.74, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=111.73, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=135.71, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.69, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=183.67, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=207.65, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=231.63, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.61, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=279.6, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='56', width=374.84):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(125.72)
            with Note(default_x=80.98, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=103.81, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.7, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.53, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=179.36, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=202.19, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=225.02, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=247.85, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=277.75, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=304.42, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=327.25, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=350.08, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='57', width=269.22):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=33.13, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.26, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.4, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=96.53, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=117.66, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.79, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.93, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=181.06, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=202.19, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=223.32, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=244.46, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='58', width=296.4):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.9, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.79, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.69, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=99.59, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.48, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=151.38, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.28, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=205.94, default_y=20.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=227.84, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.73, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=271.63, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='59', width=83.74):
            with Note(default_x=20.67, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=26.07, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=23.37, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='60', width=78.79):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=21.16, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=18.48, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='61', width=78.79):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=21.16, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=18.48, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='62', width=83.66):
            with Note(default_x=20.67, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=26.03, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=23.35, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='63', width=92.14):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=23.84, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=18.48, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=21.16, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('4')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
        with Measure(number='0', implicit='yes', width=140.95):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(50.0)
                        RightMargin(0.0)
                    SystemDistance(195.2)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(-1)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.31, default_y=38.22, relative_x=75.19, relative_y=45.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Allemande.', relative_x=135.0, relative_y=50.0, font_weight='bold', font_size='14')
            with Note(default_x=99.48, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
        with Measure(number='1', width=388.08):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.2, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=77.28, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=101.36, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=125.44, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=149.51, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=173.59, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=197.67, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=227.57, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=251.64, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=275.72, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=299.8, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=338.32, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=362.4, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=22.71, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(4.0)
            with Note(default_x=20.04, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(4.0)
            with Note(default_x=17.36, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('4')
                Type('eighth')
                Stem('up')
            with Forward():
                Duration(28.0)
        with Measure(number='2', width=358.97):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.41, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=60.81, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.22, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=109.62, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=148.67, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=187.72, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=235.34, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=259.75, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=284.15, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=308.56, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=332.96, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Forward():
                Duration(16.0)
            with Note(default_x=193.08, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Backup():
                Duration(22.0)
            with Forward():
                Duration(16.0)
            with Note(default_x=190.4, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('3')
                Type('eighth')
                Dot()
                Stem('up')
            with Forward():
                Duration(10.0)
        with Measure(number='3', width=419.57):
            with Note(default_x=17.23, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=60.69, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=93.36, default_y=20.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.52, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=147.68, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=174.84, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=202.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=229.17, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=256.33, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=283.49, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=310.65, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=337.81, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=390.8, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=25.27, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(4.0)
            with Note(default_x=22.59, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(4.0)
            with Note(default_x=19.91, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('4')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Forward():
                Duration(28.0)
        with Measure(number='4', width=452.93):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(125.72)
            with Note(default_x=77.18, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=102.2, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.23, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.25, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=177.28, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=202.31, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=227.33, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=252.36, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=277.38, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=302.41, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=327.43, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=352.46, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=377.48, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=426.31, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(32.0)
            with Forward():
                Duration(24.0)
            with Note(default_x=377.48, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=426.31, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='5', width=445.79):
            with Note(default_x=14.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.42, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=70.84, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=99.26, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=127.68, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=161.38, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=189.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.22, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=246.64, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=302.09, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=330.51, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=358.93, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=387.35, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=415.77, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(32.0)
            with Forward():
                Duration(16.0)
            with Note(default_x=246.64, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
            with Forward():
                Duration(10.0)
        with Measure(number='6', width=458.85):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=43.98, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=72.25, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=100.43, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=128.61, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=156.8, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.69, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.88, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=243.06, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=288.15, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=316.34, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=344.52, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=372.7, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=400.89, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=429.07, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='7', width=495.46):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(125.72)
            with Note(default_x=85.98, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=111.28, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.69, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.11, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=186.77, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=212.07, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.49, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.9, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=290.8, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=315.22, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=339.63, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=369.53, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=396.19, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=420.61, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=445.02, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=469.44, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=85.98, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Forward():
                Duration(6.0)
            with Note(default_x=186.77, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Forward():
                Duration(22.0)
        with Measure(number='8', width=346.08):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=36.63, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.46, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.29, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=99.12, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=119.95, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.79, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.62, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('(    )', default_y=39.81, relative_x=-10.0, relative_y=25.0)
            with Note(default_x=191.51, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=232.15, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=258.82, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=279.65, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=300.48, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=321.31, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='9', width=516.04):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.16, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.33, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=96.49, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=124.75, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=169.66, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=199.55, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(32.0)
            with Forward():
                Duration(8.0)
            with Note(default_x=124.75, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=199.55, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=238.28, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=255.88, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=285.78, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=315.67, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=333.28, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=359.94, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=379.41, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=411.47, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=434.74, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=454.2, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=473.67, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=491.27, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='10', width=545.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(125.72)
            with Note(default_x=85.98, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=115.88, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=145.08, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=174.28, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=203.48, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=233.37, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=263.27, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=292.47, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=321.67, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(32.0)
            with Forward():
                Duration(16.0)
            with Note(default_x=321.67, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(20.0)
            with Forward():
                Duration(16.0)
            with Note(default_x=329.71, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=368.39, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=397.59, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=426.79, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=455.99, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=485.19, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=514.39, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='11', width=425.36):
            with Note(default_x=17.23, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=217.81, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=260.39, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.74, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=313.09, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=339.44, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=381.6, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=25.27, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=59.39, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=85.74, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=112.09, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=138.44, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=164.8, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=191.46, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=224.11, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(20.0)
            with Note(default_x=17.23, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Forward():
                Duration(12.0)
            with Note(default_x=217.81, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(12.0)
        with Measure(number='12', width=387.01):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=65.63, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=93.12, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=120.61, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.09, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.58, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=203.07, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=230.56, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.05, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.94, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=315.43, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X1', implicit='yes', width=145.46):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(125.72)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=105.13, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
        with Measure(number='13', width=379.37):
            with Note(default_x=33.63, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=70.24, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=96.9, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=122.12, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=147.34, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=172.56, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=202.46, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=227.68, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=252.9, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.12, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=303.34, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=352.55, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=21.03, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=21.03, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('3')
                Type('eighth')
                Dot()
                Stem('down')
            with Forward():
                Duration(26.0)
        with Measure(number='14', width=430.17):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.96, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=61.92, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.89, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=111.85, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.51, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=168.41, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=193.37, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=218.33, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=243.3, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=268.26, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=293.22, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=323.12, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=348.08, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=376.94, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=403.61, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
        with Measure(number='15', width=402.57):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=35.51, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.03, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=82.54, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.44, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=135.95, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=159.46, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=182.97, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=206.49, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=236.38, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=259.9, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=283.41, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=306.92, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=330.43, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=353.95, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=377.46, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='16', width=524.11):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(125.72)
            with Note(default_x=88.38, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=115.2, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.01, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=168.82, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=195.63, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=222.44, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=249.26, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=276.07, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=302.88, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=329.69, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=356.5, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=383.32, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=410.13, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=440.03, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=466.84, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=495.7, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='17', width=433.4):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.06, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.13, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=93.19, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=120.25, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=147.32, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.98, default_y=20.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=207.05, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=236.94, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=280.24, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=307.31, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=334.37, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=377.67, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=404.74, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Forward():
                Duration(16.0)
            with Note(default_x=236.94, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(12.0)
        with Measure(number='18', width=400.06):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.31, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.62, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.93, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=121.24, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=164.93, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=208.63, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=261.91, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=289.22, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=316.53, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=343.84, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=371.15, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Forward():
                Duration(16.0)
            with Note(default_x=211.31, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Forward():
                Duration(10.0)
        with Measure(number='19', width=467.15):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(125.72)
            with Direction(placement='above'):
                with DirectionType():
                    Words('(    )', default_y=37.31, relative_x=-10.0, relative_y=50.0)
            with Note(default_x=77.18, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=127.86, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=153.83, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=179.81, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=205.79, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=231.76, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=257.74, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=283.72, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=309.69, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=335.67, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=361.65, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=387.62, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=413.6, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=439.58, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=77.18, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
            with Forward():
                Duration(26.0)
        with Measure(number='20', width=421.48):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.49, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=62.98, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.48, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=113.97, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=139.46, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=164.95, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=190.45, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=215.94, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=241.43, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=266.92, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=292.42, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=317.91, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=343.4, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=368.89, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=394.38, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='21', width=468.94):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.98, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=73.68, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=101.66, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=129.64, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=157.62, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=185.61, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=213.59, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=241.57, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=269.55, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=297.53, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=325.51, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=355.41, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=383.39, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=411.38, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=439.36, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='22', width=541.16):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(125.72)
            with Note(default_x=77.18, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.07, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=135.74, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.41, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=193.08, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=221.75, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.64, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=280.31, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=308.98, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=337.65, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=366.32, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=394.99, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=423.65, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=452.32, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=482.22, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=510.89, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=409.68):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=42.31, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.39, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=92.47, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=117.55, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.63, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=167.71, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=192.79, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=217.87, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=247.77, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=272.85, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=302.74, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=327.82, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=367.95, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='24', width=406.74):
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.51, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=73.57, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=99.28, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=124.99, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=150.69, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=176.4, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=210.1, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=235.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=261.51, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.22, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=312.92, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=338.63, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='0', implicit='yes', width=138.0):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(50.0)
                        RightMargin(0.0)
                    TopSystemDistance(75.7)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('3')
                    BeatType('4')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Courante.', relative_x=120.0, relative_y=50.0, font_weight='bold', font_size='14')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.0, default_y=63.73, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('90')
                Sound(tempo=90.0)
            with Note(default_x=98.23, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
        with Measure(number='1', width=392.9):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=47.09, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.38, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.68, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=140.97, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=172.26, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.55, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.84, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=266.13, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=297.43, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=328.72, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=360.01, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='2', width=376.57):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=94.39, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=129.46, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.53, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.61, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=234.68, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=269.75, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=304.82, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=339.89, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=33.3, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=18.38, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Forward():
                Duration(16.0)
        with Measure(number='3', width=400.1):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.21, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.42, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.63, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=140.83, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=173.04, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.25, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=237.46, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=269.67, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=301.88, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=334.08, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=366.29, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='4', width=421.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(88.67)
            with Note(default_x=89.22, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=116.4, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.59, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=170.78, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=200.67, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=227.86, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.04, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.23, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=309.42, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=338.28, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=365.47, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=392.65, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='5', width=324.79):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.93, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.86, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=89.8, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=115.73, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.66, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.59, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.53, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=219.46, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=245.39, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=271.32, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.26, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='6', width=294.55):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=75.17, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=102.16, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=129.15, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.14, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=183.12, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=211.99, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=238.98, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=265.97, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=21.16, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=18.48, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Forward():
                Duration(16.0)
        with Measure(number='7', width=316.79):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.14, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=62.28, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.42, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=112.55, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.69, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.36, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.5, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=214.63, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=239.77, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.91, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=290.05, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='8', width=354.41):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(88.67)
            with Note(default_x=80.98, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=103.58, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=126.19, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=148.8, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=171.4, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=194.01, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=216.61, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.22, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=261.83, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=284.43, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=307.04, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=329.64, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='9', width=285.43):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.61, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.21, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.82, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=102.42, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.03, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.64, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.24, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=192.85, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=215.45, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=238.06, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.67, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='10', width=372.89):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=46.36, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.48, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=104.6, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=138.3, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=167.43, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.55, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=225.67, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=254.8, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=283.92, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=313.05, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=342.17, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='11', width=344.83):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.09, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.18, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=93.27, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=120.36, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.43, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.52, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.61, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=234.87, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=261.96, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=289.05, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=316.14, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=384.32):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(88.67)
            with Note(default_x=89.22, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=113.24, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.9, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=163.92, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=187.93, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.95, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.97, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=259.98, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=284.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=308.02, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=332.04, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=358.7, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='13', width=317.93):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.78, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=63.44, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.22, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=113.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.77, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.67, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.45, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=217.22, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=242.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.78, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=291.55, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='14', width=317.93):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.78, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=63.44, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.22, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=113.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.77, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.67, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.45, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=217.22, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=242.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.78, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=291.55, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='15', width=337.39):
            with Note(default_x=17.23, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=43.02, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=69.69, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.48, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=121.26, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=147.05, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.95, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.74, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=228.53, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=254.32, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=280.11, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=310.0, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='16', width=358.43):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(88.67)
            with Note(default_x=77.18, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=102.77, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.67, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.26, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=183.86, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=209.45, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.05, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.94, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=290.54, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X1', implicit='yes', width=57.12):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=24.95, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
        with Measure(number='17', width=335.99):
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=51.11, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.06, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=101.02, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=125.98, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=150.94, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.9, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.86, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=225.81, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=250.77, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=284.47, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=309.43, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='18', width=298.52):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=75.74, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=102.99, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.23, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.48, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=184.72, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.97, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.21, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=269.68, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(16.0)
        with Measure(number='19', width=307.52):
            with Note(default_x=14.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.11, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.23, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.34, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=110.45, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=134.57, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.68, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=182.8, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=209.46, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=233.57, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=257.69, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=281.8, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='20', width=402.24):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(88.67)
            with Note(default_x=77.18, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=103.96, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.74, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=157.52, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=184.3, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.09, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.87, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.65, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=293.51, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=320.3, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=347.08, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=373.86, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='21', width=341.6):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=66.93, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.07, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=121.2, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=148.33, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.2, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=204.33, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=231.46, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=258.6, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.73, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=312.86, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Forward():
                Duration(22.0)
        with Measure(number='22', width=297.47):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=73.23, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=101.06, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.89, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.72, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=184.55, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=212.38, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=240.21, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=268.04, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(16.0)
        with Measure(number='23', width=316.26):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.22, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=62.44, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.67, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=112.89, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.11, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.33, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.55, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=213.77, default_y=-60.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=239.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.22, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=289.44, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=379.47):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(88.67)
            with Note(default_x=77.18, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=102.24, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=127.29, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.35, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=177.41, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=202.47, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.52, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=252.58, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=277.64, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=302.7, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=327.75, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=352.81, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='25', width=330.52):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=43.14, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.81, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.72, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=121.63, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=147.54, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.45, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.36, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=225.28, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=251.19, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.1, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=303.01, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='26', width=329.49):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.32, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.65, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.97, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=117.3, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=143.62, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.95, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.27, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=222.59, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=248.92, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.24, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=301.57, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=318.09):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.37, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=62.75, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.12, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=113.5, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.87, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.25, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.62, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=214.99, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=240.37, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=265.74, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=291.12, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=322.61):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(88.67)
            with Note(default_x=93.02, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=116.28, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.55, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.82, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=178.83, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=194.85, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.32, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=233.78, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=249.8, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=265.81, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=281.83, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.85, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=268.84):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=28.09, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.35, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.62, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.88, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.15, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.46, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.72, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=195.81, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.9, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.98, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=244.07, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='30', width=280.24):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.47, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=54.73, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.0, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.26, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=124.53, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.83, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=183.1, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=202.57, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=222.03, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=238.75, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.47, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=292.1):
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.42, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=56.69, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.96, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.22, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.49, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.79, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.06, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=201.25, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=217.44, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=233.64, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=267.33, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='32', width=193.79):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.71, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=47.61, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.52, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=79.43, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=95.34, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.24, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.15, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=143.06, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='1', width=266.8):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(50.0)
                        RightMargin(0.0)
                    SystemDistance(187.37)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('3')
                    BeatType('4')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.8, default_y=95.39, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Sound(tempo=60.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Sarabande.', default_y=31.67, relative_x=140.0, relative_y=50.0, font_weight='bold', font_size='14')
            with Note(default_x=99.04, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=141.95, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=163.94, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=220.04, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=242.04, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=98.23, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=163.58, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='2', width=146.34):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=64.31, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=91.12, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=117.93, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.36, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=14.68, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
            with Forward():
                Duration(12.0)
        with Measure(number='3', width=214.86):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=41.08, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('(    )', default_y=28.64, relative_x=-10.0, relative_y=22.5)
            with Note(default_x=70.15, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=99.23, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=117.4, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=135.58, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=153.75, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.92, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.09, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='4', width=151.9):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=69.67, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=96.54, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=123.42, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='5', width=162.1):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=49.61, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('(    )', default_y=64.81, relative_x=-5.0, relative_y=35.0)
            with Note(default_x=68.88, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=118.06, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.33, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.36, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=14.68, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note(default_x=68.52, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('3')
                Type('half')
                Stem('down')
        with Measure(number='6', width=146.34):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=64.31, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=91.12, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=117.93, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.36, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=14.68, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
            with Forward():
                Duration(12.0)
        with Measure(number='7', width=219.23):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=42.39, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=61.39, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=80.39, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=99.85, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=118.85, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=137.84, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=156.84, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=187.24, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='8', width=203.39):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(127.32)
            with Note(default_x=77.18, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=126.28, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=151.45, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=176.62, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=82.54, default_y=-60.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=79.86, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
            with Forward():
                Duration(12.0)
        with Measure(number='9', width=171.42):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=42.13, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=60.96, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=79.79, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=127.82, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=146.65, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=79.79, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Backup():
                Duration(20.0)
            with Forward():
                Duration(8.0)
            with Note(default_x=85.15, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
            with Forward():
                Duration(4.0)
        with Measure(number='10', width=168.88):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=40.31, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=58.01, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=76.07, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=120.85, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=144.12, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=80.7, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('2')
                Type('half')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Forward():
                Duration(8.0)
            with Note(default_x=78.03, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('3')
                Type('half')
                Stem('up')
        with Measure(number='11', width=151.55):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=34.96, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=57.91, default_y=-60.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=80.87, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=103.83, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=126.78, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=102.25):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.44, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='13', width=153.8):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=24.95, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.72, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=127.3, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(24.0)
            with Note(default_x=24.95, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.82, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=78.72, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Forward():
                Duration(4.0)
        with Measure(number='14', width=213.57):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=46.2, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=65.2, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.1, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=132.17, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=151.17, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=181.57, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(16.0)
        with Measure(number='15', width=192.71):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=41.14, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=70.27, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=100.17, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=132.84, default_y=20.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=161.97, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='16', width=225.05):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(138.87)
            with Note(default_x=77.18, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=134.82, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=164.36, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=193.91, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=82.54, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=79.86, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
            with Forward():
                Duration(12.0)
        with Measure(number='17', width=161.7):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=36.68, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=61.37, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=86.05, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=110.73, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=135.42, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='18', width=192.06):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=41.74, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=71.49, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=101.23, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=130.97, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=160.72, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='19', width=215.61):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=45.22, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=73.21, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=101.2, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=118.7, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=145.36, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=173.35, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=190.84, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=194.18):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=46.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=63.99, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=81.97, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=117.05, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=135.04, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=163.81, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=170.93):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=42.02, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=60.78, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=79.54, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=127.41, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=146.17, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.86, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='22', width=198.04):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=39.58, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=56.82, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=90.52, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=156.03, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=173.27, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=14.68, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note(default_x=95.88, default_y=-60.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(8.0)
            with Note(default_x=93.2, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
            with Forward():
                Duration(4.0)
        with Measure(number='23', width=324.37):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(126.67)
            with Note(default_x=77.18, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=125.84, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=149.11, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=169.83, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=198.33, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=219.05, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=234.72, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=250.38, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=278.88, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=299.6, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=77.18, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=198.33, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=250.38, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(24.0)
            with Note(default_x=82.54, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(4.0)
            with Note(default_x=79.86, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('4')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('4')
                Type('eighth')
            with Forward():
                Duration(16.0)
        with Measure(number='24', width=226.3):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=52.63, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=71.1, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=97.76, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.66, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=146.13, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=164.59, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=183.06, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.53, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='25', width=221.31):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.67, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=61.72, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=84.78, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.68, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=173.49, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=196.55, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=114.68, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
            with Forward():
                Duration(4.0)
        with Measure(number='26', width=240.9):
            with Note(default_x=14.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=53.05, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.92, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=100.79, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=130.68, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=191.56, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=215.43, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=19.36, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note(default_x=130.68, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
            with Backup():
                Duration(20.0)
            with Note(default_x=16.68, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Forward():
                Duration(16.0)
        with Measure(number='27', width=240.47):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=51.11, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.37, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=93.37, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.37, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=142.77, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=173.16, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=208.47, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=104.23):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.55, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='1', width=203.32):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(50.0)
                        RightMargin(0.0)
                    TopSystemDistance(74.69)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('3')
                    BeatType('4')
            with Direction(placement='above'):
                with DirectionType():
                    Segno(default_x=-8.06, relative_y=20.0)
                Sound(segno='segno')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Menuet I.', relative_x=110.0, relative_y=50.0, font_weight='bold', font_size='14')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.36, default_y=22.72, relative_x=121.14, relative_y=60.0):
                        BeatUnit('quarter')
                        PerMinute('120')
                Sound(tempo=120.0)
            with Note(default_x=98.23, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=162.06, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(24.0)
            with Note(default_x=98.23, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=104.53, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('3')
                Type('half')
                Stem('up')
            with Forward():
                Duration(8.0)
        with Measure(number='2', width=180.99):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=43.57, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=73.1, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=102.63, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=132.15, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(4.0)
            with Note(default_x=18.3, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Forward():
                Duration(20.0)
        with Measure(number='3', width=144.68):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.33, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=92.66, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=117.87, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(16.0)
        with Measure(number='4', width=209.73):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.69, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=77.38, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=110.06, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=142.75, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=175.44, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(20.0)
        with Measure(number='5', width=117.45):
            with Note(default_x=12.36, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=76.18, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=18.66, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('3')
                Type('half')
                Stem('up')
            with Forward():
                Duration(8.0)
        with Measure(number='6', width=167.07):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.4, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=66.81, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=94.21, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=121.62, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(20.0)
        with Measure(number='7', width=145.94):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=56.11, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=100.22, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Forward():
                Duration(8.0)
            with Note(default_x=61.47, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.58, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.79, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note(default_x=102.9, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=138.41):
            with Note(default_x=20.67, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=26.03, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=23.35, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=244.32):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(76.91)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=105.13, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=163.27, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=196.28, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=219.55, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=105.13, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Forward():
                Duration(8.0)
        with Measure(number='10', width=204.08):
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=46.08, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=81.38, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=111.66, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=141.93, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=172.21, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(20.0)
        with Measure(number='11', width=133.85):
            with Note(default_x=12.72, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=52.56, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=92.41, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=12.36, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=92.41, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=207.72):
            with Note(default_x=15.8, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=47.52, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=79.24, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=110.96, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=142.68, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=174.4, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(20.0)
        with Measure(number='13', width=107.36):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=74.63, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=12.36, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=43.49, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=74.63, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=149.65):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=36.3, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=60.59, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=84.89, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=109.18, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(12.0)
            with Note(default_x=109.18, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(24.0)
            with Forward():
                Duration(16.0)
            with Note(default_x=111.86, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
        with Measure(number='15', width=150.37):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=53.79, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=77.54, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=101.28, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=125.03, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(8.0)
            with Note(default_x=18.48, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Forward():
                Duration(16.0)
        with Measure(number='16', width=160.22):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=36.44, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=60.87, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=85.31, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=109.74, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=134.18, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='17', width=183.9):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(102.83)
            with Note(default_x=89.22, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=146.64, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=89.22, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
        with Measure(number='18', width=188.18):
            with Note(default_x=16.2, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=46.62, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=77.05, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=107.47, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=137.9, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Backup():
                Duration(24.0)
            with Note(default_x=16.2, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
            with Forward():
                Duration(20.0)
        with Measure(number='19', width=157.77):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.99, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=102.18, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=129.17, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.99, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=102.18, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(24.0)
            with Note(default_x=18.48, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.67, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Forward():
                Duration(8.0)
        with Measure(number='20', width=194.82):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.37, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=74.94, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=104.51, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=134.08, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=163.65, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(4.0)
            with Note(default_x=18.48, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Forward():
                Duration(20.0)
        with Measure(number='21', width=157.97):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=62.66, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=109.51, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(8.0)
            with Note(default_x=109.51, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='22', width=164.1):
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=43.17, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=69.11, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=95.06, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=121.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Forward():
                Duration(12.0)
            with Note(default_x=121.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='23', width=150.09):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=39.57, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('(    )', default_y=39.81, relative_x=-10.0, relative_y=40.0)
            with Note(default_x=67.14, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=120.92, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(24.0)
            with Forward():
                Duration(8.0)
            with Note(default_x=67.14, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Forward():
                Duration(4.0)
        with Measure(number='24', width=160.74):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=17.36, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=14.68, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Words('To Coda', relative_y=20.0)
                Sound(tocoda='coda')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=274.57):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(50.0)
                        RightMargin(0.0)
                    SystemDistance(159.81)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Attributes():
                with Key():
                    Fifths(2)
                with Time():
                    Beats('3')
                    BeatType('4')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Menuet II.', relative_x=105.0, relative_y=50.0, font_weight='bold', font_size='14')
            with Note(default_x=137.02, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=175.86, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=200.14, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=224.41, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=248.69, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='26', width=113.51):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=45.3, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.61, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='27', width=131.53):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=34.68, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=57.36, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=93.64, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='28', width=167.56):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=37.66, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=63.32, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=88.98, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=114.64, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=140.3, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='29', width=180.67):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=39.84, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=67.69, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=95.53, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=123.38, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=151.22, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='30', width=167.56):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=37.66, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=63.32, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=88.98, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=114.64, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=140.3, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='31', width=167.56):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=38.16, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=64.32, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=100.28, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=126.44, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.79, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='32', width=104.62):
            with Direction(placement='above'):
                with DirectionType():
                    Words('(    )', default_y=39.81, relative_x=-10.0, relative_y=40.0)
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Backup():
                Duration(24.0)
            with Note(default_x=12.36, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=275.32):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(102.83)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=115.97, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=161.04, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=189.21, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=217.38, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=245.55, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='34', width=108.53):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.18, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.55, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='35', width=131.49):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=34.67, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=57.34, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=93.61, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=158.78):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=36.2, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=60.39, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=84.59, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=108.78, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=132.98, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='37', width=194.47):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=41.87, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=71.75, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=101.62, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=131.49, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=163.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='38', width=171.43):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=38.23, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=64.9, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=91.13, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=117.36, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=143.6, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='39', width=158.78):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=36.2, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=60.39, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=84.59, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=108.78, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=132.98, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='40', width=158.78):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=36.2, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=60.39, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=84.59, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=108.78, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=132.98, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='41', width=250.25):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(102.83)
            with Note(default_x=88.01, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=114.79, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=141.56, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=168.33, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=195.1, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=221.88, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='42', width=146.72):
            with Note(default_x=17.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=60.24, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=102.68, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='43', width=195.63):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=42.31, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=72.78, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=103.09, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=133.4, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=163.71, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='44', width=174.24):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.77, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=65.55, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=92.32, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=119.09, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=145.86, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='45', width=161.45):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=57.98, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=83.45, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=108.92, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=134.38, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='46', width=156.22):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=37.47, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=62.94, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=88.4, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=113.87, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='47', width=174.24):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.77, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=65.55, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=92.32, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=119.09, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=145.86, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='48', width=98.83):
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('<b><i>Menuet I.\nda Capo.</i></b>', default_y=19.67, relative_y=20.0)
                Sound(dalsegno='segno')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='0', implicit='yes', width=130.16):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(50.0)
                        RightMargin(0.0)
                    SystemDistance(152.25)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('3')
                    BeatType('8')
            with Direction(placement='above'):
                with DirectionType():
                    Coda(default_x=-13.61, relative_y=20.0)
                Sound(coda='coda')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-34.94, default_y=50.28, relative_x=73.79, relative_y=30.0):
                        BeatUnit('quarter')
                        BeatUnitDot()
                        PerMinute('66')
                Sound(tempo=99.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Gigue.', relative_x=60.0, relative_y=40.0, font_weight='bold', font_size='14')
            with Note(default_x=97.12, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='1', width=77.72):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.46, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='2', width=82.95):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=56.69, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='3', width=126.13):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.09, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=52.19, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=72.28, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=92.38, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=77.72):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.46, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='5', width=109.99):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=30.54, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=49.07, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=78.73, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='6', width=109.99):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=30.54, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=49.07, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=78.73, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=146.18):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.88, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.76, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.65, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=99.53, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.41, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='8', width=77.72):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=51.46, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='9', width=110.51):
            with Note(default_x=14.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.64, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=77.28, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='10', width=151.05):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=48.16, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=74.82, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=103.69, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=126.29, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='11', width=107.45):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=43.28, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=74.57, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='12', width=187.13):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(102.83)
            with Note(default_x=77.18, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=106.81, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=125.33, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=143.84, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.36, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='13', width=110.65):
            with Note(default_x=17.8, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=48.22, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=78.63, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='14', width=121.95):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=41.63, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=60.15, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.67, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.19, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='15', width=145.65):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=35.7, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.99, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.29, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=99.59, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=120.88, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='16', width=90.62):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=37.67, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=63.35, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='17', width=181.65):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=42.12, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.78, default_y=20.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=101.1, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.41, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.73, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='18', width=100.23):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=65.85, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=38.93, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=65.85, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='19', width=160.85):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=36.54, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=61.08, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.62, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.17, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.71, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='20', width=100.23):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=65.85, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=38.93, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=65.85, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=158.62):
            with Note(default_x=14.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=37.84, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=61.67, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=85.51, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=109.34, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=133.18, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=61.67, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=109.34, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='22', width=247.07):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(120.0)
            with Note(default_x=77.18, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=105.23, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=133.28, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=161.33, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=189.38, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=217.42, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=77.18, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=133.28, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=189.38, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='23', width=164.9):
            with Note(default_x=14.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.88, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=63.77, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=88.65, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=113.53, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=138.41, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=63.77, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=113.53, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='24', width=99.26):
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=66.18, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(4.0)
        with Measure(number='25', width=178.58):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=50.95, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=76.16, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=101.37, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=126.57, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=151.78, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(4.0)
            with Note(default_x=14.68, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Forward():
                Duration(8.0)
        with Measure(number='26', width=166.3):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.67, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=63.87, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=89.08, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.28, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=139.49, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(8.0)
        with Measure(number='27', width=166.3):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.67, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=63.87, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=89.08, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.28, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=139.49, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(8.0)
        with Measure(number='28', width=166.3):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.67, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=63.87, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=89.08, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.28, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=139.49, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(8.0)
        with Measure(number='29', width=168.86):
            with Note(default_x=17.23, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=59.58, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=86.05, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.53, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.79, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Forward():
                Duration(8.0)
        with Measure(number='30', width=246.99):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(102.83)
            with Note(default_x=80.98, default_y=-60.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.54, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=134.1, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.67, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=188.93, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=218.83, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='31', width=150.21):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=32.89, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=53.78, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=74.66, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.55, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=125.45, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='32', width=67.05):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X1', implicit='yes', width=56.96):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=24.95, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='33', width=73.32):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=48.56, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='34', width=73.32):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=48.56, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='35', width=124.12):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.74, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.47, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.21, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=90.94, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='36', width=73.32):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=48.56, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='37', width=146.98):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=32.89, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.78, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=74.66, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.55, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=122.22, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='38', width=135.98):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=31.84, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.69, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=71.53, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.37, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.22, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='39', width=135.98):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=31.84, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.69, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=71.53, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.37, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.22, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='40', width=73.32):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=48.56, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='41', width=221.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(102.83)
            with Note(default_x=89.22, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=110.71, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.2, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=153.69, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.18, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.67, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='42', width=144.22):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=33.49, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.98, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=76.47, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.96, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.45, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='43', width=163.04):
            with Note(default_x=17.23, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=40.28, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.32, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=92.19, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.23, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.28, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='44', width=144.22):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=33.49, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.98, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=76.47, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.96, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.45, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='45', width=180.59):
            with Note(default_x=16.2, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=41.26, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.31, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=96.21, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.26, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.93, default_y=20.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='46', width=110.47):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=44.29, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=76.58, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='47', width=157.81):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.87, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=63.91, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=86.96, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=110.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=133.05, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='48', width=89.57):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.2, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='49', width=146.22):
            with Note(default_x=14.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=35.49, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.98, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=78.47, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=99.96, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.45, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=14.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Forward():
                Duration(4.0)
        with Measure(number='50', width=215.78):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(102.83)
            with Note(default_x=77.18, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=99.94, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=122.71, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=145.48, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.24, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.01, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='51', width=150.6):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=34.77, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.53, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=80.3, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=103.07, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.83, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='52', width=95.95):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.58, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='53', width=150.6):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=34.77, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.53, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=80.3, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=103.07, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.83, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Forward():
                Duration(4.0)
        with Measure(number='54', width=150.6):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=34.77, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.53, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=80.3, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=103.07, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.83, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='55', width=150.6):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=34.77, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.53, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=80.3, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=103.07, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.83, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='56', width=89.86):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=60.39, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='57', width=176.59):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.67, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.56, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.17, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.77, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.38, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='58', width=177.0):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=37.94, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.88, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=97.58, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=123.52, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.46, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='59', width=222.0):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(102.83)
            with Note(default_x=77.18, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=101.05, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=124.92, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=148.79, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.66, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.53, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='60', width=162.06):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=41.1, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.97, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=88.84, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.72, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.59, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='61', width=169.48):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.95, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=65.54, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=91.13, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=116.71, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=142.3, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(4.0)
            with Note(default_x=14.68, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Forward():
                Duration(8.0)
        with Measure(number='62', width=156.83):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=35.87, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=59.74, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=83.61, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=107.48, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=131.36, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(8.0)
        with Measure(number='63', width=156.83):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=35.87, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=59.74, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=83.61, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=107.48, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=131.36, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(8.0)
        with Measure(number='64', width=156.83):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=35.87, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=59.74, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=83.61, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=107.48, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=131.36, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(8.0)
        with Measure(number='65', width=162.06):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.1, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=64.97, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.84, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.72, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.59, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='66', width=171.48):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.6, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=63.2, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.79, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.39, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=144.29, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='67', width=197.34):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=77.18, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=96.26, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=115.34, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.41, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=153.49, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.57, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='68', width=135.96):
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.88, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.96, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.04, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.11, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.19, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='69', width=136.36):
            with Note(default_x=16.2, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=35.28, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=54.36, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=73.44, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=92.51, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=111.59, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=16.2, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.36, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=92.51, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='70', width=132.16):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=31.08, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=50.16, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=69.24, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=88.31, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=107.39, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=50.16, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=88.31, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='71', width=136.36):
            with Note(default_x=16.2, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=35.28, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=54.36, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=73.44, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=92.51, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=111.59, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=16.2, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.36, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=92.51, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='72', width=126.99):
            with Note(default_x=29.83, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=70.16, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=102.23, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=29.83, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(8.0)
            with Note(default_x=32.51, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Forward():
                Duration(4.0)
        with Measure(number='73', width=132.16):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=31.08, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=50.16, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.24, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.31, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.39, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='74', width=152.19):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=43.9, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.78, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.66, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.54, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.42, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='75', width=139.76):
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.64, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.48, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.32, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.15, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.99, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='76', width=68.3):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')