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
            Millimeters(5.72)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2076.92)
            PageWidth(1468.53)
            with PageMargins(type='both'):
                LeftMargin(69.9301)
                RightMargin(69.9301)
                TopMargin(69.9301)
                BottomMargin(69.9301)
        WordFont(font_family='FreeSerif', font_size='14')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('GOLDBERG-VARIATIONEN, BWV988', default_x=734.265, default_y=2006.99, justify='center', valign='top', font_weight='bold', font_style='italic', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('ARIA MIT VERSCHIEDENEN VERAGNDRUNGEN\n', default_x=734.265, default_y=1937.06, justify='center', valign='top', font_style='italic', font_family='Times New Roman')
        CreditWords('3 Recoders(Aria) and 2 Recorders(Variation 1)')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach (1685-1750)\n', default_x=1398.6, default_y=1793.96, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
        CreditWords('Arr: Jan Kok')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Soprano Rec.')
            PartAbbreviation('S.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Soprano Recorder')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(75)
                Volume(78.7402)
                Pan(-90.0)
        with ScorePart(id='P2'):
            PartName('Tenor Rec.')
            PartAbbreviation('T.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Tenor Recorder')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(75)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Bass Rec.')
            PartAbbreviation('B.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Bass Recorder')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(75)
                Volume(78.7402)
                Pan(90.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=231.9):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(146.2)
                        RightMargin(-0.0)
                    TopSystemDistance(322.01)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('0. Aria', default_x=-36.94, relative_x=-34.0, relative_y=36.9, font_weight='bold', font_family='Times New Roman', font_size='14.9991')
                Sound(tempo=72.0)
            with Note(default_x=101.61, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=138.16, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=174.72, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Ornaments():
                        Mordent()
            with Note(default_x=207.13, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='2', width=178.11):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=33.22, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(6)
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=51.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=69.09, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(6)
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=87.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=132.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
        with Measure(number='3', width=162.92):
            with Note(default_x=12.94, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        Mordent()
            with Note(default_x=52.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Ornaments():
                        InvertedMordent(long='yes', approach='above')
            with Note(default_x=120.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='4', width=238.59):
            with Note(default_x=12.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=28.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=44.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=67.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=82.76, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=98.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=115.84, default_y=-40.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=134.3, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=174.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='5', width=151.08):
            with Note(default_x=12.94, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=52.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=91.48, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Ornaments():
                        Mordent()
            with Note(default_x=126.31, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='6', width=219.87):
            with Note(default_x=12.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=30.35, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(6)
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=48.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=66.23, default_y=-20.0):
                Grace()
                with Pitch():
                    Step('B')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=84.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=118.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=184.87, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Ornaments():
                        InvertedTurn()
        with Measure(number='7', width=379.59):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(38.15)
                        RightMargin(-0.0)
                    SystemDistance(113.76)
            with Note(default_x=79.73, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=95.4, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.31, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=144.78, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=174.7, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=190.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=235.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=261.39, default_y=-15.0):
                Grace()
                with Pitch():
                    Step('C')
                    Octave(6)
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=279.85, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=353.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='8', width=204.84):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=27.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=53.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=70.62, default_y=-35.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=89.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=146.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='9', width=139.28):
            with Note(default_x=12.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=48.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=83.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Ornaments():
                        Mordent()
            with Note(default_x=114.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='10', width=198.28):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=90.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(32.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='11', width=199.57):
            with Note(default_x=12.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=28.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=45.32, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=61.92, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=78.52, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Ornaments():
                        InvertedMordent(long='yes', approach='above')
            with Note(default_x=158.2, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=168.97):
            with Note(default_x=17.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=41.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=71.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Ornaments():
                        InvertedMordent(long='yes', approach='above')
            with Note(default_x=143.32, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='13', width=300.27):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(38.15)
                        RightMargin(-0.0)
                    SystemDistance(113.76)
            with Note(default_x=83.41, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=103.2, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=122.98, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=162.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=189.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=244.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=259.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=275.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='14', width=273.67):
            with Note(default_x=12.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=34.41, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=55.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=98.81, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=125.84, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(6)
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=158.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=217.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=233.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=248.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='15', width=223.87):
            with Note(default_x=12.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=60.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=79.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.62, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=126.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=192.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='16', width=260.56):
            with Note(default_x=24.37, default_y=-15.0):
                Grace()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=42.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=70.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=85.87, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=101.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=117.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=134.62, default_y=-15.0):
                Grace()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=153.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=207.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=232.15):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=25.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=84.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    with Ornaments():
                        InvertedMordent(long='yes', approach='above')
            with Note(default_x=123.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=144.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=160.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=176.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=191.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=207.39, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='18', width=280.17):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(38.15)
                        RightMargin(-0.0)
                    SystemDistance(113.76)
            with Note(default_x=79.61, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(6)
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=98.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=115.49, default_y=-15.0):
                Grace()
                with Pitch():
                    Step('C')
                    Octave(6)
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=133.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=151.36, default_y=-25.0):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=169.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=197.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=251.38, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='19', width=302.55):
            with Note(default_x=13.75, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=32.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=73.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=103.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=121.11, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=139.55, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Ornaments():
                        Mordent()
            with Note(default_x=211.78, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=235.05, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=258.31, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=277.78, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='20', width=198.55):
            with Note(default_x=17.23, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.6, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=73.01, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(6)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=105.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=173.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='21', width=246.84):
            with Note(default_x=12.72, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        InvertedMordent(long='yes', approach='above')
            with Note(default_x=54.89, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=72.3, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=90.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=139.57, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=157.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=190.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=206.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=222.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='22', width=262.42):
            with Note(default_x=12.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=28.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.79, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=81.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.14, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=125.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=179.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=198.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.65, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=293.6):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(38.15)
                        RightMargin(-0.0)
                    SystemDistance(113.76)
            with Note(default_x=79.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=126.49, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=143.91, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(6)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=176.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=205.45, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        InvertedMordent(long='yes', approach='below')
            with Note(default_x=234.3, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=263.15, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='24', width=259.51):
            with Note(default_x=13.75, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=32.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=80.34, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=110.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=127.65, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=146.09, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='25', width=168.17):
            with Note(default_x=12.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=39.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=65.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=127.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=143.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='26', width=287.12):
            with Note(default_x=12.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=28.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=43.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=81.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=97.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=239.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=262.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=282.11):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=100.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=145.25, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=189.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='28', width=298.29):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(38.15)
                        RightMargin(-0.0)
                    TopSystemDistance(60.0)
            with Note(default_x=79.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=97.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.5, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=150.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=167.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=220.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=238.27, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=230.68):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=47.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.89, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=82.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=100.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=117.77, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.4, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=153.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=170.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='30', width=258.18):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.67, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.3, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=93.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=111.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.25, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=166.88, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=185.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.1, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=233.42, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=234.48):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=86.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=103.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=156.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='32', width=218.81):
            with Note(default_x=13.06, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=79.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=95.67, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=146.13, default_y=-35.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=164.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X1', implicit='yes', width=50.07):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('64th')
            with Barline(location='right'):
                BarStyle('none')
        with Measure(number='1', width=360.05):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(146.2)
                        RightMargin(-0.0)
                    SystemDistance(97.1)
            with Attributes():
                Divisions(16.0)
                with Time():
                    Beats('3')
                    BeatType('4')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Variation 1', default_x=-36.0, relative_x=-14.56, relative_y=26.6, font_weight='bold', font_family='Times New Roman', font_size='12')
                Sound(tempo=90.0)
            with Note(default_x=100.67, default_y=-30.0, dynamics=81.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.14, default_y=-35.0, dynamics=81.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=141.61, default_y=-30.0, dynamics=87.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=182.56, default_y=-30.0, dynamics=87.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=203.03, default_y=-45.0, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=223.5, default_y=-40.0, dynamics=85.56):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=243.97, default_y=-35.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=264.44, default_y=-30.0, dynamics=90.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=284.91, default_y=-25.0, dynamics=91.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.38, default_y=-20.0, dynamics=87.78):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=335.28, default_y=-15.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='2', width=271.38):
            with Note(default_x=12.0, default_y=-10.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.9, default_y=-15.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=62.37, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=103.31, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=123.78, default_y=-25.0, dynamics=70.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.25, default_y=-20.0, dynamics=91.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.73, default_y=-15.0, dynamics=91.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=185.2, default_y=-10.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=205.67, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.14, default_y=0.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=246.61, default_y=-10.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='3', width=271.38):
            with Note(default_x=12.0, default_y=5.0, dynamics=95.56):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.47, default_y=0.0, dynamics=85.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=52.94, default_y=5.0, dynamics=90.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=93.89, default_y=5.0, dynamics=90.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=114.36, default_y=0.0, dynamics=82.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.83, default_y=-5.0, dynamics=74.44):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.3, default_y=-10.0, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=185.2, default_y=-15.0, dynamics=84.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=205.67, default_y=-5.0, dynamics=92.22):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.14, default_y=-25.0, dynamics=67.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=246.61, default_y=-30.0, dynamics=76.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='4', width=279.66):
            with Note(default_x=12.0, default_y=-35.0, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.92, default_y=-40.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.84, default_y=-45.0, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.54, default_y=-50.0, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=108.46, default_y=-45.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.38, default_y=-35.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.3, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.22, default_y=-30.0, dynamics=78.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=192.14, default_y=-35.0, dynamics=83.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=213.06, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=233.98, default_y=-45.0, dynamics=68.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='5', width=300.1):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(38.15)
                        RightMargin(-0.0)
                    SystemDistance(97.1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=115.29, default_y=-10.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=133.08, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=150.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=186.42, default_y=-30.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=221.98, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=257.55, default_y=-10.0, dynamics=95.56):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='6', width=236.62):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=48.17, default_y=-5.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=66.2, default_y=-10.0, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=84.23, default_y=-5.0, dynamics=90.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=120.28, default_y=-25.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=156.34, default_y=-50.0, dynamics=67.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=193.83, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='7', width=260.42):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=60.88, default_y=0.0, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=79.74, default_y=-5.0, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=98.61, default_y=0.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=136.33, default_y=-10.0, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=179.06, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=216.79, default_y=-15.0, dynamics=70.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='8', width=244.79):
            with Note(default_x=12.0, default_y=-15.0, dynamics=70.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=49.41, default_y=-20.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=107.04, default_y=-30.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.74, default_y=-20.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.45, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=163.15, default_y=5.0, dynamics=95.56):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=181.86, default_y=-10.0, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.56, default_y=5.0, dynamics=96.67):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.02, default_y=10.0, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='9', width=248.59):
            with Note(default_x=15.8, default_y=15.0, dynamics=91.11):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.27, default_y=5.0, dynamics=76.67):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.97, default_y=-10.0, dynamics=67.78):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=72.67, default_y=-20.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=91.38, default_y=-30.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=110.08, default_y=-20.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.78, default_y=-10.0, dynamics=92.22):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.49, default_y=5.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=166.95, default_y=15.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.42, default_y=5.0, dynamics=76.67):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.12, default_y=0.0, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=223.82, default_y=-5.0, dynamics=74.44):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='10', width=321.84):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(38.15)
                        RightMargin(-0.0)
                    SystemDistance(97.1)
            with Note(default_x=83.41, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=101.79, default_y=-5.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=131.69, default_y=-15.0, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.06, default_y=-25.0, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=168.44, default_y=-35.0, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.81, default_y=-25.0, dynamics=92.22):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.19, default_y=-15.0, dynamics=96.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=223.57, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=241.94, default_y=10.0, dynamics=95.56):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=260.32, default_y=0.0, dynamics=77.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.7, default_y=-5.0, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.07, default_y=-10.0, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='11', width=234.91):
            with Note(default_x=12.0, default_y=5.0, dynamics=91.11):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.01, default_y=-10.0, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=48.03, default_y=-20.0, dynamics=73.33):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.04, default_y=-30.0, dynamics=76.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=84.05, default_y=-40.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=102.07, default_y=-30.0, dynamics=87.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=120.08, default_y=-20.0, dynamics=92.22):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.09, default_y=-10.0, dynamics=91.11):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=156.11, default_y=5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.12, default_y=0.0, dynamics=82.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.13, default_y=-5.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.15, default_y=-10.0, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=259.8):
            with Note(default_x=17.23, default_y=-15.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.64, default_y=-30.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.05, default_y=-40.0, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.75, default_y=-50.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=106.16, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=124.57, default_y=-50.0, dynamics=76.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.98, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.39, default_y=-30.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=179.8, default_y=-15.0, dynamics=96.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=198.21, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=216.62, default_y=-10.0, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.03, default_y=-15.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='13', width=234.91):
            with Note(default_x=12.0, default_y=-10.0, dynamics=95.56):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=48.03, default_y=-45.0, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=66.04, default_y=-35.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=84.05, default_y=-25.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=102.07, default_y=-35.0, dynamics=83.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=120.08, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=156.11, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=192.13, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='14', width=239.06):
            with Note(default_x=12.0, default_y=-20.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=48.56, default_y=-45.0, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=66.85, default_y=-30.0, dynamics=92.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=85.13, default_y=-20.0, dynamics=91.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=103.41, default_y=-30.0, dynamics=70.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=121.69, default_y=-20.0, dynamics=87.78):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=159.44, default_y=-5.0, dynamics=96.67):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=196.01, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=370.8):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(38.15)
                        RightMargin(-0.0)
                    SystemDistance(97.1)
            with Note(default_x=91.65, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=114.78, default_y=-5.0, dynamics=90.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.9, default_y=-25.0, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.03, default_y=-30.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=184.16, default_y=-35.0, dynamics=78.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.28, default_y=-25.0, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.41, default_y=-10.0, dynamics=96.67):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.53, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=276.66, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=299.79, default_y=-5.0, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=322.91, default_y=-10.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=346.04, default_y=-15.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='16', width=299.67):
            with Note(default_x=12.0, default_y=0.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.14, default_y=-10.0, dynamics=74.44):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.04, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.18, default_y=-20.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=117.33, default_y=-25.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.47, default_y=-30.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.62, default_y=-35.0, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.31, default_y=-40.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=226.46, default_y=-45.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=328.9):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=24.89, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=50.09, default_y=5.0, dynamics=95.56):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=75.3, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=125.7, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=150.9, default_y=15.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.1, default_y=10.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.3, default_y=5.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=226.5, default_y=0.0, dynamics=84.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=251.7, default_y=-5.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.9, default_y=-10.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.1, default_y=-15.0, dynamics=74.44):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='18', width=291.15):
            with Note(default_x=12.0, default_y=-20.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.13, default_y=-15.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=58.25, default_y=-10.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=104.5, default_y=-10.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=127.63, default_y=-5.0, dynamics=90.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.76, default_y=-10.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.88, default_y=-15.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=197.01, default_y=-20.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=220.13, default_y=-25.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=243.26, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.38, default_y=-35.0, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='19', width=377.79):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(38.15)
                        RightMargin(-0.0)
                    SystemDistance(97.1)
            with Note(default_x=79.61, default_y=-40.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=109.51, default_y=-30.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.19, default_y=-25.0, dynamics=87.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.87, default_y=-20.0, dynamics=95.56):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.55, default_y=-25.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=204.22, default_y=-40.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.9, default_y=-25.0, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.58, default_y=-20.0, dynamics=86.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=275.26, default_y=-15.0, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=298.94, default_y=-25.0, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=328.83, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=352.51, default_y=-5.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='20', width=302.68):
            with Note(default_x=12.0, default_y=0.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.9, default_y=-5.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.8, default_y=-10.0, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.7, default_y=-15.0, dynamics=76.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=117.24, default_y=-20.0, dynamics=87.78):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='21', width=301.9):
            with Note(default_x=12.0, default_y=-20.0, dynamics=87.78):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=41.9, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=64.71, default_y=-5.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=110.34, default_y=-5.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=140.24, default_y=-45.0, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=163.05, default_y=-40.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=208.68, default_y=-40.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=231.5, default_y=-10.0, dynamics=105.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=254.31, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='22', width=308.15):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=37.02, default_y=5.0, dynamics=76.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=60.98, default_y=10.0, dynamics=91.11):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=108.91, default_y=10.0, dynamics=91.11):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=138.81, default_y=-30.0, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=162.77, default_y=-25.0, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=210.7, default_y=-25.0, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=234.66, default_y=5.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=258.62, default_y=10.0, dynamics=91.11):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='23', width=329.43):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(38.15)
                        RightMargin(-0.0)
                    SystemDistance(97.1)
            with Note(default_x=91.65, default_y=10.0, dynamics=91.11):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=109.96, default_y=-20.0, dynamics=65.56):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.28, default_y=-15.0, dynamics=82.22):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.59, default_y=-35.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=164.9, default_y=-20.0, dynamics=92.22):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=194.8, default_y=-45.0, dynamics=67.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=213.11, default_y=-40.0, dynamics=82.22):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=231.42, default_y=-30.0, dynamics=87.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=249.73, default_y=-35.0, dynamics=83.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=268.04, default_y=-40.0, dynamics=74.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.35, default_y=-45.0, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=304.66, default_y=-25.0, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=249.78):
            with Note(default_x=12.0, default_y=-30.0, dynamics=78.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.31, default_y=-35.0, dynamics=78.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=48.62, default_y=-40.0, dynamics=81.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.52, default_y=-45.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=96.83, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=115.14, default_y=-30.0, dynamics=92.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.45, default_y=-20.0, dynamics=92.22):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.77, default_y=-25.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=170.08, default_y=-30.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=188.39, default_y=-20.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=206.7, default_y=-40.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='25', width=234.38):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=48.03, default_y=-5.0, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=83.94, default_y=-15.0, dynamics=76.67):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=119.85, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=155.75, default_y=10.0, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=191.66, default_y=-25.0, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='26', width=242.67):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=49.2, default_y=-10.0, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=87.2, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=125.21, default_y=-10.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=162.28, default_y=5.0, dynamics=91.11):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=199.36, default_y=-30.0, dynamics=62.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='27', width=234.26):
            with Note(default_x=12.0, default_y=-15.0, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.95, default_y=-25.0, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=47.91, default_y=-40.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.86, default_y=-50.0, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=83.82, default_y=-25.0, dynamics=105.56):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=101.77, default_y=-50.0, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.73, default_y=-40.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.68, default_y=-25.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=155.64, default_y=-15.0, dynamics=96.67):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=173.59, default_y=-25.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.54, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.5, default_y=-5.0, dynamics=95.56):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=308.29):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(38.15)
                        RightMargin(-0.0)
                    SystemDistance(97.1)
            with Note(default_x=79.61, default_y=0.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=98.15, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=116.69, default_y=-25.0, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.22, default_y=-35.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=153.76, default_y=-45.0, dynamics=68.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=172.3, default_y=-35.0, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.84, default_y=-25.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.37, default_y=-15.0, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=227.91, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=246.45, default_y=-15.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.98, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=283.52, default_y=10.0, dynamics=95.56):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=274.78):
            with Note(default_x=15.8, default_y=15.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.1, default_y=5.0, dynamics=76.67):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.4, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.69, default_y=-20.0, dynamics=75.56):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=96.99, default_y=-30.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=117.29, default_y=-20.0, dynamics=90.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.59, default_y=-10.0, dynamics=95.56):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.88, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=178.18, default_y=15.0, dynamics=96.67):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=206.45, default_y=0.0, dynamics=78.89):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.74, default_y=15.0, dynamics=102.22):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=250.01, default_y=25.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='30', width=257.24):
            with Note(default_x=12.0, default_y=-5.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.33, default_y=25.0, dynamics=105.56):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.59, default_y=20.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.92, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=93.25, default_y=-10.0, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.57, default_y=20.0, dynamics=108.89):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.84, default_y=15.0, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.17, default_y=-10.0, dynamics=67.78):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=174.49, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=193.82, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=213.15, default_y=0.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=232.48, default_y=5.0, dynamics=90.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=244.47):
            with Note(default_x=15.8, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.34, default_y=-15.0, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=52.87, default_y=-20.0, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.41, default_y=-25.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=89.95, default_y=-20.0, dynamics=87.78):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=108.49, default_y=-10.0, dynamics=91.11):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.02, default_y=-20.0, dynamics=76.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=145.56, default_y=-30.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=164.1, default_y=-15.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=182.63, default_y=-25.0, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.17, default_y=-30.0, dynamics=80.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.71, default_y=-35.0, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='32', width=205.74):
            with Note(default_x=12.0, default_y=-20.0, dynamics=96.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.24, default_y=5.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=46.48, default_y=0.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.72, default_y=-5.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=80.96, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=98.2, default_y=-15.0, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.44, default_y=-20.0, dynamics=76.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.68, default_y=-25.0, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=149.92, default_y=-30.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P2'):
        with Measure(number='1', width=231.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(50.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=138.16, default_y=-110.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=174.72, default_y=-100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=178.11):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=87.55, default_y=-115.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=132.03, default_y=-100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=162.92):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=52.29, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=91.65, default_y=-105.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='4', width=238.59):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=134.3, default_y=-125.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=174.23, default_y=-115.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='5', width=151.08):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=52.21, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=91.48, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=219.87):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=84.69, default_y=-130.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=151.48, default_y=-115.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='7', width=379.59):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(50.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=125.31, default_y=-105.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=174.7, default_y=-105.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=279.85, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=304.39, default_y=-125.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=328.92, default_y=-130.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=353.46, default_y=-125.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='8', width=204.84):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.2, default_y=-115.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=88.72, default_y=-110.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='9', width=139.28):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=48.12, default_y=-110.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.31, default_y=-95.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=198.28):
            with Note(default_x=12.0, default_y=-115.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=90.93, default_y=-100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=199.57):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=45.32, default_y=-110.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=78.52, default_y=-95.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=158.2, default_y=-100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='12', width=168.97):
            with Note(default_x=17.23, default_y=-105.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=41.28, default_y=-100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=70.81, default_y=-95.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='13', width=300.27):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(50.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=162.56, default_y=-115.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=216.97, default_y=-100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=273.67):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=98.81, default_y=-110.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=188.05, default_y=-95.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=223.87):
            with Note(default_x=12.72, default_y=-90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=97.62, default_y=-95.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=145.28, default_y=-90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=163.61, default_y=-85.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='16', width=260.56):
            with Note(default_x=42.83, default_y=-85.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=152.7, default_y=-90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=232.15):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=55.12, default_y=-95.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=84.63, default_y=-90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='18', width=280.17):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(50.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=133.95, default_y=-105.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=169.45, default_y=-100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='19', width=302.55):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=56.29, default_y=-95.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=139.55, default_y=-85.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=187.71, default_y=-90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=211.78, default_y=-95.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='20', width=198.55):
            with Note(default_x=17.23, default_y=-100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=39.93, default_y=-95.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=105.33, default_y=-90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='21', width=246.84):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=37.13, default_y=-115.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=90.74, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    with Ornaments():
                        InvertedMordent(long='yes')
            with Note(default_x=115.16, default_y=-125.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=139.57, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='22', width=262.42):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=51.79, default_y=-115.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=125.58, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    with Ornaments():
                        InvertedMordent(long='yes')
            with Note(default_x=152.38, default_y=-125.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=179.18, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=218.16, default_y=-110.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='23', width=293.6):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(50.0)
            with Note(default_x=79.61, default_y=-125.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=205.45, default_y=-105.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=234.3, default_y=-110.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=263.15, default_y=-115.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='24', width=259.51):
            with Note(default_x=32.21, default_y=-115.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=146.09, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='25', width=168.17):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=65.12, default_y=-130.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=101.0, default_y=-115.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='26', width=287.12):
            with Note(default_x=12.36, default_y=-115.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=66.06, default_y=-125.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=119.76, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=150.52, default_y=-130.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=172.88, default_y=-125.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=195.25, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=217.62, default_y=-125.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=239.99, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='27', width=282.11):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=56.42, default_y=-130.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=100.83, default_y=-115.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=145.25, default_y=-95.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=189.66, default_y=-95.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=211.87, default_y=-75.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.14, default_y=-80.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=257.35, default_y=-85.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=298.29):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(50.0)
            with Note(default_x=79.61, default_y=-90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=185.38, default_y=-90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='29', width=230.68):
            with Note(default_x=12.0, default_y=-85.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=117.77, default_y=-100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=170.66, default_y=-85.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='30', width=258.18):
            with Note(default_x=12.0, default_y=-85.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=130.25, default_y=-85.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=185.2, default_y=-70.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=234.48):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=218.81):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=29.58, default_y=-105.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=46.1, default_y=-110.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.62, default_y=-115.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=79.15, default_y=-110.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=164.57, default_y=-110.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X1', implicit='yes', width=50.07):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('64th')
            with Barline(location='right'):
                BarStyle('none')
        with Measure(number='1', width=360.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Attributes():
                Divisions(16.0)
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=271.38):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=271.38):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=279.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=300.1):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=236.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='7', width=260.42):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=244.79):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=248.59):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=321.84):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=234.91):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=259.8):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=234.91):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=239.06):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=370.8):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=299.67):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=328.9):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=291.15):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=377.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=302.68):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=301.9):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=308.15):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=329.43):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=249.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=234.38):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=242.67):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=234.26):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=308.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='29', width=274.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='30', width=257.24):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=244.47):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=205.74):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P3'):
        with Measure(number='1', width=231.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(50.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
                    ClefOctaveChange(1)
            with Note(default_x=101.25, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='2', width=178.11):
            with Note(default_x=15.44, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='3', width=162.92):
            with Note(default_x=12.58, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='4', width=238.59):
            with Note(default_x=12.58, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=174.23, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=205.61, default_y=-205.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='5', width=151.08):
            with Note(default_x=12.58, default_y=-210.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='6', width=219.87):
            with Note(default_x=12.58, default_y=-205.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=151.48, default_y=-205.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=184.87, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='7', width=379.59):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(50.0)
            with Note(default_x=79.73, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=125.31, default_y=-205.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=174.34, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='8', width=204.84):
            with Note(default_x=12.0, default_y=-220.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=117.88, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=146.68, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=180.07, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='9', width=139.28):
            with Note(default_x=12.58, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='10', width=198.28):
            with Note(default_x=12.0, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=91.3, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=117.64, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=143.99, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=170.33, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='11', width=199.57):
            with Note(default_x=12.12, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=105.08, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=131.64, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=158.2, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=168.97):
            with Note(default_x=17.23, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=95.22, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=119.27, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=143.32, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=300.27):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(50.0)
            with Note(default_x=83.05, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='14', width=273.67):
            with Note(default_x=12.58, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='15', width=223.87):
            with Note(default_x=12.36, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='16', width=260.56):
            with Note(default_x=42.83, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=180.44, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=207.82, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=232.15):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=24.89, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=123.0, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=280.17):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(50.0)
            with Note(default_x=98.07, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=197.0, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=224.19, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='19', width=302.55):
            with Note(default_x=32.21, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=163.63, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=187.71, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=198.55):
            with Note(default_x=17.23, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=128.39, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=151.09, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=173.79, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=246.84):
            with Note(default_x=12.36, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=139.57, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='22', width=262.42):
            with Note(default_x=12.0, default_y=-205.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=179.18, default_y=-210.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='23', width=293.6):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(50.0)
            with Note(default_x=79.61, default_y=-215.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=108.46, default_y=-205.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=176.6, default_y=-210.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=205.45, default_y=-215.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=234.3, default_y=-210.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=259.51):
            with Note(default_x=32.21, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=60.07, default_y=-210.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=146.45, default_y=-220.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=174.32, default_y=-210.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=202.18, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=230.05, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='25', width=168.17):
            with Note(default_x=12.58, default_y=-205.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='26', width=287.12):
            with Note(default_x=12.0, default_y=-210.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='27', width=282.11):
            with Note(default_x=12.0, default_y=-215.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=145.25, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=189.66, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=235.14, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='28', width=298.29):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(50.0)
            with Note(default_x=79.61, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=114.87, default_y=-215.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=150.13, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=185.38, default_y=-205.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=220.64, default_y=-210.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=255.9, default_y=-215.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='29', width=230.68):
            with Note(default_x=12.0, default_y=-220.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=47.26, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=82.51, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=117.77, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=153.03, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=188.29, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='30', width=258.18):
            with Note(default_x=12.0, default_y=-205.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.98, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=93.62, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.25, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=166.88, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=215.1, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=234.48):
            with Note(default_x=15.8, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=51.06, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=86.31, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=121.57, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=156.83, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=192.09, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=218.81):
            with Note(default_x=13.06, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=112.19, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=164.57, default_y=-220.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X1', implicit='yes', width=50.07):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('64th')
            with Barline(location='right'):
                BarStyle('none')
        with Measure(number='1', width=360.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Attributes():
                Divisions(16.0)
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=100.67, default_y=-130.0, dynamics=70.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=141.61, default_y=-85.0, dynamics=104.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=162.08, default_y=-90.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=182.56, default_y=-85.0, dynamics=91.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=223.5, default_y=-95.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=264.44, default_y=-130.0, dynamics=78.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=305.38, default_y=-95.0, dynamics=108.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='2', width=271.38):
            with Note(default_x=12.0, default_y=-100.0, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=62.37, default_y=-100.0, dynamics=77.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=82.84, default_y=-105.0, dynamics=81.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.31, default_y=-100.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=144.25, default_y=-110.0, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=185.2, default_y=-100.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=226.14, default_y=-110.0, dynamics=74.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='3', width=271.38):
            with Note(default_x=12.0, default_y=-105.0, dynamics=91.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=52.94, default_y=-105.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=73.41, default_y=-110.0, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=93.89, default_y=-105.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=134.83, default_y=-95.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=185.2, default_y=-125.0, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=226.14, default_y=-80.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=279.66):
            with Note(default_x=12.0, default_y=-110.0, dynamics=67.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.84, default_y=-100.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=87.54, default_y=-105.0, dynamics=82.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=108.46, default_y=-100.0, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=150.3, default_y=-75.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=192.14, default_y=-110.0, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=254.9, default_y=-80.0, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
        with Measure(number='5', width=300.1):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Note(default_x=79.73, default_y=-85.0, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=97.51, default_y=-90.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=115.29, default_y=-85.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=150.86, default_y=-85.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=168.64, default_y=-110.0, dynamics=70.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.42, default_y=-105.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=204.2, default_y=-100.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=221.98, default_y=-95.0, dynamics=87.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=239.77, default_y=-90.0, dynamics=86.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=257.55, default_y=-85.0, dynamics=92.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.33, default_y=-95.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='6', width=236.62):
            with Note(default_x=12.12, default_y=-115.0, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.15, default_y=-120.0, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=48.17, default_y=-115.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=84.23, default_y=-115.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=102.26, default_y=-105.0, dynamics=91.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=120.28, default_y=-100.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.31, default_y=-95.0, dynamics=86.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=156.34, default_y=-90.0, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.37, default_y=-85.0, dynamics=93.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.83, default_y=-80.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=211.86, default_y=-90.0, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='7', width=260.42):
            with Note(default_x=12.12, default_y=-110.0, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.02, default_y=-115.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=60.88, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=98.61, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=117.47, default_y=-90.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.33, default_y=-85.0, dynamics=91.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.8, default_y=-80.0, dynamics=91.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=179.06, default_y=-75.0, dynamics=86.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=197.93, default_y=-105.0, dynamics=67.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=216.79, default_y=-100.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.66, default_y=-110.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='8', width=244.79):
            with Note(default_x=12.0, default_y=-95.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=30.7, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=49.41, default_y=-95.0, dynamics=83.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=68.11, default_y=-75.0, dynamics=96.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=87.58, default_y=-85.0, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.04, default_y=-75.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.74, default_y=-95.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.45, default_y=-85.0, dynamics=90.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=163.15, default_y=-110.0, dynamics=68.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=181.86, default_y=-95.0, dynamics=95.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.56, default_y=-120.0, dynamics=76.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.02, default_y=-110.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='9', width=248.59):
            with Note(default_x=15.8, default_y=-130.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.97, default_y=-95.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=91.38, default_y=-85.0, dynamics=96.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=128.78, default_y=-95.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=166.95, default_y=-130.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=205.12, default_y=-95.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='10', width=321.84):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Note(default_x=83.41, default_y=-100.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=168.44, default_y=-100.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=205.19, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=241.94, default_y=-110.0, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=278.7, default_y=-100.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='11', width=234.91):
            with Note(default_x=12.0, default_y=-105.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.03, default_y=-105.0, dynamics=82.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=84.05, default_y=-95.0, dynamics=87.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=120.08, default_y=-105.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=156.11, default_y=-105.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=192.13, default_y=-95.0, dynamics=92.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=259.8):
            with Note(default_x=17.23, default_y=-125.0, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.05, default_y=-105.0, dynamics=96.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=106.16, default_y=-95.0, dynamics=96.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=142.98, default_y=-105.0, dynamics=74.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=179.8, default_y=-125.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=216.62, default_y=-95.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=234.91):
            with Note(default_x=12.0, default_y=-100.0, dynamics=82.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.01, default_y=-90.0, dynamics=91.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=48.03, default_y=-100.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=84.05, default_y=-100.0, dynamics=85.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=120.08, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.09, default_y=-90.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=156.11, default_y=-100.0, dynamics=73.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.12, default_y=-90.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.13, default_y=-110.0, dynamics=67.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.15, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='14', width=239.06):
            with Note(default_x=12.0, default_y=-95.0, dynamics=85.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.28, default_y=-85.0, dynamics=95.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=48.56, default_y=-95.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=85.13, default_y=-95.0, dynamics=82.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=121.69, default_y=-75.0, dynamics=102.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.16, default_y=-85.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=159.44, default_y=-95.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.73, default_y=-85.0, dynamics=95.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.01, default_y=-105.0, dynamics=74.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.29, default_y=-95.0, dynamics=90.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='15', width=370.8):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.5)
            with Note(default_x=91.65, default_y=-95.5, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=137.9, default_y=-85.5, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=184.16, default_y=-80.5, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.28, default_y=-95.5, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.41, default_y=-105.5, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.53, default_y=-115.5, dynamics=74.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=276.66, default_y=-95.5, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=322.91, default_y=-130.5, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='16', width=299.67):
            with Note(default_x=12.0, default_y=-115.5, dynamics=95.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.14, default_y=-115.5, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.04, default_y=-110.5, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.18, default_y=-105.5, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=117.33, default_y=-100.5, dynamics=87.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.47, default_y=-95.5, dynamics=91.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.62, default_y=-90.5, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.31, default_y=-85.5, dynamics=92.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=226.46, default_y=-80.5, dynamics=91.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=328.9):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=24.89, default_y=-115.5, dynamics=62.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=75.3, default_y=-105.5, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=100.5, default_y=-110.5, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=125.7, default_y=-105.5, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=176.1, default_y=-115.5, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=226.5, default_y=-115.5, dynamics=86.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=276.9, default_y=-105.5, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='18', width=291.15):
            with Note(default_x=12.0, default_y=-135.5, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.25, default_y=-90.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=81.38, default_y=-95.5, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=104.5, default_y=-90.5, dynamics=92.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=150.76, default_y=-100.5, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=197.01, default_y=-135.5, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=243.26, default_y=-90.5, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='19', width=377.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(91.86)
            with Note(default_x=79.61, default_y=-116.86, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=133.19, default_y=-81.86, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=156.87, default_y=-86.86, dynamics=102.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.55, default_y=-81.86):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=227.9, default_y=-101.86, dynamics=72.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=275.26, default_y=-91.86, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=328.83, default_y=-81.86, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='20', width=302.68):
            with Note(default_x=12.0, default_y=-91.86, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=64.8, default_y=-101.86, dynamics=77.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=117.6, default_y=-111.86, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.5, default_y=-121.86, dynamics=78.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.4, default_y=-111.86, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.31, default_y=-101.86, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=209.21, default_y=-86.86, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=232.11, default_y=-111.86, dynamics=66.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.01, default_y=-101.86, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.92, default_y=-91.86, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='21', width=301.9):
            with Note(default_x=12.0, default_y=-96.86, dynamics=80.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=64.71, default_y=-96.86, dynamics=80.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=87.53, default_y=-101.86, dynamics=77.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=110.34, default_y=-96.86, dynamics=84.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=163.05, default_y=-96.86, dynamics=84.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=185.87, default_y=-101.86, dynamics=85.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=208.68, default_y=-96.86, dynamics=85.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=254.31, default_y=-96.86, dynamics=85.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=277.13, default_y=-121.86, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='22', width=308.15):
            with Note(default_x=13.06, default_y=-116.86, dynamics=84.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=60.98, default_y=-116.86, dynamics=84.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=84.95, default_y=-86.86, dynamics=105.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=108.91, default_y=-81.86, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=162.77, default_y=-81.86, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=186.73, default_y=-86.86, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=210.7, default_y=-81.86, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=258.62, default_y=-81.86, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=282.59, default_y=-106.86, dynamics=70.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=329.43):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Note(default_x=91.65, default_y=-110.0, dynamics=74.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=128.28, default_y=-90.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=164.9, default_y=-95.0, dynamics=84.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=213.11, default_y=-125.0, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=249.73, default_y=-120.0, dynamics=87.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=286.35, default_y=-100.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='24', width=249.78):
            with Note(default_x=12.0, default_y=-105.0, dynamics=82.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.62, default_y=-95.0, dynamics=90.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=78.52, default_y=-100.0, dynamics=81.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=96.83, default_y=-95.0, dynamics=87.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=133.45, default_y=-105.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=170.08, default_y=-105.0, dynamics=107.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=225.01, default_y=-110.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
        with Measure(number='25', width=234.38):
            with Note(default_x=12.12, default_y=-115.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.07, default_y=-105.0, dynamics=95.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=48.03, default_y=-90.0, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.98, default_y=-80.0, dynamics=95.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=83.94, default_y=-105.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=101.89, default_y=-80.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.85, default_y=-90.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.8, default_y=-105.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=155.75, default_y=-115.0, dynamics=76.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=173.71, default_y=-105.0, dynamics=95.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.66, default_y=-110.0, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.62, default_y=-115.0, dynamics=76.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='26', width=242.67):
            with Note(default_x=12.12, default_y=-120.0, dynamics=78.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.66, default_y=-110.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=49.2, default_y=-95.0, dynamics=96.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.74, default_y=-85.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=87.2, default_y=-75.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=106.67, default_y=-85.0, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.21, default_y=-95.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.75, default_y=-110.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=162.28, default_y=-120.0, dynamics=78.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=180.82, default_y=-110.0, dynamics=91.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.36, default_y=-115.0, dynamics=74.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.9, default_y=-120.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=234.26):
            with Note(default_x=12.0, default_y=-125.0, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=47.91, default_y=-115.0, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=83.82, default_y=-105.0, dynamics=93.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=119.73, default_y=-95.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=155.64, default_y=-100.0, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=191.54, default_y=-105.0, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='28', width=308.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Note(default_x=79.61, default_y=-110.0, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=116.69, default_y=-100.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=153.76, default_y=-90.0, dynamics=91.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=190.84, default_y=-80.0, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=227.91, default_y=-85.0, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=264.98, default_y=-90.0, dynamics=85.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='29', width=274.78):
            with Note(default_x=15.8, default_y=-95.0, dynamics=81.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.4, default_y=-120.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=96.99, default_y=-110.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=137.59, default_y=-100.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=178.18, default_y=-105.0, dynamics=82.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=226.74, default_y=-110.0, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='30', width=257.24):
            with Note(default_x=12.0, default_y=-115.0, dynamics=76.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.59, default_y=-105.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=93.25, default_y=-100.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=135.84, default_y=-95.0, dynamics=90.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=174.49, default_y=-90.0, dynamics=86.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=213.15, default_y=-95.0, dynamics=81.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=244.47):
            with Note(default_x=15.8, default_y=-100.0, dynamics=81.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=52.87, default_y=-110.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=89.95, default_y=-95.0, dynamics=95.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=127.02, default_y=-130.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=164.1, default_y=-75.0, dynamics=102.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=201.17, default_y=-110.0, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=205.74):
            with Note(default_x=12.0, default_y=-95.0, dynamics=92.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.24, default_y=-130.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=46.48, default_y=-125.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.72, default_y=-120.0, dynamics=90.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=80.96, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=98.2, default_y=-110.0, dynamics=93.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.44, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.68, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=149.92, default_y=-95.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')