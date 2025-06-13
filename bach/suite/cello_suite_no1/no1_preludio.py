with ScorePartwise(version='3.1'):
    with Identification():
        Rights('1893-G.Schirmer, Inc')
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
            Millimeters(5.6896)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2087.5)
            PageWidth(1476.79)
            with PageMargins(type='even'):
                LeftMargin(70.3037)
                RightMargin(70.3037)
                TopMargin(70.3037)
                BottomMargin(140.607)
            with PageMargins(type='odd'):
                LeftMargin(70.3037)
                RightMargin(70.3037)
                TopMargin(70.3037)
                BottomMargin(140.607)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J.S.BACH', default_x=1406.48, default_y=1917.2, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Preludio I', default_x=738.393, default_y=2017.2, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('1893-G.Schirmer, Inc', default_x=738.393, default_y=140.607, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('1893-G.Schirmer, Inc', default_x=738.393, default_y=140.607, justify='center', valign='bottom', font_size='8')
    with PartList():
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
    with Part(id='P1'):
        with Measure(number='1', width=689.33):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.84)
                        RightMargin(-0.0)
                    TopSystemDistance(189.16)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(0)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Allegro. ', default_y=62.25, font_weight='bold', font_family='Times New Roman', font_size='12.4008')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=156.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=194.79, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2')
            with Direction(placement='above'):
                with DirectionType():
                    Words('legato.', default_y=75.28, font_style='italic', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=232.71, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=270.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=308.55, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=346.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=460.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=498.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=536.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=573.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=611.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=649.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=118.96, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=232.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=422.31, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=536.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-154.45, relative_x=-1.29, relative_y=109.05):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=80.68, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=384.03, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='2', width=624.0):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=91.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=129.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('3')
            with Note(default_x=167.38, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=205.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=243.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=281.14, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=394.89, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=432.81, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=470.73, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=508.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=546.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=584.48, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=53.63, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=167.38, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=356.97, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=470.73, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.35, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=318.69, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=466.79):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.84)
                        RightMargin(-0.0)
                    SystemDistance(102.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=116.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=139.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', default_y=52.06, font_style='italic', font_family='Times New Roman')
                Staff(1)
            with Note(default_x=170.06, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=193.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=240.59, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=317.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=340.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=371.14, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=394.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=418.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=441.67, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=86.53, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=170.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=287.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=371.14, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=62.65, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=263.74, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='4', width=419.48):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=68.91, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=92.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=122.75, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=146.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=270.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=293.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=323.83, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=347.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=370.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=394.37, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=39.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=122.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=240.3, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=323.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.35, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=216.43, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=427.08):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=69.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=124.02, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=148.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.45, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=274.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=298.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=328.9, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=353.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=377.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=401.33, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=39.85, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=124.02, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=244.74, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=328.9, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-150.83, relative_x=-7.19, relative_y=105.43):
                        F()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=15.35, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=220.23, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='6', width=493.47):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.84)
                        RightMargin(-0.0)
                    SystemDistance(102.43)
                with StaffLayout(number=2):
                    StaffDistance(73.6)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=131.49, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=156.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=186.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=210.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.01, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=338.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=363.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=393.68, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=418.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=442.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=467.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=87.56, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=186.37, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=309.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=393.68, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-151.94, relative_x=-5.33, relative_y=106.54):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=62.65, default_y=-103.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=284.2, default_y=-103.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='7', width=431.93):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=69.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=94.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=124.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=149.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.47, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=277.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=301.81, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=332.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=356.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=381.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=405.78, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=40.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=124.83, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=247.57, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=332.14, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-146.61, relative_x=-9.05, relative_y=101.21):
                        F()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=15.35, default_y=-108.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=222.66, default_y=-108.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='8', width=387.94):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=61.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=84.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=130.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=247.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=270.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=293.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=316.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=339.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=363.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.53, default_y=-175.23, relative_x=-7.0, relative_y=129.83):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=38.0, default_y=-103.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('1')
            with Note(default_x=107.67, default_y=-103.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=223.78, default_y=-103.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=293.45, default_y=-103.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=14.42, default_y=-108.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=200.2, default_y=-108.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='9', width=461.96):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.84)
                        RightMargin(-0.0)
                    SystemDistance(102.43)
                with StaffLayout(number=2):
                    StaffDistance(73.6)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=108.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=134.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=159.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=184.24, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=309.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=334.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=359.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=385.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=410.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=435.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.53, default_y=-176.22, relative_x=-9.05, relative_y=130.82):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=83.83, default_y=-103.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=159.14, default_y=-103.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=284.65, default_y=-103.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=359.95, default_y=-103.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=58.37, default_y=-113.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=259.19, default_y=-113.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=432.44):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=66.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=98.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=123.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=149.43, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=277.35, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=302.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=328.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=354.1, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=379.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=405.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=41.29, default_y=-113.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('2')
            with Note(default_x=123.85, default_y=-113.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=251.76, default_y=-113.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=328.51, default_y=-113.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.35, default_y=-133.6):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=225.82, default_y=-133.6):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=418.93):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=65.91, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=91.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=116.11, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=266.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=291.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=316.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=342.03, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=367.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=392.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=40.81, default_y=-108.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('1')
            with Note(default_x=116.11, default_y=-108.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=241.62, default_y=-108.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', default_y=35.65, font_style='italic', font_family='Times New Roman')
                Staff(2)
            with Note(default_x=316.93, default_y=-108.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.35, default_y=-118.6):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=216.16, default_y=-118.6):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=480.23):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.84)
                        RightMargin(-0.0)
                    SystemDistance(102.43)
                with StaffLayout(number=2):
                    StaffDistance(75.63)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=114.68, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=171.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=197.24, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=222.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=248.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=325.14, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=350.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=376.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=401.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=427.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=453.05, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=89.1, default_y=-110.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('1')
            with Note(default_x=171.66, default_y=-110.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=299.56, default_y=-110.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=376.31, default_y=-110.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=58.37, default_y=-120.63):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=273.62, default_y=-120.63):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=410.13):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=64.81, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=89.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=113.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.47, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=261.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=285.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=310.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=334.88, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=359.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=383.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=40.26, default_y=-115.63):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('1')
            with Note(default_x=113.91, default_y=-115.63):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=236.67, default_y=-115.63):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=310.33, default_y=-115.63):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.35, default_y=-125.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=211.76, default_y=-125.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=422.97):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=71.09, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=96.11, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=121.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=146.15, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.17, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=271.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=296.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=321.29, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=346.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=371.33, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=396.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=46.07, default_y=-115.63):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('1')
            with Note(default_x=121.13, default_y=-115.63):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('dimin.', default_y=45.65, font_style='italic', font_family='Times New Roman')
                Staff(2)
            with Note(default_x=246.23, default_y=-115.63):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=321.29, default_y=-115.63):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.35, default_y=-125.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=220.85, default_y=-125.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=447.86):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.84)
                        RightMargin(-0.0)
                    SystemDistance(102.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=107.17, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=131.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=155.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=179.83, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=204.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=300.94, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=325.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=349.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=373.6, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=397.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=422.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=82.95, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=155.61, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=276.72, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=349.38, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=58.37, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=252.13, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=435.23):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=67.95, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=94.07, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=120.19, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=146.31, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.43, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=276.91, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=303.03, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=329.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=355.27, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=381.39, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=407.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.53, default_y=-173.61, relative_x=-10.35, relative_y=120.46):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=41.83, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('1')
            with Note(default_x=120.19, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=250.79, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=329.15, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.35, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=224.31, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=430.25):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=62.96, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=89.08, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=115.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.32, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=271.93, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=298.05, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=324.17, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=350.29, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=376.41, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=402.53, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=36.84, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=115.2, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=245.8, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=324.17, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=10.36, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=219.32, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=469.31):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.84)
                        RightMargin(-0.0)
                    SystemDistance(102.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-62.44, relative_x=-0.12, relative_y=17.04):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=109.54, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=135.12, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=160.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.29, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=211.87, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=314.21, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=339.79, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=365.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=390.96, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=416.54, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=442.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=83.96, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('2')
            with Note(default_x=160.71, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=288.62, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=365.37, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=58.01, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=262.68, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='19', width=422.38):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=61.98, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=87.61, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=113.24, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.86, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.49, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=267.01, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=292.63, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=318.26, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=343.89, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=369.52, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=395.15, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=36.35, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=113.24, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=241.38, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=318.26, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=10.36, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=215.39, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='20', width=421.66):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=61.89, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=87.47, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=113.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.64, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.22, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.81, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=266.56, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=292.14, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=317.72, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=343.31, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=368.89, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=394.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=36.31, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=113.06, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=240.97, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=317.72, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=10.36, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=215.03, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='21', width=453.82):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.84)
                        RightMargin(-0.0)
                    TopSystemDistance(100.0)
                with StaffLayout(number=2):
                    StaffDistance(80.63)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=107.5, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.27, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=156.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=181.4, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.17, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=304.43, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=329.2, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=353.76, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=378.33, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=403.09, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=427.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=82.94, default_y=-130.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=156.83, default_y=-130.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('dimin.', default_y=35.65, font_style='italic', font_family='Times New Roman')
                Staff(2)
            with Note(default_x=279.86, default_y=-130.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=353.76, default_y=-130.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=58.01, default_y=-165.63):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=254.94, default_y=-165.63):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=426.61):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=68.18, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.29, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=123.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=148.77, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.88, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.99, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=274.33, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=299.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=324.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=349.67, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=374.78, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=399.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=43.07, default_y=-145.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=123.66, default_y=-145.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=249.22, default_y=-145.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=324.56, default_y=-145.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.59, default_y=-165.63):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=223.74, default_y=-165.63):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='23', width=432.91):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=67.1, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=92.78, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=123.15, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=148.83, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=174.51, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.19, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=277.23, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=302.91, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=328.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=354.27, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=379.95, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=405.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.53, default_y=-174.21, relative_x=-9.05, relative_y=102.31):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=41.42, default_y=-135.63):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('2')
            with Note(default_x=123.15, default_y=-135.63):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=251.55, default_y=-135.63):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=328.59, default_y=-135.63):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=10.7, default_y=-160.63):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=225.51, default_y=-160.63):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='24', width=484.63):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.84)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=121.58, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=147.39, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=173.21, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=199.03, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.85, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=250.67, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=328.12, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=353.94, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=379.76, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=405.58, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=431.4, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=457.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=95.76, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=173.21, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=302.31, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=379.76, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=69.58, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=276.13, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='25', width=425.75):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=62.69, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=88.51, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=114.33, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.15, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=165.97, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.79, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=269.24, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=295.06, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=320.88, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=346.7, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=372.51, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=398.33, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', default_y=43.2, font_style='italic', font_family='Times New Roman')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=36.87, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=114.33, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=243.42, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=320.88, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=10.7, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=217.24, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=402.95):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=59.6, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=84.36, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=108.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.9, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.67, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=254.74, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=279.51, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=303.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=328.05, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=352.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=377.08, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=35.33, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=108.63, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=230.47, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=303.78, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=10.7, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=205.84, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='27', width=459.64):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.84)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=108.33, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=133.31, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=158.29, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=183.27, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.25, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=233.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=308.17, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=333.15, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=358.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=383.1, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=408.08, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=433.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=83.35, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=158.29, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=283.19, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=358.12, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=58.01, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=257.85, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='28', width=412.33):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=61.02, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.99, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=110.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=135.95, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.93, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=260.85, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=285.83, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=310.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=335.79, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=360.77, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=385.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=36.04, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=110.97, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=235.87, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=310.81, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=10.7, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=210.53, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='29', width=441.37):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=67.52, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.61, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=126.62, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.72, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=204.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=283.19, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=309.29, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=335.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=361.48, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=387.58, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=413.67, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.53, default_y=-167.6, relative_x=-2.54, relative_y=117.15):
                        F()
                Staff(2)
                Sound(dynamics=106.67)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=41.42, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=126.62, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=257.1, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=335.38, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=10.7, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=230.64, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='30', width=469.32):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.84)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(75.63)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-57.19, relative_x=-1.92, relative_y=11.8):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=109.54, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=135.13, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=160.71, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.29, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=211.88, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=314.22, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=339.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=365.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=390.97, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=416.55, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=442.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=83.96, default_y=-130.63):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=160.71, default_y=-130.63):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('dimin.', default_y=25.65, font_style='italic', font_family='Times New Roman')
                Staff(2)
            with Note(default_x=288.63, default_y=-130.63):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=365.39, default_y=-130.63):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=58.01, default_y=-155.63):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=262.69, default_y=-155.63):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='31', width=422.01):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=62.23, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=87.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=113.39, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.98, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.56, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=266.9, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=292.49, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=318.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=343.65, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=369.24, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=394.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=36.64, default_y=-135.63):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=113.39, default_y=-135.63):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=241.32, default_y=-135.63):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=318.07, default_y=-135.63):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=10.7, default_y=-155.63):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=215.37, default_y=-155.63):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='32', width=422.01):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=62.23, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=87.81, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=113.39, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.98, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.56, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=266.9, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=292.49, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=318.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=343.65, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=369.24, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=394.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.53, default_y=-168.34, relative_x=-2.91, relative_y=117.89):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=36.64, default_y=-135.63):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=113.39, default_y=-135.63):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=241.32, default_y=-135.63):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=318.07, default_y=-135.63):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=10.7, default_y=-155.63):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=215.37, default_y=-155.63):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='33', width=447.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.84)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=104.51, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.49, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=163.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.63, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=211.39, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=303.68, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=328.44, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=351.52, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=374.59, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=399.35, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=422.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.53, default_y=-194.24, relative_x=-5.63, relative_y=106.09):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=81.44, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=163.56, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=280.61, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=351.52, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=58.01, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=257.18, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='34', width=382.29):
            with Direction(placement='above'):
                with DirectionType():
                    Words('calando', relative_y=20.0, font_style='italic', font_family='Times New Roman')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=110.53, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=132.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=154.97, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.74, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=66.08, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=88.3, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=201.96, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=224.18, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=246.41, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=268.63, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=290.85, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=313.08, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=335.3, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=357.52, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Staff(2)
            with Note(default_x=36.38, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('6')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=110.53, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=201.6, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Tie(type='start')
                Voice('7')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=201.6, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('7')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='35', width=361.37):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=57.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=78.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=100.15, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.64, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=186.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=207.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=229.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=250.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=272.12, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=293.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=315.11, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=35.66, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=100.15, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=185.77, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=185.77, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='36', width=122.49):
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=13.31, relative_y=10.0)
            with Note(default_x=13.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=13.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-59.42, relative_y=-10.0)
            with Note(default_x=13.8, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')