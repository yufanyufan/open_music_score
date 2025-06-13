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
        CreditWords('"Air" from Bach\'s Orchestral Suite No. 3 (BWV 1068)', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Piano')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Voice')
            PartAbbreviation('Vo.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Voice')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=252.52):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(87.4)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(2)
                with Time():
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
                    with Metronome(parentheses='no', default_x=-39.32, relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Note(default_x=112.27, default_y=0.0, dynamics=116.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=20.0)
                Staff(2)
            with Note(default_x=115.59, default_y=-125.0, dynamics=116.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=149.42, default_y=-90.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F#m', default_y=0.42, relative_y=20.0)
                Staff(2)
            with Note(default_x=183.26, default_y=-95.0, dynamics=105.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=217.09, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='2', width=144.46):
            with Note(default_x=13.32, default_y=0.0, dynamics=116.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Bm', relative_y=20.0)
                Staff(2)
            with Note(default_x=16.64, default_y=-135.0, dynamics=116.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=48.19, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=20.0)
                Staff(2)
            with Note(default_x=79.75, default_y=-105.0, dynamics=105.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=111.3, default_y=-140.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='3', width=235.92):
            with Note(default_x=13.8, default_y=0.0, dynamics=116.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=58.57, default_y=15.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=86.55, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=103.96, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=122.4, default_y=-5.0, dynamics=105.56):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=150.38, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=178.36, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=206.34, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('GM7', relative_y=20.0)
                Staff(2)
            with Note(default_x=13.8, default_y=-145.0, dynamics=116.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=58.57, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G#o', relative_y=20.0)
                Staff(2)
            with Note(default_x=122.4, default_y=-110.0, dynamics=105.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=178.36, default_y=-145.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
        with Measure(number='4', width=160.78):
            with Note(default_x=13.8, default_y=-15.0, dynamics=116.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=82.4, default_y=-20.0, dynamics=105.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=103.73, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=20.0)
                Staff(2)
            with Note(default_x=14.16, default_y=-140.0, dynamics=116.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=48.28, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C#o', relative_y=20.0)
                Staff(2)
            with Note(default_x=82.4, default_y=-110.0, dynamics=105.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=125.05, default_y=-145.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='5', width=196.41):
            with Note(default_x=17.8, default_y=10.0, dynamics=116.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=57.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=81.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=106.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=145.64, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=170.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F#Φ7', relative_y=20.0)
                Staff(2)
            with Note(default_x=17.8, default_y=-150.0, dynamics=116.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=57.14, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F#Φ7/E', relative_y=20.0)
                Staff(2)
            with Note(default_x=106.31, default_y=-120.0, dynamics=105.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=145.64, default_y=-155.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='6', width=315.97):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    SystemDistance(91.09)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=107.05, default_y=-20.0, dynamics=116.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=132.18, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=158.84, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=183.97, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=209.09, default_y=-5.0, dynamics=105.56):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=238.99, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=264.12, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=289.24, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B7/D#', relative_y=20.0)
                Staff(2)
            with Note(default_x=107.05, default_y=-160.0, dynamics=116.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=158.84, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=209.09, default_y=-135.0, dynamics=105.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=264.12, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='7', width=169.44):
            with Note(default_x=14.16, default_y=-20.0, dynamics=116.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=45.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=65.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=85.35, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=105.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=124.9, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=144.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=20.0)
                Staff(2)
            with Note(default_x=14.16, default_y=-155.0, dynamics=116.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=45.8, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=20.0)
                Staff(2)
            with Note(default_x=85.35, default_y=-125.0, dynamics=105.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=124.9, default_y=-160.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='8', width=188.24):
            with Note(default_x=14.16, default_y=-25.0, dynamics=116.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=35.49, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=56.82, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=78.15, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=99.48, default_y=-10.0, dynamics=105.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=120.81, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=142.14, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.47, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A7', relative_y=20.0)
                Staff(2)
            with Note(default_x=14.16, default_y=-165.0, dynamics=116.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=56.82, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F#m7', relative_y=20.0)
                Staff(2)
            with Note(default_x=99.48, default_y=-140.0, dynamics=105.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=142.14, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='9', width=142.08):
            with Note(default_x=10.36, default_y=0.0, dynamics=116.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=97.85, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=117.31, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=20.0)
                Staff(2)
            with Note(default_x=10.72, default_y=-125.0, dynamics=116.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=39.76, default_y=-90.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F#m', default_y=0.42, relative_y=20.0)
                Staff(2)
            with Note(default_x=68.81, default_y=-95.0, dynamics=105.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=97.85, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='10', width=189.18):
            with Note(default_x=14.16, default_y=-10.0, dynamics=116.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=44.58, default_y=-10.0, dynamics=88.89):
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
            with Note(default_x=60.25, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=75.91, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=98.04, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=120.16, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=142.29, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=164.41, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Bm', relative_y=20.0)
                Staff(2)
            with Note(default_x=14.16, default_y=-135.0, dynamics=116.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=44.58, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=20.0)
                Staff(2)
            with Note(default_x=98.04, default_y=-110.0, dynamics=105.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=142.29, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=309.24):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    SystemDistance(91.09)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=95.01, default_y=-15.0, dynamics=116.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=122.35, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=149.69, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=166.78, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=183.86, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=211.2, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=252.96, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=280.3, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('DM7', relative_y=20.0)
                Staff(2)
            with Note(default_x=95.01, default_y=-105.0, dynamics=116.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=149.69, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E7', relative_y=20.0)
                Staff(2)
            with Note(default_x=211.2, default_y=-120.0, dynamics=105.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=252.96, default_y=-155.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='12', width=212.9):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=30.0)
            with Note(default_x=10.84, default_y=-25.0, dynamics=116.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=20.0)
                Staff(2)
            with Note(default_x=14.16, default_y=-140.0, dynamics=116.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.62, default_y=-135.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=59.08, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=81.53, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F#m7', relative_y=20.0)
                Staff(2)
            with Note(default_x=103.99, default_y=-120.0, dynamics=105.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=126.45, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=148.91, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=171.37, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='13', width=76.94):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=30.0)
            with Note(default_x=13.8, default_y=-25.0, dynamics=116.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=20.0)
                Staff(2)
            with Note(default_x=13.8, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue')
        with Measure(number='14', width=210.7):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=28.37, default_y=-15.0, dynamics=116.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=96.87, default_y=-15.0, dynamics=116.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=121.65, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.32, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=152.99, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.65, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=184.32, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=20.0)
                Staff(2)
            with Note(default_x=28.73, default_y=-140.0, dynamics=116.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=62.8, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C#o', relative_y=20.0)
                Staff(2)
            with Note(default_x=96.87, default_y=-110.0, dynamics=105.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=152.99, default_y=-145.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='15', width=195.11):
            with Note(default_x=17.8, default_y=10.0, dynamics=116.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=40.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=66.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=102.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=125.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=147.87, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=170.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F#Φ7', relative_y=20.0)
                Staff(2)
            with Note(default_x=17.8, default_y=-150.0, dynamics=116.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=66.94, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F#Φ7/E', relative_y=20.0)
                Staff(2)
            with Note(default_x=102.91, default_y=-120.0, dynamics=105.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=147.87, default_y=-155.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='16', width=276.43):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    SystemDistance(91.09)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=107.05, default_y=-20.0, dynamics=116.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=144.34, default_y=15.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=181.62, default_y=15.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=204.92, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=228.23, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=251.53, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B7', relative_y=20.0)
                Staff(2)
            with Note(default_x=107.05, default_y=-160.0, dynamics=116.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=144.34, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=181.62, default_y=-110.0, dynamics=105.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=228.23, default_y=-135.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='17', width=190.38):
            with Note(default_x=13.8, default_y=5.0, dynamics=116.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=78.98, default_y=5.0, dynamics=116.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=94.64, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.31, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.97, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=141.64, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=165.21, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=20.0)
                Staff(2)
            with Note(default_x=14.16, default_y=-120.0, dynamics=116.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=46.57, default_y=-85.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', default_y=5.82, relative_y=20.0)
                Staff(2)
            with Note(default_x=78.98, default_y=-90.0, dynamics=105.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=141.64, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=151.29):
            with Note(default_x=17.23, default_y=-25.0, dynamics=116.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=35.63, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=54.03, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=83.46, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=101.86, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=120.26, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C#o7', default_y=0.82, relative_y=20.0)
                Staff(2)
            with Note(default_x=17.23, default_y=-130.0, dynamics=116.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=54.03, default_y=-95.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=20.0)
                Staff(2)
            with Note(default_x=83.46, default_y=-100.0, dynamics=105.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=120.26, default_y=-135.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='19', width=182.61):
            with Note(default_x=17.23, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=37.52, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=57.8, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=78.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=107.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=128.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=148.55, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F#', relative_y=20.0)
                Staff(2)
            with Note(default_x=17.23, default_y=-140.0, dynamics=116.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=57.8, default_y=-135.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=107.98, default_y=-130.0, dynamics=105.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=148.55, default_y=-140.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='20', width=204.18):
            with Note(default_x=10.0, default_y=-5.0, dynamics=116.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=33.01, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=56.03, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=79.04, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=102.05, default_y=-15.0, dynamics=105.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=125.07, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.73, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=156.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=179.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Bm', relative_y=20.0)
                Staff(2)
            with Note(default_x=10.0, default_y=-135.0, dynamics=116.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C#o7', relative_y=20.0)
                Staff(2)
            with Note(default_x=56.03, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=102.05, default_y=-120.0, dynamics=105.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=156.4, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='21', width=225.88):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=91.57, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=111.09, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=130.24, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Bm', relative_y=20.0)
                Staff(2)
            with Note(default_x=91.57, default_y=-135.0, dynamics=116.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=130.6, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=20.0)
                Staff(2)
            with Note(default_x=161.83, default_y=-105.0, dynamics=105.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=193.05, default_y=-140.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='22', width=187.7):
            with Note(default_x=17.59, default_y=-10.0, dynamics=116.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=92.69, default_y=-10.0, dynamics=116.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=116.04, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=139.39, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=162.75, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G#Φ7', relative_y=20.0)
                Staff(2)
            with Note(default_x=17.95, default_y=-145.0, dynamics=116.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=55.32, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=20.0)
                Staff(2)
            with Note(default_x=92.69, default_y=-115.0, dynamics=105.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=139.39, default_y=-150.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='23', width=224.79):
            with Note(default_x=17.23, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=58.53, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=84.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=114.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=140.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=165.87, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=197.37, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=20.0)
                Staff(2)
            with Note(default_x=17.23, default_y=-155.0, dynamics=116.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=58.53, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E7', relative_y=20.0)
                Staff(2)
            with Note(default_x=114.24, default_y=-125.0, dynamics=105.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=165.87, default_y=-160.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='24', width=221.51):
            with Note(default_x=14.16, default_y=0.0, dynamics=116.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.39, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=48.61, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=76.17, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=114.06, default_y=-20.0, dynamics=105.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=151.96, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=179.52, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=196.74, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=20.0)
                Staff(2)
            with Note(default_x=14.16, default_y=-165.0, dynamics=116.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=76.17, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Bm', relative_y=20.0)
                Staff(2)
            with Note(default_x=114.06, default_y=-125.0, dynamics=105.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E7', relative_y=20.0)
                Staff(2)
            with Note(default_x=151.96, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='25', width=145.03):
            with Note(default_x=10.72, default_y=-15.0, dynamics=116.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=61.46, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=80.62, default_y=-25.0, dynamics=105.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=20.0)
                Staff(2)
            with Note(default_x=10.72, default_y=-140.0, dynamics=116.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=41.95, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C#o', relative_y=20.0)
                Staff(2)
            with Note(default_x=80.98, default_y=-110.0, dynamics=105.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=112.2, default_y=-145.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='26', width=273.04):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=91.57, default_y=-10.0, dynamics=116.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=126.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=153.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=174.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=204.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=226.51, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=248.28, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=20.0)
                Staff(2)
            with Note(default_x=91.57, default_y=-150.0, dynamics=116.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=126.41, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('GM7', relative_y=20.0)
                Staff(2)
            with Note(default_x=174.84, default_y=-110.0, dynamics=105.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=226.51, default_y=-145.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='27', width=186.22):
            with Note(default_x=17.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=52.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=74.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=96.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=117.97, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=139.71, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=161.46, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=20.0)
                Staff(2)
            with Note(default_x=17.95, default_y=-145.0, dynamics=116.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=52.74, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A7', relative_y=20.0)
                Staff(2)
            with Note(default_x=96.23, default_y=-105.0, dynamics=105.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=139.71, default_y=-140.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='28', width=215.76):
            with Note(default_x=42.93, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=78.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=101.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=123.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=146.13, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=168.56, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=191.0, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F#M7', relative_y=20.0)
                Staff(2)
            with Note(default_x=42.93, default_y=-140.0, dynamics=116.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=78.83, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B7', relative_y=20.0)
                Staff(2)
            with Note(default_x=123.69, default_y=-100.0, dynamics=105.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=168.56, default_y=-135.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='29', width=145.71):
            with Note(default_x=13.32, default_y=5.0, dynamics=116.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=31.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=49.65, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=67.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=85.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=20.0)
                Staff(2)
            with Note(default_x=13.32, default_y=-120.0, dynamics=116.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=49.65, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=85.98, default_y=-125.0, dynamics=105.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=115.05, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='30', width=184.15):
            with Note(default_x=14.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=34.91, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=55.65, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=76.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=97.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=117.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=138.64, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=159.39, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A7', relative_y=20.0)
                Staff(2)
            with Note(default_x=14.16, default_y=-130.0, dynamics=116.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=55.65, default_y=-95.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=97.15, default_y=-105.0, dynamics=105.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=138.64, default_y=-95.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='31', width=302.79):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=91.57, default_y=5.0, dynamics=116.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=117.77, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=143.96, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=170.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=196.35, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=258.56, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=278.03, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', default_y=5.42, relative_y=20.0)
                Staff(2)
            with Note(default_x=91.57, default_y=-90.0, dynamics=116.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=143.96, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F#o', default_y=10.52, relative_y=20.0)
                Staff(2)
            with Note(default_x=196.35, default_y=-130.0, dynamics=105.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=232.37, default_y=-95.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='32', width=201.16):
            with Note(default_x=23.31, default_y=-10.0, dynamics=116.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=60.52, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=97.73, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=120.98, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=144.24, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=176.3, default_y=20.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em7', relative_y=20.0)
                Staff(2)
            with Note(default_x=23.31, default_y=-100.0, dynamics=116.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=60.52, default_y=-135.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D7', relative_y=20.0)
                Staff(2)
            with Note(default_x=97.73, default_y=-140.0, dynamics=105.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=144.24, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='33', width=126.92):
            with Note(default_x=13.8, default_y=15.0, dynamics=116.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=97.53, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=20.0)
                Staff(2)
            with Note(default_x=14.16, default_y=-110.0, dynamics=116.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=41.95, default_y=-145.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Bm', relative_y=20.0)
                Staff(2)
            with Note(default_x=69.74, default_y=-150.0, dynamics=105.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=97.53, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='34', width=159.43):
            with Note(default_x=13.32, default_y=-15.0, dynamics=116.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=34.57, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=55.46, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=123.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C#Φ7', relative_y=20.0)
                Staff(2)
            with Note(default_x=13.32, default_y=-120.0, dynamics=116.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=55.82, default_y=-155.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=89.82, default_y=-160.0, dynamics=105.56):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=123.83, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='35', width=214.59):
            with Note(default_x=14.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=48.42, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=73.34, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=89.01, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=105.46, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=130.38, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=180.22, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=155.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A7', relative_y=20.0)
                Staff(2)
            with Note(default_x=14.16, default_y=-130.0, dynamics=116.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=48.42, default_y=-140.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=20.0)
                Staff(2)
            with Note(default_x=105.46, default_y=-125.0, dynamics=105.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=20.0)
                Staff(2)
            with Note(default_x=155.3, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='36', width=602.97):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    SystemDistance(124.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=91.57, default_y=-10.0, dynamics=116.67):
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
            with Note(default_x=130.19, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=168.82, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=230.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=292.4, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=354.2, default_y=-10.0, dynamics=105.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=415.99, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=477.78, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=539.58, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=20.0)
                Staff(2)
            with Note(default_x=91.57, default_y=-105.0, dynamics=116.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=230.61, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A7', relative_y=20.0)
                Staff(2)
            with Note(default_x=354.2, default_y=-105.0, dynamics=105.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=477.78, default_y=-140.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='37', width=401.92):
            with Note(default_x=13.8, default_y=-10.0, dynamics=116.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', default_y=10.23, relative_y=20.0)
                Staff(2)
            with Note(default_x=13.8, default_y=-160.0, dynamics=116.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P2'):
        with Measure(number='1', width=252.52):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=115.23, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=115.23, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=115.23, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=182.9, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=182.9, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=182.9, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='2', width=144.46):
            with Note(default_x=16.28, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=16.28, default_y=-255.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=16.28, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=79.39, default_y=-270.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=79.39, default_y=-255.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=79.39, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='3', width=235.92):
            with Note(default_x=13.8, default_y=-275.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=13.8, default_y=-265.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=13.8, default_y=-255.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=13.8, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.57, default_y=-275.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.57, default_y=-265.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.57, default_y=-255.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=122.04, default_y=-275.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=122.04, default_y=-265.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=122.04, default_y=-255.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='4', width=160.78):
            with Note(default_x=13.8, default_y=-270.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=82.04, default_y=-275.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=82.04, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=82.04, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='5', width=196.41):
            with Note(default_x=17.44, default_y=-280.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=17.44, default_y=-270.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=17.44, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
            with Note(default_x=17.44, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=105.95, default_y=-285.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=118.53, default_y=-280.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=105.95, default_y=-270.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=105.95, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='6', width=315.97):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=106.69, default_y=-290.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=106.69, default_y=-280.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=106.69, default_y=-270.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=119.28, default_y=-265.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=208.73, default_y=-290.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=208.73, default_y=-280.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=208.73, default_y=-270.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=221.32, default_y=-265.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=169.44):
            with Note(default_x=13.8, default_y=-285.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-275.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-265.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=84.99, default_y=-290.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=84.99, default_y=-275.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=84.99, default_y=-265.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='8', width=188.24):
            with Note(default_x=13.8, default_y=-270.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=99.12, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=99.12, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=111.71, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=99.12, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='9', width=142.08):
            with Note(default_x=10.36, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=10.36, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=10.36, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=68.45, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=68.45, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=68.45, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='10', width=189.18):
            with Note(default_x=13.8, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-255.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=97.68, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=97.68, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=97.68, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=97.68, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='11', width=309.24):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=95.01, default_y=-270.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=95.01, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=95.01, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=149.69, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=149.69, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=149.69, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=211.2, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=211.2, default_y=-255.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=223.07, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=211.2, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=252.96, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=252.96, default_y=-255.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=264.83, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=252.96, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
        with Measure(number='12', width=212.9):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=30.0)
            with Note(default_x=13.8, default_y=-270.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=103.63, default_y=-270.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=103.63, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=103.63, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=103.63, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='13', width=76.94):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=30.0)
            with Note(default_x=13.8, default_y=-270.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Note(default_x=13.8, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Note(default_x=13.8, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue')
        with Measure(number='14', width=210.7):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=28.37, default_y=-270.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=28.37, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=28.37, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=96.51, default_y=-275.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=96.51, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=96.51, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=195.11):
            with Note(default_x=17.44, default_y=-280.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=17.44, default_y=-270.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=17.44, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
            with Note(default_x=17.44, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=102.55, default_y=-285.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=115.14, default_y=-280.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=102.55, default_y=-270.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=102.55, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='16', width=276.43):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=106.69, default_y=-290.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=106.69, default_y=-280.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=106.69, default_y=-270.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=119.28, default_y=-265.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=181.26, default_y=-290.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=181.26, default_y=-280.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=181.26, default_y=-270.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=193.85, default_y=-265.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='17', width=190.38):
            with Note(default_x=13.8, default_y=-285.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-275.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-265.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=78.62, default_y=-290.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=78.62, default_y=-275.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=78.62, default_y=-265.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='18', width=151.29):
            with Note(default_x=16.87, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=16.87, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=16.87, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=29.46, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=83.1, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=83.1, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=83.1, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=95.69, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='19', width=182.61):
            with Note(default_x=16.87, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=16.87, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=16.87, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=107.62, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=107.62, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=107.62, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='20', width=204.18):
            with Note(default_x=10.0, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=10.0, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=10.0, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.03, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.16, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=56.03, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.03, default_y=-215.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=101.69, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=101.69, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=101.69, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=114.28, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='21', width=225.88):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=91.21, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=91.21, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=91.21, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=161.47, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=161.47, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=161.47, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='22', width=187.7):
            with Note(default_x=17.59, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=17.59, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=17.59, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=17.59, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=92.32, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=92.32, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=92.32, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='23', width=224.79):
            with Note(default_x=16.87, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=16.87, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=16.87, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=113.88, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=113.88, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=113.88, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=113.88, default_y=-215.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='24', width=221.51):
            with Note(default_x=13.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=114.06, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=114.06, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=114.06, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=151.96, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=151.96, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=151.96, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=151.96, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='25', width=145.03):
            with Note(default_x=10.36, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=10.36, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=10.36, default_y=-215.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=80.62, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=80.62, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=80.62, default_y=-215.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='26', width=273.04):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=91.21, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=91.21, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=91.21, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=174.48, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=174.48, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=174.48, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=174.48, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='27', width=186.22):
            with Note(default_x=17.59, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=17.59, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=17.59, default_y=-215.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=95.87, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=95.87, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=95.87, default_y=-215.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=95.87, default_y=-205.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='28', width=215.76):
            with Note(default_x=42.57, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=42.57, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=29.98, default_y=-215.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=42.57, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=123.33, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=123.33, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=123.33, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=123.33, default_y=-200.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='29', width=145.71):
            with Note(default_x=10.0, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Note(default_x=10.0, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Note(default_x=10.0, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='30', width=184.15):
            with Note(default_x=13.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=26.39, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=96.79, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=96.79, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=96.79, default_y=-215.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=96.79, default_y=-205.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='31', width=302.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=91.21, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=91.21, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=91.21, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=195.99, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
            with Note(default_x=195.99, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=195.99, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='32', width=201.16):
            with Note(default_x=22.95, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=22.95, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=10.36, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=22.95, default_y=-215.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=97.36, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=84.78, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
            with Note(default_x=97.36, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=97.36, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='33', width=126.92):
            with Note(default_x=13.8, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=13.8, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=13.8, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=69.38, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=69.38, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=69.38, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='34', width=159.43):
            with Note(default_x=10.0, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Note(default_x=10.0, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Note(default_x=10.0, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Note(default_x=28.51, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='35', width=214.59):
            with Note(default_x=13.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=13.8, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=26.39, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=105.46, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.46, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.46, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=155.3, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=155.3, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=155.3, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='36', width=602.97):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=91.21, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=91.21, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=91.21, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=342.33, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=354.2, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=354.2, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=354.2, default_y=-215.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=477.78, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=477.78, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=477.78, default_y=-215.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=477.78, default_y=-205.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='37', width=401.92):
            with Note(default_x=13.8, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Note(default_x=13.8, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Note(default_x=13.8, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')