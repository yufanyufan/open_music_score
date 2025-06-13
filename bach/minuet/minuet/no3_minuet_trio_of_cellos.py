with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Minuet No. 3')
    with Identification():
        Creator('Isaac Yung Lopes', type='arranger')
        Creator('J.S. Bach', type='composer')
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
        CreditWords('Minuet No. 3\n', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_weight='bold', font_size='24')
        CreditWords(None)
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J.S Bach\n', default_x=1134.19, default_y=1447.87, justify='right', valign='bottom', font_size='12')
        CreditWords(None)
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Isaac Yung Lopes\n', default_x=56.6929, default_y=1447.87, justify='left', valign='bottom', font_size='12')
        CreditWords(None)
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Trio of cellos', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Violoncelo', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Violoncelo')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(43)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Violoncelo', print_object='no')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Violoncelo')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(4)
                MidiProgram(43)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Violoncelo', print_object='no')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Violoncelo')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(7)
                MidiProgram(43)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=219.53):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(258.8)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=83.37, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        DownBow()
            with Note(default_x=121.81, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=145.84, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=169.87, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=193.9, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=120.88):
            with Note(default_x=10.94, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.57, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=77.6, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='3', width=120.88):
            with Note(default_x=10.94, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.57, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.08, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=77.6, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=96.12, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=128.12):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.95, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=83.88, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='5', width=120.88):
            with Note(default_x=10.94, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.57, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.08, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=77.6, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=96.12, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='6', width=124.11):
            with Note(default_x=14.16, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=43.79, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=62.31, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=80.82, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=99.34, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=124.11):
            with Note(default_x=14.16, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=43.79, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=62.31, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=80.82, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=99.34, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='8', width=118.97):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=38.71, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=84.6, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
        with Measure(number='9', width=202.93):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(164.59)
            with Note(default_x=62.31, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        DownBow()
            with Note(default_x=102.03, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=126.85, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=151.68, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=176.5, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='10', width=125.33):
            with Note(default_x=10.94, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.11, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=81.08, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='11', width=125.33):
            with Note(default_x=10.94, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.11, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=61.6, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=81.08, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=100.57, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=132.57):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.5, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=87.37, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='13', width=125.33):
            with Note(default_x=10.94, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.11, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=61.6, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=81.08, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=100.57, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='14', width=128.56):
            with Note(default_x=14.16, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=45.34, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=64.82, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=84.31, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=103.79, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=128.56):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=30.76)
            with Note(default_x=14.16, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=45.34, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=64.82, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=84.31, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=103.79, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='16', width=108.88):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='17', width=163.6):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(164.59)
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=30.0)
            with Note(default_x=62.31, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.93, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=105.56, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=65.81)
            with Note(default_x=122.2, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=138.83, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='18', width=95.77):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue')
        with Measure(number='19', width=165.55):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=29.3, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        DownBow()
            with Note(default_x=67.77, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=91.82, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=115.86, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=139.91, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='20', width=115.09):
            with Note(default_x=13.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.42, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.05, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
            with Note(default_x=73.69, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=90.32, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=123.83):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.31, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=61.78, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=81.24, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=99.06, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='22', width=118.52):
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=43.85, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=60.48, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=77.12, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='23', width=149.47):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=34.05, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=63.95, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=84.2, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=104.45, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=124.7, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='24', width=145.68):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.02, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=97.55, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='25', width=184.01):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    TopSystemDistance(85.0)
            with Note(default_x=62.31, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=95.05, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=41.16)
            with Note(default_x=138.78, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='26', width=103.07):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=10.36, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='27', width=141.37):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.94, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Technical():
                        DownBow()
            with Note(default_x=47.33, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=70.6, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=93.86, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='28', width=132.63):
            with Note(default_x=10.94, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=43.68, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=66.94, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=87.41, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='29', width=119.52):
            with Note(default_x=10.94, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.09, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
            with Note(default_x=76.54, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='30', width=140.76):
            with Note(default_x=14.16, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=34.53, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=54.9, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=75.26, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=95.63, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='31', width=136.6):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=30.37, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=50.73, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=71.1, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=91.47, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=111.84, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='32', width=119.52):
            with Note(default_x=10.94, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.09, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.54, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='33', width=318.77):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(170.0)
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=48.5)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=62.31, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=104.79, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=30.0)
            with Note(default_x=147.26, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=232.21, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='34', width=269.37):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='35', width=256.44):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=48.5)
            with Note(default_x=14.16, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=60.44, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=106.73, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=180.78, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='36', width=232.93):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=0.65, relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='2', type='discontinue')
    with Part(id='P2'):
        with Measure(number='1', width=219.53):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(80.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=83.0, default_y=-160.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='2', width=120.88):
            with Note(default_x=10.58, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='3', width=120.88):
            with Note(default_x=10.58, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='4', width=128.12):
            with Note(default_x=13.44, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='5', width=120.88):
            with Note(default_x=10.58, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='6', width=124.11):
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='7', width=124.11):
            with Note(default_x=13.8, default_y=-175.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='8', width=118.97):
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=38.71, default_y=-175.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=84.6, default_y=-175.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='9', width=202.93):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(80.0)
            with Note(default_x=61.95, default_y=-160.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='10', width=125.33):
            with Note(default_x=10.58, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='11', width=125.33):
            with Note(default_x=10.58, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='12', width=132.57):
            with Note(default_x=13.44, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='13', width=125.33):
            with Note(default_x=10.58, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='14', width=128.56):
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='15', width=128.56):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=30.76)
            with Note(default_x=13.8, default_y=-175.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='16', width=108.88):
            with Note(default_x=13.8, default_y=-180.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='17', width=163.6):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(80.0)
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=30.0)
            with Note(default_x=61.95, default_y=-175.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='18', width=95.77):
            with Note(default_x=13.8, default_y=-180.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue')
        with Measure(number='19', width=165.55):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=28.94, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='20', width=115.09):
            with Note(default_x=13.44, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='21', width=123.83):
            with Note(default_x=13.44, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='22', width=118.52):
            with Note(default_x=16.87, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
        with Measure(number='23', width=149.47):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=13.8, default_y=-175.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=63.95, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=104.45, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='24', width=145.68):
            with Note(default_x=13.44, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='25', width=184.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(80.0)
            with Note(default_x=61.95, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='26', width=103.07):
            with Note(default_x=10.36, default_y=-160.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='27', width=141.37):
            with Note(default_x=10.58, default_y=-160.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='28', width=132.63):
            with Note(default_x=10.58, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='29', width=119.52):
            with Note(default_x=10.58, default_y=-160.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='30', width=140.76):
            with Note(default_x=13.8, default_y=-175.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='31', width=136.6):
            with Note(default_x=10.0, default_y=-160.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=50.73, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=91.47, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='32', width=119.52):
            with Note(default_x=10.58, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='33', width=318.77):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(83.53)
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=48.5)
            with Note(default_x=61.95, default_y=-183.53):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
        with Measure(number='34', width=269.37):
            with Note(default_x=13.8, default_y=-183.53):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='35', width=256.44):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=48.5)
            with Note(default_x=13.8, default_y=-183.53):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=13.8, default_y=-163.53):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='36', width=232.93):
            with Note(default_x=13.8, default_y=-183.53):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=13.8, default_y=-163.53):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='2', type='discontinue')
    with Part(id='P3'):
        with Measure(number='1', width=219.53):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(80.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Sound(dynamics=71.11)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=121.81, default_y=-230.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=145.84, default_y=-225.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=169.87, default_y=-220.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=193.9, default_y=-215.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='2', width=120.88):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=40.57, default_y=-255.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.08, default_y=-250.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=77.6, default_y=-245.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=96.12, default_y=-240.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='3', width=120.88):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=40.57, default_y=-250.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.08, default_y=-245.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=77.6, default_y=-240.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=96.12, default_y=-235.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='4', width=128.12):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=44.95, default_y=-230.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=64.42, default_y=-235.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=83.88, default_y=-240.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=103.35, default_y=-245.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='5', width=120.88):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=40.57, default_y=-235.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.08, default_y=-240.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=77.6, default_y=-245.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=96.12, default_y=-250.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='6', width=124.11):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=43.79, default_y=-250.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=62.31, default_y=-255.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=80.82, default_y=-260.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=99.34, default_y=-265.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='7', width=124.11):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=43.79, default_y=-275.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=62.31, default_y=-270.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=80.82, default_y=-265.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=99.34, default_y=-260.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='8', width=118.97):
            with Note(default_x=13.8, default_y=-220.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=38.71, default_y=-225.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=84.6, default_y=-225.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
        with Measure(number='9', width=202.93):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(80.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=102.03, default_y=-230.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=126.85, default_y=-225.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=151.68, default_y=-220.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=176.5, default_y=-215.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='10', width=125.33):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=42.11, default_y=-255.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=61.6, default_y=-250.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=81.08, default_y=-245.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=100.57, default_y=-240.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='11', width=125.33):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=42.11, default_y=-250.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=61.6, default_y=-245.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=81.08, default_y=-240.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=100.57, default_y=-235.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='12', width=132.57):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=46.5, default_y=-230.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=66.93, default_y=-235.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=87.37, default_y=-240.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=107.8, default_y=-245.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='13', width=125.33):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=42.11, default_y=-235.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=61.6, default_y=-240.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=81.08, default_y=-245.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=100.57, default_y=-250.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='14', width=128.56):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=45.34, default_y=-250.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=64.82, default_y=-255.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=84.31, default_y=-260.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=103.79, default_y=-265.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='15', width=128.56):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=30.76)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=45.34, default_y=-245.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=64.82, default_y=-250.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=84.31, default_y=-255.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=103.79, default_y=-260.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='16', width=108.88):
            with Note(default_x=13.8, default_y=-230.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='17', width=163.6):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(85.3)
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=30.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=88.93, default_y=-250.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=105.56, default_y=-255.3):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=122.2, default_y=-260.3):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=138.83, default_y=-265.3):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='18', width=95.77):
            with Note(default_x=13.8, default_y=-235.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue')
        with Measure(number='19', width=165.55):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=67.77, default_y=-250.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=91.82, default_y=-245.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=115.86, default_y=-240.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=139.91, default_y=-235.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=115.09):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=40.42, default_y=-255.3):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.05, default_y=-250.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=73.69, default_y=-245.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=90.32, default_y=-240.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='21', width=123.83):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=42.31, default_y=-235.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=61.78, default_y=-240.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=81.24, default_y=-245.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=99.06, default_y=-250.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='22', width=118.52):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=43.85, default_y=-245.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=60.48, default_y=-250.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=77.12, default_y=-255.3):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=93.75, default_y=-260.3):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='23', width=149.47):
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=30.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=13.8, default_y=-265.3):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=34.05, default_y=-260.3):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=63.95, default_y=-255.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=84.2, default_y=-250.3):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=104.45, default_y=-245.3):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=124.7, default_y=-240.3):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='24', width=145.68):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=51.02, default_y=-220.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=74.28, default_y=-225.3):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=97.55, default_y=-230.3):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=120.82, default_y=-235.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='25', width=184.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(80.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=95.05, default_y=-225.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=118.31, default_y=-230.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=138.78, default_y=-235.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=159.24, default_y=-240.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='26', width=103.07):
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=30.0)
            with Note(default_x=10.36, default_y=-245.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
        with Measure(number='27', width=141.37):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=47.33, default_y=-220.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=70.6, default_y=-225.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=93.86, default_y=-230.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=116.61, default_y=-235.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=132.63):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=43.68, default_y=-225.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=66.94, default_y=-230.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=87.41, default_y=-235.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=107.87, default_y=-240.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='29', width=119.52):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=40.09, default_y=-240.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=58.31, default_y=-245.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=76.54, default_y=-250.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=94.76, default_y=-255.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='30', width=140.76):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=54.9, default_y=-260.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=75.26, default_y=-265.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=95.63, default_y=-270.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=116.0, default_y=-275.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='31', width=136.6):
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=30.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=10.0, default_y=-280.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=30.37, default_y=-275.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=50.73, default_y=-270.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=71.1, default_y=-265.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=91.47, default_y=-260.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=111.84, default_y=-255.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='32', width=119.52):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=40.09, default_y=-235.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=58.31, default_y=-240.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=76.54, default_y=-245.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=94.76, default_y=-250.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='33', width=318.77):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(106.2)
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=48.5)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=147.26, default_y=-274.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=189.74, default_y=-279.73):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=232.21, default_y=-284.73):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=274.69, default_y=-289.73):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='34', width=269.37):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=81.83, default_y=-279.73):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=124.12, default_y=-284.73):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=166.42, default_y=-289.73):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=208.71, default_y=-294.73):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='35', width=256.44):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=48.5)
            with Note(default_x=14.16, default_y=-254.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=60.44, default_y=-244.73):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=106.73, default_y=-259.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=180.78, default_y=-264.73):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='36', width=232.93):
            with Note(default_x=13.8, default_y=-259.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', default_y=11.33, relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='2', type='discontinue')