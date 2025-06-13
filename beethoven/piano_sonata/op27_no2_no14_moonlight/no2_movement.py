with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Sonata No. 14 "Moonlight Sonata"')
    MovementNumber('2')
    MovementTitle('Allegretto')
    with Identification():
        Creator('Ludwig van Beethoven', type='composer')
        Rights('Public Domain')
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-15')
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
        Source('http://imslp.org/wiki/Piano_Sonata_No.14,_Op.27_No.2_(Beethoven,_Ludwig_van)')
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
        CreditWords('Sonata No. 14 "Moonlight Sonata"', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('2nd Movement, Opus 27, No. 2', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Ludwig van Beethoven\n', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
        CreditWords('(1770 - 1827)')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Public Domain', default_x=595.44, default_y=113.386, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Public Domain', default_x=595.44, default_y=113.386, justify='center', valign='bottom', font_size='8')
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
        with Measure(number='1', width=166.61):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(177.97)
                with StaffLayout(number=2):
                    StaffDistance(73.23)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-5)
                with Time():
                    Beats('3')
                    BeatType('4')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=-16.13, relative_y=-21.85):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Allegretto\n', default_x=-36.0, default_y=3.94, relative_x=-33.5, relative_y=56.83, font_weight='bold', font_size='12')
                    Words('La prima parte senza repetizione')
                Staff(1)
                Sound(tempo=120.0)
            with Note(default_x=139.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=139.83, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=139.83, default_y=-88.23):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
        with Measure(number='2', width=77.63):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=52.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=52.86, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-93.23):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=52.86, default_y=-98.23):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=83.71):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=58.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=58.95, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-103.23):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=58.95, default_y=-133.23):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=58.95, default_y=-108.23):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='4', width=89.88):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=64.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=64.12, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-128.23):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-93.23):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=64.12, default_y=-128.23):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=64.12, default_y=-98.23):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=117.43):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=88.96, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=88.96, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-113.23):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-103.23):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=88.96, default_y=-133.23):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
        with Measure(number='6', width=62.37):
            with Note(default_x=12.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=12.36, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=37.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=37.6, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-138.23):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=37.6, default_y=-143.23):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='7', width=83.71):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=58.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=58.95, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-148.23):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=58.95, default_y=-178.23):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=58.95, default_y=-153.23):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='8', width=83.71):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=58.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=58.95, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-173.23):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-138.23):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=58.95, default_y=-173.23):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=58.95, default_y=-143.23):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='9', width=115.07):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=86.51, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=86.51, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.0, default_y=-158.23):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=12.0, default_y=-148.23):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=86.51, default_y=-123.23):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=86.51, default_y=-113.23):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=92.66):
            with Note(default_x=12.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=12.72, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=38.84, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=38.84, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=64.95, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=64.95, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-128.23):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=12.36, default_y=-113.23):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=64.95, default_y=-133.23):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=64.95, default_y=-118.23):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=83.71):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.37, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=58.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=58.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-138.23):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=3)
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-103.23):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=58.95, default_y=-133.23):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=58.95, default_y=-108.23):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=200.56):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(98.44)
                with StaffLayout(number=2):
                    StaffDistance(76.8)
            with Note(default_x=118.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=145.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=172.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=118.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=172.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(6.0)
            with Note(default_x=118.78, default_y=-131.8):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=118.78, default_y=-96.8):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=172.23, default_y=-131.8):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=172.23, default_y=-101.8):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=84.93):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=60.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=60.16, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-116.8):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-106.8):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=60.16, default_y=-111.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=60.16, default_y=-101.8):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=84.21):
            with Note(default_x=16.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=16.16, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=37.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=59.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.44, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-116.8):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-101.8):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=59.44, default_y=-121.8):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=59.44, default_y=-106.8):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=92.59):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=40.86, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=65.93, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=65.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-126.8):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-91.8):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=65.93, default_y=-121.8):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=65.93, default_y=-96.8):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=84.93):
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.98, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=60.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=60.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-116.8):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-81.8):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=60.16, default_y=-116.8):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=60.16, default_y=-86.8):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=61.03):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(4.0)
            with Note(default_x=15.8, default_y=-101.8):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-91.8):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='18', width=56.55):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=29.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=29.37, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=29.37, default_y=-101.8):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
        with Measure(number='19', width=63.59):
            with Note(default_x=12.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=38.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=38.82, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-111.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=38.82, default_y=-116.8):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='20', width=97.23):
            with Note(default_x=14.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=40.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=3)
            with Note(default_x=69.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.64, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=69.25, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=14.0, default_y=-121.8):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=40.38, default_y=-116.8):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=69.25, default_y=-116.8):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='21', width=81.41):
            with Note(default_x=15.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=55.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.84, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=55.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.84, default_y=-116.8):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=55.35, default_y=-121.8):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=84.61):
            with Note(default_x=16.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=38.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=59.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Backup():
                Duration(6.0)
            with Note(default_x=16.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=59.84, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=16.56, default_y=-126.8):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=38.2, default_y=-121.8):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=59.84, default_y=-121.8):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
        with Measure(number='23', width=64.86):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-44.12, relative_x=-4.96, relative_y=-35.23):
                        OtherDynamics('cresc.')
                Staff(1)
            with Note(default_x=13.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=40.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=40.1, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.64, default_y=-131.8):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=13.64, default_y=-116.8):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=40.1, default_y=-136.8):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=40.1, default_y=-116.8):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='24', width=170.27):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(98.44)
                with StaffLayout(number=2):
                    StaffDistance(83.05)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-48.62, relative_x=-5.0, relative_y=-36.93):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-80.55)
                Staff(1)
            with Note(default_x=118.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=145.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-21.0)
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=118.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=145.51, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=118.78, default_y=-148.05):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=118.78, default_y=-123.05):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='25', width=103.42):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.17, relative_x=0.97, relative_y=-45.38):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=12.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=62.96, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=78.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.72, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.84, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=62.96, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-123.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=62.96, default_y=-128.05):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=78.66, default_y=-138.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-143.05):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=62.96, default_y=-163.05):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=89.78):
            with Note(default_x=12.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.72, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=37.87, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=37.87, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=63.03, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=63.03, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-123.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=63.03, default_y=-133.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=63.03, default_y=-123.05):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-158.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(2.0)
        with Measure(number='27', width=79.11):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=53.92, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=53.92, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-138.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-123.05):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=53.92, default_y=-143.05):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=53.92, default_y=-128.05):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='28', width=85.2):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=60.43, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(6.0)
            with Forward():
                Duration(4.0)
            with Note(default_x=60.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-148.05):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-113.05):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=60.43, default_y=-143.05):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=60.43, default_y=-118.05):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='29', width=97.85):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=42.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=69.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=69.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-138.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-103.05):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=69.43, default_y=-138.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=69.43, default_y=-108.05):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='30', width=100.38):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=42.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=71.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=71.72, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-123.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-113.05):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=71.72, default_y=-118.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=71.72, default_y=-108.05):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='31', width=75.62):
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=50.85, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=50.85, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-123.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-108.05):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=50.85, default_y=-128.05):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=50.85, default_y=-113.05):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='32', width=85.2):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=60.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=60.43, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-133.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-108.05):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=60.43, default_y=-118.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=60.43, default_y=-108.05):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='33', width=84.48):
            with Note(default_x=16.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=16.16, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.94, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=37.94, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=59.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=59.71, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-123.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-108.05):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=59.71, default_y=-128.05):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=59.71, default_y=-113.05):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='34', width=85.2):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-45.84, relative_x=-28.3, relative_y=-29.76):
                        OtherDynamics('cresc.')
                Staff(1)
            with Note(default_x=60.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=60.43, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-133.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-108.05):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=60.43, default_y=-118.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=60.43, default_y=-108.05):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='35', width=202.95):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(98.44)
                with StaffLayout(number=2):
                    StaffDistance(161.16)
            with Note(default_x=119.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=119.14, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=146.54, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=146.54, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-44.63, relative_x=-4.12, relative_y=-31.07):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=173.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=173.94, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=118.78, default_y=-201.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=118.78, default_y=-186.16):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=173.94, default_y=-206.16):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    Slur(type='start', placement='above', number=3)
                    Slur(type='start', placement='below', number=4)
                    Slur(type='start', placement='above', number=5)
            with Note(default_x=162.08, default_y=-186.16):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=173.94, default_y=-181.16):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='36', width=92.3):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=40.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=40.77, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-201.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=3)
                    Slur(type='stop', number=4)
                    Slur(type='stop', number=5)
            with Note(default_x=15.8, default_y=-186.16):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-176.16):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='37', width=92.08):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.33, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=67.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-271.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-236.16):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='38', width=78.52):
            with Note(default_x=15.8, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=15.8, default_y=-256.16):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-236.16):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Words('Fine', default_y=-40.0, relative_x=-28.01, relative_y=-155.12)
                Sound(fine='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='39', width=53.02):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-28.67, relative_y=-49.12):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Trio.', relative_x=-1.12, relative_y=27.68)
                Staff(1)
            with Note(default_x=24.37, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=24.37, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(2.0)
            with Note():
                Rest(measure='yes')
                Duration(2.0)
                Voice('5')
                Staff(2)
        with Measure(number='40', width=73.98):
            with Note(default_x=15.8, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-41.18, relative_x=-10.47, relative_y=-53.22):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=49.22, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=49.22, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-45.88, relative_x=3.17, relative_y=-56.07):
                        Fp()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-236.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-256.16):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='41', width=65.66):
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-45.76, relative_x=-3.07, relative_y=-38.04):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=40.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=40.89, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-236.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-251.16):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='42', width=87.78):
            with Note(default_x=12.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.36, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=36.97, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=36.97, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=61.58, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=61.58, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.0, default_y=-236.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=24.59, default_y=-241.16):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='43', width=79.4):
            with Note(default_x=12.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=12.72, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=33.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=33.68, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-42.6, relative_x=-12.67, relative_y=-56.8):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=54.64, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=54.64, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-236.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-246.16):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='44', width=73.98):
            with Note(default_x=15.8, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.39, relative_x=-8.82, relative_y=-54.01):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=49.22, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=49.22, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=5.33, relative_y=-62.01):
                        Fp()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-236.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-256.16):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='45', width=69.61):
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-51.32, relative_x=-8.53, relative_y=-42.93):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=44.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.85, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-236.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-251.16):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='46', width=87.21):
            with Note(default_x=16.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=16.16, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=39.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=39.3, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=62.45, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=62.45, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-236.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=62.45, default_y=-236.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-271.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=62.45, default_y=-236.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='47', width=186.42):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(98.44)
                with StaffLayout(number=2):
                    StaffDistance(77.3)
            with Note(default_x=122.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=122.94, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=145.89, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=145.89, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=122.58, default_y=-152.3):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(4.0)
            with Note(default_x=122.58, default_y=-172.3):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='48', width=53.92):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-42.78, relative_x=-2.79, relative_y=-36.57):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=24.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=24.37, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(2.0)
            with Note():
                Rest(measure='yes')
                Duration(2.0)
                Voice('5')
                Staff(2)
        with Measure(number='49', width=66.08):
            with Note(default_x=14.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=14.36, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=41.32, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=41.32, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=4.93, relative_y=-30.69):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=14.36, default_y=-137.3):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=14.36, default_y=-117.3):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='50', width=66.91):
            with Note(default_x=14.36, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=14.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=42.15, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=42.15, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=14.36, default_y=-137.3):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=14.36, default_y=-122.3):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='51', width=69.11):
            with Note(default_x=16.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=16.56, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=44.35, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=44.35, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=16.56, default_y=-142.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=16.56, default_y=-122.3):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='52', width=73.07):
            with Note(default_x=16.56, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=16.56, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=48.3, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=48.3, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=16.56, default_y=-142.3):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=16.56, default_y=-127.3):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='53', width=68.87):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-60.15, relative_x=8.26, relative_y=-34.25):
                        Fp()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=12.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.36, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=44.1, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=44.1, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-58.07, relative_y=-40.0):
                        Fp()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=12.36, default_y=-137.3):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-147.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
        with Measure(number='54', width=76.68):
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=51.91, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=51.91, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-137.3):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-152.3):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='55', width=116.87):
            with Note(default_x=15.8, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=48.3, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=48.3, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=82.77, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=82.77, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.44, default_y=-137.3):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-172.3):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=48.3, default_y=-162.3):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=82.77, default_y=-152.3):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='56', width=98.29):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=42.76, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=42.76, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=69.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=69.72, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.44, default_y=-137.3):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.44, default_y=-157.3):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='57', width=103.61):
            with Note(default_x=12.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.36, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Attributes():
                with Clef(number=1):
                    Sign('F')
                    Line(4)
            with Note(default_x=71.52, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=71.52, default_y=30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-42.45, relative_x=0.9, relative_y=-48.17):
                        Fp()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=12.36, default_y=-137.3):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-147.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
        with Measure(number='58', width=76.68):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=51.91, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=51.91, default_y=25.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-137.3):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-152.3):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='59', width=277.03):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(144.51)
            with Note(default_x=127.58, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=127.58, default_y=25.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=218.7, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=218.7, default_y=20.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=127.58, default_y=-204.51):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=127.58, default_y=-224.51):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='60', width=155.13):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=100.69, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=100.69, default_y=25.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-204.51):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-219.51):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='61', width=155.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=2.79, relative_y=-24.73):
                        OtherDynamics('cresc.')
                Staff(1)
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=25.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=100.69, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=100.69, default_y=30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-204.51):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-214.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
        with Measure(number='62', width=155.13):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=100.69, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=100.69, default_y=25.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-204.51):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-219.51):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='63', width=181.47):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=1.84, relative_y=-21.38):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=16.16, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=16.16, default_y=25.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=70.73, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=70.73, default_y=30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=125.3, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=125.3, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-254.51):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=15.8, default_y=-219.51):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=125.3, default_y=-219.51):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='64', width=132.62):
            with Direction():
                with DirectionType():
                    Words('Allegretto da capo.', default_y=-40.0, relative_x=3.36, relative_y=-135.12, font_style='italic')
                Staff(1)
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=15.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=15.8, default_y=-239.51):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D.C. al Fine', default_y=12.39, relative_y=20.0)
                Sound(dacapo='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')