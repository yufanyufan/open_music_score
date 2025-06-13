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
            Millimeters(4.804)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2472.32)
            PageWidth(1749.03)
            with PageMargins(type='both'):
                LeftMargin(83.264)
                RightMargin(83.264)
                TopMargin(83.264)
                BottomMargin(166.528)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Weihnachts-Oratorium ', default_x=874.513, default_y=2389.06, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('10. Sinfonia', default_x=874.513, default_y=2305.8, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditWords('Orgel (Oboen)', default_x=83.264, default_y=2389.06, justify='left', valign='top', font_size='18')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J. S. Bach', default_x=1665.76, default_y=2176.52, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Violine I+II')
            PartAbbreviation('Vln.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Violinen')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(7)
                MidiProgram(49)
                Volume(100.0)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Viola+Cello')
            PartAbbreviation('Vio+Cl\n')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Bratschen')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(9)
                MidiProgram(49)
                Volume(100.0)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Orgel')
            PartAbbreviation('Org.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Orgel')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(11)
                MidiProgram(20)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=364.74):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(112.05)
                        RightMargin(0.0)
                    TopSystemDistance(282.54)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-47.37, default_y=25.05, relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('150')
                with DirectionType():
                    Words('\n', default_x=-47.37, default_y=25.05, relative_y=20.0, font_weight='bold', font_size='12')
                    Words(None)
                Sound(tempo=75.0)
            with Note(default_x=113.59, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=137.4, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=153.07, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=172.59, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=196.4, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=212.07, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=234.99, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=333.8, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
            with Note(default_x=231.59, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=255.73, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=271.4, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=290.92, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=314.73, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=330.4, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=285.42):
            with Note(default_x=20.48, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=45.63, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=61.3, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=82.01, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=107.27, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=122.94, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=143.65, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=257.88, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=122.94, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=151.57, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=176.82, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=192.49, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=213.21, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=238.47, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=257.88, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='3', width=284.89):
            with Note(default_x=10.0, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=45.85, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=61.51, default_y=7.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=81.69, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=103.37, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=127.98, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=148.16, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=184.01, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=199.67, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=219.85, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=235.52, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=260.12, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=10.0, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=30.18, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=61.51, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=127.98, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=148.16, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=168.34, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=199.67, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=260.12, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=260.0):
            with Note(default_x=12.66, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.3, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=52.97, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=73.89, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=98.54, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=114.2, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=134.41, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=174.72, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=194.93, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.3, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=52.97, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=73.89, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=98.54, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=114.2, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=134.41, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=174.72, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=235.23, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='5', width=275.4):
            with Note(default_x=12.66, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=52.97, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=113.48, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=144.54, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=190.12, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=210.32, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-31.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=52.97, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=73.18, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=141.14, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=190.12, default_y=-28.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=250.63, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='6', width=340.41):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(0.0)
                    SystemDistance(95.87)
            with Note(default_x=81.21, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=124.18, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=177.39, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=208.45, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=249.74, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=278.09, default_y=10.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=81.21, default_y=-28.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=124.18, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=142.62, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=205.05, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=239.82, default_y=10.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=278.09, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=312.87, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='7', width=263.61):
            with Note(default_x=12.96, default_y=10.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=56.41, default_y=7.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=116.42, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=147.48, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=168.21, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=183.88, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=204.07, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=223.18, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=238.85, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.96, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=56.41, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=81.65, default_y=7.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(18.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=144.08, default_y=7.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=183.88, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=204.07, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=238.85, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='8', width=294.22):
            with Note(default_x=12.66, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=45.83, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=96.97, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=150.19, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=169.29, default_y=-31.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=184.96, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=223.23, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=242.34, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=266.68, default_y=-28.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=20.58, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=61.5, default_y=-31.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=78.53, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=96.97, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=116.08, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=131.74, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=150.19, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=184.96, default_y=-31.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=223.23, default_y=-31.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=266.68, default_y=-35.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
        with Measure(number='9', width=236.19):
            with Note(default_x=12.66, default_y=-31.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-42.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
            with Forward():
                Duration(36.0)
        with Measure(number='10', width=367.16):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='11', width=352.1):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(0.0)
                    SystemDistance(95.87)
            with Note(default_x=85.01, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=113.72, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=129.38, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=152.92, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=181.63, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=199.24, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=240.35, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=85.01, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.38, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=152.92, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=199.24, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=236.95, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(18.0)
        with Measure(number='12', width=440.97):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='13', width=304.42):
            with Note(default_x=13.8, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=46.56, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=65.98, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=92.85, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=125.62, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=142.41, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=169.28, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=65.98, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=92.85, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=142.41, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=169.28, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
        with Measure(number='14', width=404.1):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=369.14, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='15', width=426.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(0.0)
                    SystemDistance(95.87)
            with Note(default_x=83.44, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=119.03, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=137.27, default_y=7.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=166.46, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=193.76, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=229.35, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=258.54, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=294.13, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=312.38, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=341.56, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=359.81, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=395.4, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=137.27, default_y=-28.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=166.46, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=258.54, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=312.38, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=395.4, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='16', width=304.27):
            with Note(default_x=12.66, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=46.54, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=63.9, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=91.68, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=125.56, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=142.92, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=170.7, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=208.9, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=46.54, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=63.9, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=91.68, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=125.56, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=142.92, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=170.7, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=208.9, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(18.0)
        with Measure(number='17', width=393.85):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=262.76, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=296.44, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=337.51, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=358.56, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='18', width=377.29):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=72.77, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=103.83, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=156.57, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=175.98, default_y=7.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=207.03, default_y=7.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=238.09, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=10.66, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=41.71, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=72.77, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=103.83, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=134.89, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=175.98, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=207.03, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
        with Measure(number='19', width=539.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(0.0)
                    SystemDistance(95.87)
            with Note(default_x=82.96, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=128.08, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=151.2, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=188.2, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=248.33, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=271.46, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=311.86, default_y=-28.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
            with Note(default_x=308.46, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=353.57, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=376.7, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=413.7, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=458.82, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=481.94, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='20', width=477.95):
            with Note(default_x=13.8, default_y=7.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=87.87, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=128.04, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=202.11, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=245.67, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=326.26, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=359.91, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=440.5, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-28.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
            with Note(default_x=242.27, default_y=7.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=316.34, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=356.51, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=430.58, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='21', width=484.2):
            with Note(default_x=17.2, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=87.64, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=127.68, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=176.5, default_y=7.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=211.53, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=254.58, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=87.64, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=127.68, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=211.53, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=263.0, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=368.72, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=417.54, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=442.56, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='22', width=846.54):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=91.68, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=223.71, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=280.0, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=402.1, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=468.31, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=549.04, default_y=14.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=590.42, default_y=10.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=656.63, default_y=10.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=737.35, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=778.73, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=91.68, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=213.79, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=280.0, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=468.31, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=549.04, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=590.42, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=656.63, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=737.35, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=778.73, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='23', width=655.05):
            with Note(default_x=13.8, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=333.62, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=402.18, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=437.32, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=493.54, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=562.09, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=597.23, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=82.35, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=117.49, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=173.71, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=242.27, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=277.4, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=333.62, default_y=-28.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
        with Measure(number='24', width=434.43):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=79.64, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=235.74, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=270.13, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=298.86, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=317.6, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=347.57, default_y=-28.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=384.12, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=402.85, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('2')
                Type('eighth')
            with Note():
                Rest()
                Duration(3.0)
                Voice('2')
                Type('16th')
            with Note(default_x=128.35, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=147.08, default_y=-28.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=177.06, default_y=-31.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=213.61, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=232.34, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=262.31, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=402.85, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='25', width=351.73):
            with Note(default_x=12.66, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=155.13, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=184.79, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=217.56, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=236.1, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=265.76, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=301.93, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=320.47, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=20.58, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=48.83, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=67.37, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=97.03, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=133.19, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=151.73, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=181.39, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=320.47, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='26', width=384.92):
            with Note(default_x=12.66, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=44.12, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=83.44, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=114.9, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=204.37, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=242.73, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=262.39, default_y=10.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=293.85, default_y=7.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=332.21, default_y=10.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=351.87, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=63.78, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=83.44, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=114.9, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=153.25, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=172.91, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=204.37, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=262.39, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=293.85, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=351.87, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='27', width=330.51):
            with Note(default_x=12.66, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=46.07, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=63.19, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=90.58, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=123.99, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=145.67, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=173.06, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=250.99, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=284.39, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=301.52, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=63.19, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=90.58, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=145.67, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=173.06, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=206.47, default_y=-31.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=223.59, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=250.99, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=284.39, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=301.52, default_y=-28.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='28', width=404.65):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=82.96, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=82.96, default_y=-31.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(54.0)
        with Measure(number='29', width=377.2):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=198.18, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=236.21, default_y=7.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=255.7, default_y=17.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=286.89, default_y=17.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=324.92, default_y=14.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=344.41, default_y=17.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=198.18, default_y=-31.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=255.7, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=286.89, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=344.41, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='30', width=360.49):
            with Note(default_x=17.12, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=17.12, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(54.0)
        with Measure(number='31', width=359.25):
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=160.88, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=189.63, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=224.69, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=242.65, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=271.4, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=300.15, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=328.9, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=242.65, default_y=-31.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=271.4, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='32', width=367.31):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=79.64, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=109.4, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=125.06, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=149.47, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=173.87, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=198.27, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=222.67, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=252.43, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=268.1, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=292.5, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=316.9, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=341.3, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=79.64, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=125.06, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=198.27, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=222.67, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=268.1, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=341.3, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='33', width=332.07):
            with Note(default_x=15.62, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=60.32, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=15.62, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=60.32, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(54.0)
        with Measure(number='34', width=405.96):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=83.42, default_y=10.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=118.23, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=208.73, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=235.72, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(18.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=166.1, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=200.91, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=235.72, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=270.53, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=305.34, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='35', width=396.26):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='36', width=511.42):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='37', width=493.47):
            with Note(default_x=16.64, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=67.57, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=93.68, default_y=10.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=135.45, default_y=10.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=186.38, default_y=7.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=212.49, default_y=10.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=257.65, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
            with Note(default_x=254.25, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=305.19, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=331.29, default_y=10.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=373.06, default_y=10.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=423.99, default_y=7.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=450.1, default_y=10.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='38', width=496.7):
            with Note(default_x=16.64, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=93.54, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=135.24, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=212.13, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=257.23, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=340.65, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=375.82, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=459.24, default_y=-17.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=16.64, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
            with Note(default_x=253.83, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=330.73, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=372.42, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=449.32, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='39', width=556.56):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=86.36, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=159.15, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=200.46, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=250.83, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=276.65, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=317.71, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=82.96, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=159.15, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=200.46, default_y=-24.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=276.65, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=326.13, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=437.46, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=487.83, default_y=-17.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=513.65, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='40', width=507.16):
            with Note(default_x=21.03, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=111.23, default_y=-17.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=142.63, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=218.84, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=260.16, default_y=-24.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=310.55, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=336.37, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=388.02, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=438.41, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=464.23, default_y=-17.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=21.03, default_y=-17.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=101.31, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=142.63, default_y=-24.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=260.16, default_y=-24.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=310.55, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=336.37, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=388.02, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=438.41, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=464.23, default_y=-17.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='41', width=437.88):
            with Note(default_x=12.66, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
            with Note(default_x=270.61, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=292.65, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=335.96, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=378.96, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=401.01, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(18.0)
            with Note():
                Rest()
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
        with Measure(number='42', width=406.29):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(-0.0)
                    SystemDistance(97.39)
            with Note(default_x=83.44, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=117.41, default_y=14.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=139.09, default_y=10.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=166.95, default_y=10.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=200.93, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=218.34, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=246.2, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=297.59, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=325.45, default_y=7.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=376.83, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=139.09, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=166.95, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=200.93, default_y=-24.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=218.34, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=246.2, default_y=-17.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=297.59, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=325.45, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=376.83, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
        with Measure(number='43', width=507.03):
            with Note(default_x=12.96, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.75, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=12.96, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=105.75, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Forward():
                Duration(54.0)
        with Measure(number='44', width=284.14):
            with Note(default_x=13.8, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=40.63, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=56.3, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=78.3, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=105.13, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=120.79, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=146.2, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=253.19, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
            with Note(default_x=142.8, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=169.63, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=185.29, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=207.3, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=234.13, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=249.79, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='45', width=304.13):
            with Note(default_x=20.48, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=45.63, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=61.3, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=85.45, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=114.91, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=130.57, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=154.73, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=276.59, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=130.57, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=162.64, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=187.9, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=203.56, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=227.72, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=257.18, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=276.59, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='46', width=554.79):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(0.0)
                    SystemDistance(97.39)
            with Note(default_x=79.64, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=153.2, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=212.08, default_y=7.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=238.64, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=260.32, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=290.53, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=317.1, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=390.65, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=449.53, default_y=3.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=476.1, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=496.41, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=526.63, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=79.64, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=106.2, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=121.87, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=137.53, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=161.12, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=180.75, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=196.41, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=212.08, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=290.53, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=317.1, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=343.66, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=359.32, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=374.99, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=398.57, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=418.2, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=433.87, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=449.53, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=526.63, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='47', width=234.41):
            with Note(default_x=12.66, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=36.76, default_y=-3.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=52.42, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=73.35, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=97.45, default_y=-7.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=113.12, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=132.88, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=160.06, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=36.76, default_y=-10.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=52.42, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=73.35, default_y=-17.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=97.45, default_y=-14.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=113.12, default_y=-21.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=132.88, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=160.06, default_y=-24.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(18.0)
        with Measure(number='48', width=354.12):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='49', width=358.27):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=185.63, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=221.1, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=239.28, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=268.36, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=303.83, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=322.01, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=185.63, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=239.28, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=268.36, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=322.01, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='50', width=526.18):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(0.0)
                    SystemDistance(97.39)
            with Note(default_x=90.16, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=86.76, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(54.0)
        with Measure(number='51', width=528.9):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=282.46, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=334.94, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=361.84, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=404.88, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=457.36, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=484.26, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=282.46, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=361.84, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=404.88, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=484.26, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='52', width=446.5):
            with Note(default_x=17.12, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=17.12, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(54.0)
        with Measure(number='53', width=471.7):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(0.0)
                    SystemDistance(97.39)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=244.27, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=282.79, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=343.52, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=437.17, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=343.52, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=376.44, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='54', width=334.38):
            with Note(default_x=14.83, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=97.07, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=175.64, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=226.59, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=305.15, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=11.43, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=69.45, default_y=-17.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=148.02, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=175.64, default_y=-17.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=226.59, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=254.21, default_y=14.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(18.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='55', width=324.34):
            with Note(default_x=16.06, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=62.93, default_y=14.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=90.18, default_y=21.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=167.7, default_y=21.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=217.96, default_y=17.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=295.48, default_y=14.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=14.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=62.93, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=90.18, default_y=7.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=140.45, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=167.7, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=217.96, default_y=7.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=245.22, default_y=17.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(18.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='56', width=371.18):
            with Note(default_x=12.66, default_y=17.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=58.25, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=76.65, default_y=14.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=106.08, default_y=10.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=141.98, default_y=14.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=160.37, default_y=7.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=189.56, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=29.6, default_y=17.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=76.65, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=106.08, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=160.37, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=201.38, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=230.28, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=248.68, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=278.12, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=314.01, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=332.41, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='57', width=345.19):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=82.15, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=111.33, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=127.0, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=150.93, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=180.12, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=195.78, default_y=-17.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=219.72, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=82.15, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=127.0, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=150.93, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=195.78, default_y=-24.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=219.72, default_y=-31.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(18.0)
        with Measure(number='58', width=390.6):
            with Note(default_x=13.32, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=51.6, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=81.21, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=112.6, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=150.88, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=170.51, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=212.43, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
            with Note(default_x=209.03, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=247.31, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=266.93, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=298.32, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=336.6, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=356.22, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='59', width=360.87):
            with Note(default_x=13.8, default_y=14.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.06, default_y=10.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=95.94, default_y=10.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=149.21, default_y=7.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=178.09, default_y=7.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=231.35, default_y=7.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=260.23, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=323.41, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
            with Note(default_x=186.0, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=231.35, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=260.23, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=313.5, default_y=7.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='60', width=404.93):
            with Note(default_x=16.2, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=75.14, default_y=10.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
            with Note(default_x=107.09, default_y=10.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=146.05, default_y=14.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=171.52, default_y=7.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=209.17, default_y=7.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=16.2, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.14, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=107.09, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=146.05, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=179.43, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=209.43, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=277.13, default_y=-17.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=312.44, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=371.38, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='61', width=660.04):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(80.91)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=81.21, default_y=7.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=174.78, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=225.52, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=319.09, default_y=7.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=369.82, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=435.09, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=466.8, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=517.53, default_y=-17.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=579.39, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=611.1, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=81.21, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=225.52, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=287.38, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=319.09, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=369.82, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=431.69, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=463.4, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=514.13, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=575.99, default_y=7.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=607.7, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='62', width=549.49):
            with Note(default_x=16.06, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=68.05, default_y=-3.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=96.44, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=141.86, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=197.25, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=225.64, default_y=-24.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=271.06, default_y=-21.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=68.05, default_y=-10.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=96.44, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=141.86, default_y=-14.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=197.25, default_y=-31.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=225.64, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=271.06, default_y=-31.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(18.0)
        with Measure(number='63', width=292.06):
            with Note(default_x=13.91, default_y=3.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=13.91, default_y=-7.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
            with Forward():
                Duration(36.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=364.74):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(71.95)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=113.59, default_y=-89.45, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=172.59, default_y=-89.45, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=231.59, default_y=-85.96, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=290.92, default_y=-85.96, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(72.0)
            with Note(default_x=113.59, default_y=-103.45, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=153.07, default_y=-106.95, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=172.59, default_y=-106.95, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=212.07, default_y=-110.45, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=231.59, default_y=-110.45, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=271.4, default_y=-113.95, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=290.92, default_y=-113.95, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=330.4, default_y=-117.45, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='2', width=285.42):
            with Note(default_x=12.66, default_y=-85.96, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=82.01, default_y=-89.45, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=143.65, default_y=-89.45, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=213.21, default_y=-89.45, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-117.45, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=61.3, default_y=-124.45, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=82.01, default_y=-113.95, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=122.94, default_y=-138.46, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=143.65, default_y=-127.95, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=213.21, default_y=-120.95, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='3', width=284.89):
            with Note(default_x=10.0, default_y=-103.45, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=81.69, default_y=-92.95, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=148.16, default_y=-106.95, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=219.85, default_y=-96.46, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(72.0)
            with Note(default_x=10.0, default_y=-117.45, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=81.69, default_y=-124.45, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=148.16, default_y=-120.95, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=219.85, default_y=-127.95, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='4', width=260.0):
            with Note(default_x=12.66, default_y=-103.45, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.97, default_y=-89.45, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=73.89, default_y=-89.45, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=114.2, default_y=-85.96, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=134.41, default_y=-89.45, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=174.72, default_y=-82.46, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=194.93, default_y=-75.46, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-134.96, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=52.97, default_y=-131.46, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=73.89, default_y=-127.95, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=114.2, default_y=-141.95, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=134.41, default_y=-138.46, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=159.05, default_y=-124.45, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=174.72, default_y=-113.95, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=194.93, default_y=-113.95, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=219.57, default_y=-117.45, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=235.23, default_y=-113.95, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='5', width=275.4):
            with Note(default_x=12.66, default_y=-75.46, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=52.97, default_y=-78.96, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=113.48, default_y=-82.46, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=141.14, default_y=-85.96, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=190.12, default_y=-78.96, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=210.32, default_y=-71.95, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-127.95, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=37.3, default_y=-120.95, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=52.97, default_y=-113.95, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=73.18, default_y=-113.95, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=97.82, default_y=-117.45, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=113.48, default_y=-113.95, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=141.14, default_y=-134.96, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=165.78, default_y=-120.95, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=190.12, default_y=-110.45, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=210.32, default_y=-110.45, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=234.97, default_y=-113.95, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=250.63, default_y=-110.45, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='6', width=340.41):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(83.89)
            with Note(default_x=81.21, default_y=-83.89, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=124.18, default_y=-87.39, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=177.39, default_y=-90.89, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=205.05, default_y=-97.89, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=239.82, default_y=-101.39, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=278.09, default_y=-104.89, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=312.87, default_y=-97.89, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=81.21, default_y=-136.39, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=108.51, default_y=-129.39, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=124.18, default_y=-122.39, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=142.62, default_y=-122.39, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=161.73, default_y=-125.89, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=177.39, default_y=-122.39, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=205.05, default_y=-129.39, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=224.15, default_y=-122.39, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=239.82, default_y=-115.39, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=278.09, default_y=-115.39, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=297.2, default_y=-118.89, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=312.87, default_y=-115.39, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=263.61):
            with Note(default_x=12.96, default_y=-90.89, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.81, default_y=-115.39, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=119.82, default_y=-111.89, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=144.08, default_y=-101.39, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.88, default_y=-101.39, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=204.07, default_y=-87.39, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=12.96, default_y=-122.39, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.07, default_y=-115.39, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=56.41, default_y=-104.89, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=81.65, default_y=-104.89, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=100.76, default_y=-108.39, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=116.42, default_y=-104.89, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=144.08, default_y=-101.39, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.88, default_y=-108.39, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=204.07, default_y=-111.89, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=238.85, default_y=-115.39, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='8', width=294.22):
            with Note(default_x=12.66, default_y=-87.39, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=61.5, default_y=-94.39, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=78.53, default_y=-101.39, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=96.97, default_y=-94.39, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=131.74, default_y=-108.39, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=150.19, default_y=-111.89, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=194.88, default_y=-115.39, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=223.23, default_y=-111.89, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=266.68, default_y=-115.39, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-118.89, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.53, default_y=-115.39, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=96.97, default_y=-118.89, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=131.74, default_y=-122.39, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=150.19, default_y=-118.89, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=184.96, default_y=-108.39, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=223.23, default_y=-111.89, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=266.68, default_y=-136.39, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='9', width=236.19):
            with Note(default_x=12.66, default_y=-118.89, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=12.91, default_y=-125.89, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.08, default_y=-129.39, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=63.56, default_y=-132.89, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=94.73, default_y=-136.39, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=114.21, default_y=-139.89, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
        with Measure(number='10', width=367.16):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='11', width=352.1):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=85.01, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=152.92, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=236.95, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=85.01, default_y=-96.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.38, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=152.92, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=199.24, default_y=-103.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=236.95, default_y=-103.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(18.0)
        with Measure(number='12', width=440.97):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='13', width=304.42):
            with Note(default_x=13.8, default_y=-79.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=65.98, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=92.85, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.41, default_y=-96.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=169.28, default_y=-72.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-103.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=65.98, default_y=-107.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=92.85, default_y=-107.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=142.41, default_y=-110.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=169.28, default_y=-110.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
        with Measure(number='14', width=404.1):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='15', width=426.19):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.44, default_y=-96.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=166.46, default_y=-93.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=258.54, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=341.56, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(72.0)
            with Note(default_x=83.44, default_y=-110.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=166.46, default_y=-117.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=258.54, default_y=-114.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=341.56, default_y=-121.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='16', width=304.27):
            with Note(default_x=12.66, default_y=-96.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=63.9, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=91.68, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.92, default_y=-79.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=170.7, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-128.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=63.9, default_y=-124.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=91.68, default_y=-121.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=142.92, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=170.7, default_y=-131.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=208.9, default_y=-107.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=236.69, default_y=-103.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=274.89, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='17', width=393.85):
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=262.76, default_y=-79.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=296.44, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=358.56, default_y=-96.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=14.34, default_y=-96.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.71, default_y=-121.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=115.39, default_y=-117.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=161.71, default_y=-114.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=195.39, default_y=-110.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=262.76, default_y=-86.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=296.44, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=358.56, default_y=-103.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='18', width=377.29):
            with Note(default_x=10.66, default_y=-93.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.77, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=103.83, default_y=-86.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=175.98, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=207.03, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=10.66, default_y=-93.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.77, default_y=-96.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=103.83, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=175.98, default_y=-114.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=207.03, default_y=-103.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
        with Measure(number='19', width=539.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=82.96, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=308.46, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=82.96, default_y=-128.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(18.0)
            with Note(default_x=308.46, default_y=-103.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(18.0)
        with Measure(number='20', width=477.95):
            with Note(default_x=13.8, default_y=-93.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=62.77, default_y=-86.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=87.87, default_y=-79.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=128.04, default_y=-79.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=177.01, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=202.11, default_y=-79.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=242.27, default_y=-93.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-128.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
            with Note(default_x=242.27, default_y=-110.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=291.24, default_y=-103.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=316.34, default_y=-93.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=356.51, default_y=-93.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=405.48, default_y=-96.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=430.58, default_y=-93.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=484.2):
            with Note(default_x=13.8, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=254.83, default_y=-75.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-114.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=62.62, default_y=-103.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=87.64, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=127.68, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=176.5, default_y=-93.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=211.53, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=254.83, default_y=-117.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=303.65, default_y=-103.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=328.68, default_y=-86.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=368.72, default_y=-86.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=417.54, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=442.56, default_y=-86.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='22', width=846.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=91.68, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=213.79, default_y=-75.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=280.0, default_y=-79.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=402.1, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=468.31, default_y=-79.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=549.04, default_y=-75.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=590.42, default_y=-72.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=656.63, default_y=-75.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=778.73, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=91.68, default_y=-117.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=213.79, default_y=-93.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=280.0, default_y=-96.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=402.1, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=468.31, default_y=-96.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=590.42, default_y=-103.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=656.63, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=778.73, default_y=-114.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='23', width=655.05):
            with Note(default_x=13.8, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=173.71, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=333.62, default_y=-86.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=493.54, default_y=-96.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-103.5, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=117.49, default_y=-107.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=173.71, default_y=-107.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=277.4, default_y=-110.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=333.62, default_y=-110.5, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=437.32, default_y=-114.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=493.54, default_y=-114.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=597.23, default_y=-117.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='24', width=434.43):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(73.7)
            with Note(default_x=79.64, default_y=-94.7, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=177.06, default_y=-98.2, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=262.31, default_y=-98.2, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=347.57, default_y=-98.2, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(72.0)
            with Note(default_x=79.64, default_y=-129.7, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=147.08, default_y=-133.2, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=177.06, default_y=-122.7, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=232.34, default_y=-122.7, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=262.31, default_y=-136.7, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=317.6, default_y=-122.7, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=347.57, default_y=-112.2, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=402.85, default_y=-115.7, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='25', width=351.73):
            with Note(default_x=12.66, default_y=-87.7, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=97.03, default_y=-91.2, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=181.39, default_y=-91.2, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=265.76, default_y=-91.2, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-119.2, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=67.37, default_y=-126.2, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=97.03, default_y=-115.7, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=151.73, default_y=-140.2, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=181.39, default_y=-129.7, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=236.1, default_y=-115.7, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=265.76, default_y=-105.2, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=320.47, default_y=-108.7, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='26', width=384.92):
            with Note(default_x=12.66, default_y=-80.7, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.44, default_y=-80.7, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=114.9, default_y=-87.7, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=172.91, default_y=-91.2, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=204.37, default_y=-94.7, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=262.39, default_y=-87.7, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=293.85, default_y=-84.2, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=351.87, default_y=-94.7, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-112.2, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.44, default_y=-115.7, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=114.9, default_y=-119.2, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=172.91, default_y=-122.7, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=204.37, default_y=-126.2, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=262.39, default_y=-129.7, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=293.85, default_y=-133.2, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=351.87, default_y=-136.7, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='27', width=330.51):
            with Note(default_x=12.66, default_y=-91.2, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=63.19, default_y=-87.7, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=90.58, default_y=-84.2, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=123.99, default_y=-91.2, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=145.67, default_y=-77.2, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=173.06, default_y=-77.2, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=223.59, default_y=-91.2, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=250.99, default_y=-73.7, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=301.52, default_y=-77.2, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-140.2, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=63.19, default_y=-122.7, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=90.58, default_y=-126.2, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=145.67, default_y=-129.7, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=173.06, default_y=-133.2, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=223.59, default_y=-122.7, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=250.99, default_y=-129.7, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=301.52, default_y=-126.2, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='28', width=404.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=82.96, default_y=-75.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=82.96, default_y=-131.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(54.0)
        with Measure(number='29', width=377.2):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=198.18, default_y=-93.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=286.89, default_y=-93.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=198.18, default_y=-107.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=255.7, default_y=-110.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=286.89, default_y=-110.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=344.41, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='30', width=360.49):
            with Note(default_x=17.12, default_y=-75.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=17.12, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(54.0)
        with Measure(number='31', width=359.25):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=189.63, default_y=-75.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=271.4, default_y=-72.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=189.63, default_y=-89.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=271.4, default_y=-96.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='32', width=367.31):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.95)
            with Note(default_x=79.64, default_y=-85.95, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=149.47, default_y=-75.45, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=222.67, default_y=-89.45, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=292.5, default_y=-78.95, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(72.0)
            with Note(default_x=79.64, default_y=-99.95, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=149.47, default_y=-106.95, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=222.67, default_y=-103.45, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=292.5, default_y=-110.45, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='33', width=332.07):
            with Note(default_x=15.62, default_y=-92.95, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=60.32, default_y=-75.45, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=88.26, default_y=-71.95, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=144.13, default_y=-68.45, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=172.06, default_y=-82.45, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=229.9, default_y=-82.45, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=257.83, default_y=-78.95, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=302.53, default_y=-106.95, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=15.62, default_y=-106.95, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=60.32, default_y=-106.95, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=88.26, default_y=-103.45, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=116.19, default_y=-110.45, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=144.13, default_y=-124.45, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=172.06, default_y=-120.95, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=229.9, default_y=-117.45, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=257.83, default_y=-113.95, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=302.53, default_y=-138.45, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
        with Measure(number='34', width=405.96):
            with Note(default_x=13.8, default_y=-96.45, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.42, default_y=-99.95, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=118.23, default_y=-96.45, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=166.1, default_y=-96.45, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=200.91, default_y=-85.95, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=270.53, default_y=-85.95, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=305.34, default_y=-85.95, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=369.55, default_y=-85.95, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-134.95, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.42, default_y=-131.45, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=118.23, default_y=-127.95, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=166.1, default_y=-103.45, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=200.91, default_y=-99.95, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=270.53, default_y=-110.45, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=305.34, default_y=-124.45, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=369.55, default_y=-117.45, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
        with Measure(number='35', width=396.26):
            with Note(default_x=10.94, default_y=-99.95, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.61, default_y=-99.95, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=106.49, default_y=-96.45, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=174.74, default_y=-103.45, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=205.07, default_y=-99.95, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=265.74, default_y=-96.45, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=296.07, default_y=-92.95, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=364.33, default_y=-96.45, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=10.94, default_y=-113.95, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.61, default_y=-117.45, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=106.49, default_y=-120.95, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=174.74, default_y=-110.45, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=205.07, default_y=-99.95, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=265.74, default_y=-103.45, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=296.07, default_y=-106.95, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=364.33, default_y=-96.45, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='36', width=511.42):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.64, default_y=-93.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=157.86, default_y=-82.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=196.96, default_y=-72.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=284.95, default_y=-75.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=324.06, default_y=-75.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=79.64, default_y=-103.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=157.86, default_y=-107.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.96, default_y=-110.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=284.95, default_y=-100.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=324.06, default_y=-89.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(18.0)
        with Measure(number='37', width=493.47):
            with Note(default_x=16.64, default_y=-75.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=254.25, default_y=-75.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=16.64, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(18.0)
            with Note(default_x=254.25, default_y=-89.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(18.0)
        with Measure(number='38', width=496.7):
            with Note(default_x=16.64, default_y=-79.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=67.48, default_y=-72.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=93.54, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=135.24, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=186.08, default_y=-68.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=212.13, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=253.83, default_y=-79.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=16.64, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
            with Note(default_x=253.83, default_y=-121.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=304.67, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=330.73, default_y=-103.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=372.42, default_y=-103.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=423.26, default_y=-107.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=449.32, default_y=-103.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='39', width=556.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=82.96, default_y=-75.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=317.96, default_y=-86.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=82.96, default_y=-124.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=133.33, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=159.15, default_y=-100.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=200.46, default_y=-100.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=250.83, default_y=-103.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=276.65, default_y=-100.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=317.96, default_y=-128.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=368.33, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=394.15, default_y=-96.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=437.46, default_y=-96.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=487.83, default_y=-100.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=513.65, default_y=-96.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='40', width=507.16):
            with Note(default_x=21.03, default_y=-75.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=101.31, default_y=-86.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=142.63, default_y=-89.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=218.84, default_y=-93.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=260.16, default_y=-89.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=336.37, default_y=-89.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=388.02, default_y=-82.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=464.23, default_y=-75.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=21.03, default_y=-128.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=101.31, default_y=-103.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=142.63, default_y=-107.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=218.84, default_y=-110.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=260.16, default_y=-107.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=336.37, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=388.02, default_y=-100.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=464.23, default_y=-124.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='41', width=437.88):
            with Note(default_x=12.66, default_y=-75.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.67, default_y=-100.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=77.71, default_y=-89.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=112.98, default_y=-89.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=155.98, default_y=-93.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=178.03, default_y=-89.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=213.3, default_y=-128.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
        with Measure(number='42', width=406.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=139.09, default_y=-89.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=166.95, default_y=-79.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=218.34, default_y=-79.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=246.2, default_y=-79.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=297.59, default_y=-79.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=325.45, default_y=-79.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=376.83, default_y=-86.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=139.09, default_y=-103.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=166.95, default_y=-103.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=218.34, default_y=-128.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=246.2, default_y=-117.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=280.17, default_y=-103.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=297.59, default_y=-93.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=325.45, default_y=-93.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=359.42, default_y=-96.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=376.83, default_y=-93.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='43', width=507.03):
            with Note(default_x=12.96, default_y=-93.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=12.96, default_y=-131.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(18.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=341.23, default_y=-107.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=382.47, default_y=-107.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=458.53, default_y=-131.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='44', width=284.14):
            with Note(default_x=13.8, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=78.3, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=142.8, default_y=-79.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=207.3, default_y=-79.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-121.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.3, default_y=-124.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=78.3, default_y=-124.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.79, default_y=-128.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=142.8, default_y=-128.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=185.29, default_y=-131.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=207.3, default_y=-131.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=249.79, default_y=-135.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='45', width=304.13):
            with Note(default_x=12.66, default_y=-79.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=85.45, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=154.73, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=227.72, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-135.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=61.3, default_y=-117.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=85.45, default_y=-107.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=130.57, default_y=-131.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=154.73, default_y=-121.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=227.72, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='46', width=554.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.64, default_y=-96.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=238.64, default_y=-86.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=317.1, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=476.1, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(72.0)
            with Note(default_x=79.64, default_y=-110.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=238.64, default_y=-117.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=317.1, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=476.1, default_y=-121.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='47', width=234.41):
            with Note(default_x=12.66, default_y=-96.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.42, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=73.35, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=113.12, default_y=-79.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=132.88, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-128.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=52.42, default_y=-124.5, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=73.35, default_y=-121.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=113.12, default_y=-110.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=132.88, default_y=-107.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=160.06, default_y=-110.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=179.82, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=206.99, default_y=-117.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='48', width=354.12):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
            with Backup():
                Duration(72.0)
            with Note(default_x=14.34, default_y=-121.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
            with Forward():
                Duration(36.0)
        with Measure(number='49', width=358.27):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=185.63, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=268.36, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=185.63, default_y=-96.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=239.28, default_y=-100.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=268.36, default_y=-100.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=322.01, default_y=-103.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='50', width=526.18):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=86.76, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=86.76, default_y=-103.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(54.0)
        with Measure(number='51', width=528.9):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=282.46, default_y=-79.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=361.84, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=404.88, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=484.26, default_y=-96.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=282.46, default_y=-103.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=361.84, default_y=-107.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=404.88, default_y=-107.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=484.26, default_y=-110.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='52', width=446.5):
            with Note(default_x=17.12, default_y=-72.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=17.12, default_y=-110.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(54.0)
        with Measure(number='53', width=471.7):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(78.65)
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=282.79, default_y=-85.65, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=437.17, default_y=-103.15, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=282.79, default_y=-124.15, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=322.94, default_y=-117.15, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=343.52, default_y=-110.15, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=376.44, default_y=-110.15, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=416.59, default_y=-113.65, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=437.17, default_y=-110.15, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='54', width=334.38):
            with Note(default_x=11.43, default_y=-106.65, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.45, default_y=-99.65, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=97.07, default_y=-92.65, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=175.64, default_y=-92.65, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=226.59, default_y=-96.15, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=305.15, default_y=-75.15, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=11.43, default_y=-131.15, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=45.11, default_y=-117.15, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=69.45, default_y=-106.65, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=97.07, default_y=-106.65, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.75, default_y=-110.15, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=148.02, default_y=-106.65, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=175.64, default_y=-120.65, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=209.32, default_y=-113.65, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=226.59, default_y=-106.65, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=254.21, default_y=-106.65, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=287.89, default_y=-110.15, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=305.15, default_y=-106.65, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='55', width=324.34):
            with Note(default_x=12.66, default_y=-82.15, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=62.93, default_y=-85.65, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=90.18, default_y=-89.15, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=140.45, default_y=-82.15, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=167.7, default_y=-75.15, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=217.96, default_y=-99.65, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=295.48, default_y=-96.15, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-138.15, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=45.89, default_y=-131.15, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=62.93, default_y=-124.15, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=90.18, default_y=-124.15, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=123.41, default_y=-127.65, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=140.45, default_y=-124.15, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=167.7, default_y=-131.15, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=200.93, default_y=-124.15, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=217.96, default_y=-113.65, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=245.22, default_y=-113.65, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=278.45, default_y=-117.15, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=295.48, default_y=-113.65, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='56', width=371.18):
            with Note(default_x=12.66, default_y=-85.65, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=106.08, default_y=-71.65, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=189.81, default_y=-71.65, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=230.28, default_y=-78.65, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=248.68, default_y=-85.65, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=278.12, default_y=-78.65, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=332.41, default_y=-92.65, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-134.65, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.65, default_y=-117.15, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=106.08, default_y=-120.65, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=160.37, default_y=-124.15, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=189.81, default_y=-127.65, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=248.68, default_y=-124.15, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=278.12, default_y=-127.65, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=332.41, default_y=-131.15, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='57', width=345.19):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=82.15, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=127.0, default_y=-79.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=150.93, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=195.78, default_y=-86.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=219.72, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=82.15, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=127.0, default_y=-110.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=150.93, default_y=-110.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=180.12, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=195.78, default_y=-110.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=219.72, default_y=-96.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(18.0)
        with Measure(number='58', width=390.6):
            with Note(default_x=13.32, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=209.03, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=13.32, default_y=-121.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
            with Note(default_x=209.03, default_y=-96.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
        with Measure(number='59', width=360.87):
            with Note(default_x=13.8, default_y=-86.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=49.01, default_y=-79.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=67.06, default_y=-72.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=95.94, default_y=-72.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=131.16, default_y=-75.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=149.21, default_y=-72.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=178.09, default_y=-86.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-121.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
            with Note(default_x=178.09, default_y=-103.5, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=213.3, default_y=-96.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=231.35, default_y=-86.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=260.23, default_y=-86.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=295.45, default_y=-89.5, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=313.5, default_y=-86.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='60', width=404.93):
            with Note(default_x=16.2, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=209.43, default_y=-68.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=16.2, default_y=-107.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.16, default_y=-96.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=75.14, default_y=-82.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=107.09, default_y=-82.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=146.05, default_y=-86.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=171.52, default_y=-82.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=209.43, default_y=-110.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=248.39, default_y=-96.5, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=277.13, default_y=-79.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=312.44, default_y=-79.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=351.4, default_y=-82.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=371.38, default_y=-79.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='61', width=660.04):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.21, default_y=-68.5, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=174.78, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=225.52, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=319.09, default_y=-86.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=369.82, default_y=-72.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=463.4, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=514.13, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=607.7, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(72.0)
            with Note(default_x=81.21, default_y=-110.5, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=225.52, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=319.09, default_y=-117.5, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=369.82, default_y=-114.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=463.4, default_y=-121.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=514.13, default_y=-107.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=607.7, default_y=-131.5, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='62', width=549.49):
            with Note(default_x=12.66, default_y=-82.5, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=68.05, default_y=-75.5, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=96.44, default_y=-72.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=141.86, default_y=-96.5, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=197.25, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=225.64, default_y=-93.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=271.06, default_y=-89.5, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-121.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
            with Note(default_x=271.06, default_y=-121.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(18.0)
        with Measure(number='63', width=292.06):
            with Note(default_x=13.91, default_y=-65.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
            with Backup():
                Duration(72.0)
            with Note(default_x=13.91, default_y=-121.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
            with Forward():
                Duration(36.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=364.74):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-127.95)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(1)
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
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='2', width=285.42):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='3', width=284.89):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='4', width=260.0):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='5', width=275.4):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='6', width=340.41):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(80.65)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='7', width=263.61):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='8', width=294.22):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='9', width=236.19):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Staff(1)
            with Note(default_x=114.21, default_y=-249.89, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=114.21, default_y=-234.89, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=114.21, default_y=-224.89, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=145.37, default_y=-254.89, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=145.37, default_y=-239.89, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=145.37, default_y=-229.89, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=170.65, default_y=-254.89, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=170.65, default_y=-239.89, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=170.65, default_y=-229.89, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=201.82, default_y=-259.89, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=201.82, default_y=-249.89, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=201.82, default_y=-234.89, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Staff(2)
            with Note(default_x=113.85, default_y=-330.54, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(36.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='10', width=367.16):
            with Note(default_x=13.32, default_y=-234.89, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=50.86, default_y=-209.89, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=70.1, default_y=-214.89, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=100.88, default_y=-214.89, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=138.42, default_y=-234.89, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=157.66, default_y=-239.89, dynamics=111.11):
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
            with Note(default_x=188.44, default_y=-234.89, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=225.98, default_y=-209.89, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=245.22, default_y=-214.89, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=276.0, default_y=-214.89, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=313.54, default_y=-234.89, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=332.78, default_y=-239.89, dynamics=111.11):
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
            with Note(default_x=13.32, default_y=-249.89, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=70.1, default_y=-239.89, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=100.88, default_y=-234.89, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=157.66, default_y=-254.89, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=188.44, default_y=-249.89, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=245.22, default_y=-239.89, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=276.0, default_y=-234.89, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=332.78, default_y=-254.89, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=10.0, default_y=-330.54, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(72.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=16.64, default_y=-320.54, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=70.1, default_y=-315.54, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=100.88, default_y=-320.54, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=157.66, default_y=-325.54, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=188.44, default_y=-320.54, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=245.22, default_y=-315.54, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=276.0, default_y=-320.54, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=332.78, default_y=-325.54, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='11', width=352.1):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=85.01, default_y=-241.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=85.01, default_y=-231.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=85.01, default_y=-216.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note(default_x=236.95, default_y=-226.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=236.95, default_y=-216.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=236.95, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=269.31, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=269.31, default_y=-211.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=269.31, default_y=-196.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=294.59, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=294.59, default_y=-211.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=294.59, default_y=-196.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=326.96, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=326.96, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=326.96, default_y=-191.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=85.01, default_y=-296.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=236.59, default_y=-346.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(36.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='12', width=440.97):
            with Note(default_x=17.12, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=17.12, default_y=-191.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=185.14, default_y=-211.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=185.14, default_y=-201.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=219.13, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=219.13, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=290.47, default_y=-196.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=328.91, default_y=-191.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=405.38, default_y=-186.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=405.38, default_y=-176.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=17.12, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=58.57, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=79.81, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=113.8, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=155.24, default_y=-226.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=185.14, default_y=-231.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=219.13, default_y=-226.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=260.57, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=290.47, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=328.91, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(63.0)
            with Note(default_x=13.8, default_y=-346.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(72.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(5)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=79.81, default_y=-336.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=79.81, default_y=-316.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=113.8, default_y=-331.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=113.8, default_y=-321.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=290.47, default_y=-316.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=328.91, default_y=-321.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(3.0)
                Voice('6')
                Type('16th')
                Staff(2)
            with Note(default_x=384.14, default_y=-331.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=405.38, default_y=-336.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='13', width=304.42):
            with Note(default_x=13.8, default_y=-191.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-181.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note(default_x=169.28, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=169.28, default_y=-201.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=169.28, default_y=-191.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=206.23, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=206.23, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=206.23, default_y=-196.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=233.1, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=233.1, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=233.1, default_y=-196.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=270.04, default_y=-226.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=270.04, default_y=-216.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=270.04, default_y=-201.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-346.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Note(default_x=168.92, default_y=-341.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(36.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-331.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Forward():
                Duration(54.0)
        with Measure(number='14', width=404.1):
            with Note(default_x=17.12, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=57.8, default_y=-176.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=78.65, default_y=-181.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=112.01, default_y=-181.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=152.69, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=179.36, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=212.72, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=253.4, default_y=-176.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=274.25, default_y=-181.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=307.61, default_y=-181.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=348.29, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=369.14, default_y=-206.0, dynamics=111.11):
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
            with Note(default_x=17.12, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=78.65, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=112.01, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=179.36, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=212.72, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=274.25, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=307.61, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=369.14, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-341.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(72.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=20.44, default_y=-331.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=78.65, default_y=-326.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=112.01, default_y=-331.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=179.36, default_y=-336.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=212.72, default_y=-331.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=274.25, default_y=-326.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=307.61, default_y=-331.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=369.14, default_y=-336.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='15', width=426.19):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=83.44, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=83.44, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(18.0)
            with Note(default_x=83.44, default_y=-341.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(18.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Note():
                Rest()
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Staff(2)
        with Measure(number='16', width=304.27):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=274.89, default_y=-176.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='17', width=393.85):
            with Note(default_x=14.34, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=48.02, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=14.34, default_y=-231.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=81.71, default_y=-301.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=115.39, default_y=-326.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=195.39, default_y=-326.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=229.07, default_y=-331.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(30.0)
            with Note(default_x=161.71, default_y=-336.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=195.39, default_y=-356.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(18.0)
        with Measure(number='18', width=377.29):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Staff(1)
            with Note(default_x=206.67, default_y=-191.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Staff(2)
            with Note(default_x=207.03, default_y=-331.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=207.03, default_y=-321.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=207.03, default_y=-311.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=269.15, default_y=-326.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=269.15, default_y=-316.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=300.21, default_y=-326.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=300.21, default_y=-316.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=342.91, default_y=-331.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=342.91, default_y=-321.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=342.91, default_y=-311.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='19', width=539.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=79.64, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=79.64, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=151.2, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=151.2, default_y=-211.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=188.2, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=188.2, default_y=-211.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=271.46, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=271.46, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=308.46, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=413.7, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=481.94, default_y=-211.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=79.64, default_y=-191.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(72.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('whole')
                Dot()
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=308.46, default_y=-321.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=376.7, default_y=-321.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=413.7, default_y=-321.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=481.94, default_y=-331.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(72.0)
            with Note(default_x=82.6, default_y=-331.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(36.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=308.46, default_y=-331.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=376.7, default_y=-336.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=413.7, default_y=-336.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=481.94, default_y=-341.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='20', width=477.95):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=10.48, default_y=-191.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(72.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                Dot()
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-226.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-211.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=87.87, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=87.87, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=128.04, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=128.04, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=202.11, default_y=-211.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=202.11, default_y=-201.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=242.27, default_y=-211.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=242.27, default_y=-201.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=316.34, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=356.51, default_y=-211.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=356.51, default_y=-191.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=430.58, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=430.58, default_y=-176.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-281.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=87.87, default_y=-286.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=128.04, default_y=-286.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=202.11, default_y=-291.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=242.27, default_y=-291.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=316.34, default_y=-271.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=356.51, default_y=-281.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=430.58, default_y=-291.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='21', width=484.2):
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=127.68, default_y=-191.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=176.5, default_y=-186.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=211.53, default_y=-181.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=254.47, default_y=-186.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=87.64, default_y=-226.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=87.64, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=127.68, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=211.53, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=254.83, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.48, default_y=-191.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(72.0)
                Tie(type='stop')
                Voice('3')
                Type('whole')
                Dot()
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-271.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=87.64, default_y=-286.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=127.68, default_y=-296.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=211.53, default_y=-321.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=254.83, default_y=-341.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=328.68, default_y=-326.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=328.68, default_y=-316.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=368.72, default_y=-326.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=368.72, default_y=-316.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=442.56, default_y=-316.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=442.56, default_y=-306.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=846.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=91.68, default_y=-196.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=172.41, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=213.79, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=280.0, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=360.73, default_y=-226.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=402.1, default_y=-231.0, dynamics=111.11):
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
            with Note(default_x=402.1, default_y=-221.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=402.1, default_y=-211.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=468.31, default_y=-226.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=468.31, default_y=-216.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=549.04, default_y=-231.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=549.04, default_y=-221.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=549.04, default_y=-211.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=590.42, default_y=-226.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=590.42, default_y=-216.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=590.42, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=656.63, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=656.63, default_y=-211.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=737.35, default_y=-226.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=737.35, default_y=-216.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=778.73, default_y=-221.0, dynamics=111.11):
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
            with Note(default_x=778.73, default_y=-211.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=91.68, default_y=-186.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('4')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(12.0)
            with Note(default_x=91.68, default_y=-326.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=91.68, default_y=-311.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=213.79, default_y=-326.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=280.0, default_y=-321.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=402.1, default_y=-341.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=468.31, default_y=-346.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=590.42, default_y=-346.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=656.63, default_y=-346.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=778.73, default_y=-346.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='23', width=655.05):
            with Note(default_x=13.8, default_y=-226.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-216.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-346.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Note():
                Rest()
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Staff(2)
        with Measure(number='24', width=434.43):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-129.7)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='25', width=351.73):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='26', width=384.92):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='27', width=330.51):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='28', width=404.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=82.96, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=82.96, default_y=-196.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=82.96, default_y=-186.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=124.15, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=124.15, default_y=-201.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=124.15, default_y=-191.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=154.11, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=154.11, default_y=-201.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=154.11, default_y=-191.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=195.31, default_y=-221.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=195.31, default_y=-211.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=195.31, default_y=-196.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=225.26, default_y=-196.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=261.8, default_y=-171.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=285.06, default_y=-176.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=315.02, default_y=-176.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=351.55, default_y=-196.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=370.27, default_y=-201.0, dynamics=111.11):
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
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=225.26, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=285.06, default_y=-201.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=315.02, default_y=-196.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=370.27, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=79.64, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(72.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=225.26, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=285.06, default_y=-321.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=315.02, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=370.27, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='29', width=377.2):
            with Note(default_x=10.36, default_y=-196.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=48.39, default_y=-171.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=78.29, default_y=-176.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=109.47, default_y=-176.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=147.5, default_y=-196.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=166.99, default_y=-201.0, dynamics=111.11):
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
            with Note(default_x=198.18, default_y=-196.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=10.36, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=78.29, default_y=-201.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=109.47, default_y=-196.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=166.99, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=198.18, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(54.0)
            with Note(default_x=10.0, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
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
            with Note(default_x=198.18, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Backup():
                Duration(72.0)
            with Note(default_x=10.72, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=78.29, default_y=-321.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=109.47, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=166.99, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=198.18, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Forward():
                Duration(18.0)
        with Measure(number='30', width=360.49):
            with Note(default_x=17.12, default_y=-196.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=61.03, default_y=-181.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=100.54, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=144.45, default_y=-186.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=176.38, default_y=-221.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=235.28, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=267.22, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=326.12, default_y=-181.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=17.12, default_y=-196.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=61.03, default_y=-201.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=100.54, default_y=-201.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=144.45, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=176.38, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=215.32, default_y=-181.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=235.28, default_y=-186.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=267.22, default_y=-186.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=306.16, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=326.12, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-346.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(72.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=20.44, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=61.03, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=100.54, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=144.45, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=176.38, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=235.28, default_y=-341.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=267.22, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=326.12, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='31', width=359.25):
            with Note(default_x=14.16, default_y=-186.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=79.11, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=107.86, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=160.88, default_y=-181.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=189.63, default_y=-186.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=14.16, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=49.22, default_y=-181.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=79.11, default_y=-186.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=107.86, default_y=-186.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=142.92, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=160.88, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=189.63, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(54.0)
            with Note(default_x=13.8, default_y=-346.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(36.0)
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
            with Note(default_x=189.63, default_y=-346.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Backup():
                Duration(72.0)
            with Note(default_x=14.52, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=79.11, default_y=-341.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=107.86, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=160.88, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=189.63, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Forward():
                Duration(18.0)
        with Measure(number='32', width=367.31):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='33', width=332.07):
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=144.13, default_y=-187.95, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=172.06, default_y=-192.95, dynamics=111.11):
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
            with Note(default_x=200.0, default_y=-212.95, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=229.9, default_y=-217.95, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=257.83, default_y=-212.95, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(66.0)
            with Note(default_x=302.53, default_y=-207.95, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=60.32, default_y=-312.95, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=88.26, default_y=-337.95, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=172.06, default_y=-337.95, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=200.0, default_y=-342.95, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(48.0)
            with Note(default_x=229.9, default_y=-332.95, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=257.83, default_y=-357.95, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(18.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='34', width=405.96):
            with Note(default_x=13.8, default_y=-212.95, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=48.61, default_y=-232.95, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=83.42, default_y=-237.95, dynamics=100.0):
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
            with Note(default_x=118.23, default_y=-232.95, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=270.53, default_y=-342.95, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=305.34, default_y=-342.95, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=347.79, default_y=-347.95, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=369.55, default_y=-327.95, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-357.95, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=48.61, default_y=-362.95, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(54.0)
        with Measure(number='35', width=396.26):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=71.61, default_y=-217.95, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=106.49, default_y=-217.95, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=155.78, default_y=-222.95, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=174.74, default_y=-202.95, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=205.07, default_y=-202.95, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=235.41, default_y=-207.95, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=265.74, default_y=-212.95, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=296.07, default_y=-217.95, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=326.41, default_y=-227.95, dynamics=100.0):
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
            with Note(default_x=364.33, default_y=-202.95, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=10.94, default_y=-327.95, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=41.27, default_y=-332.95, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=71.61, default_y=-337.95, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=106.49, default_y=-342.95, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=136.82, default_y=-352.95, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=265.74, default_y=-337.95, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=296.07, default_y=-337.95, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=345.37, default_y=-342.95, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=364.33, default_y=-322.95, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='36', width=511.42):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=79.64, default_y=-191.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note(default_x=324.06, default_y=-196.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=377.83, default_y=-191.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=416.94, default_y=-191.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=470.71, default_y=-186.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=157.86, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=196.96, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=260.51, default_y=-211.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=284.95, default_y=-191.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=323.7, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=79.64, default_y=-316.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=118.75, default_y=-321.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=157.86, default_y=-326.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=196.96, default_y=-331.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=236.07, default_y=-341.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=284.95, default_y=-316.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=324.06, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=377.83, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=416.94, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=470.71, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=324.06, default_y=-346.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=377.83, default_y=-341.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=416.94, default_y=-341.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=470.71, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='37', width=493.47):
            with Note(default_x=16.64, default_y=-186.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=93.68, default_y=-201.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=135.45, default_y=-201.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=212.49, default_y=-196.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=254.25, default_y=-196.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=331.29, default_y=-196.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=373.06, default_y=-196.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=450.1, default_y=-191.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=13.32, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(72.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('whole')
                Dot()
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=16.64, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=93.68, default_y=-321.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=135.45, default_y=-321.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=212.49, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=254.25, default_y=-311.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=331.29, default_y=-316.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=373.06, default_y=-316.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=450.1, default_y=-321.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(72.0)
            with Note(default_x=16.64, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=93.68, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=135.45, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=212.49, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=254.25, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=373.06, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=450.1, default_y=-346.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='38', width=496.7):
            with Note(default_x=16.64, default_y=-191.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=93.54, default_y=-186.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=135.24, default_y=-186.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=212.13, default_y=-181.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=253.83, default_y=-181.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=330.73, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=372.42, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=449.32, default_y=-191.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=13.32, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(72.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('whole')
                Dot()
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=16.64, default_y=-321.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=93.54, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=135.24, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=212.13, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=253.83, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=330.73, default_y=-311.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=372.42, default_y=-321.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=449.32, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(72.0)
            with Note(default_x=16.64, default_y=-346.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=93.54, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=135.24, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=212.13, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=253.83, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=330.73, default_y=-346.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=372.42, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=449.32, default_y=-321.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='39', width=556.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=82.96, default_y=-196.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=159.15, default_y=-186.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=200.46, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=250.83, default_y=-201.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=276.65, default_y=-196.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=317.6, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=79.64, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Tie(type='stop')
                Voice('2')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(24.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=82.96, default_y=-311.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=159.15, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=200.46, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=317.96, default_y=-321.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=394.15, default_y=-306.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=437.46, default_y=-341.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=437.46, default_y=-331.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=513.65, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=513.65, default_y=-321.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(72.0)
            with Note(default_x=82.96, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=159.15, default_y=-346.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=200.46, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=276.65, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=317.96, default_y=-321.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=394.15, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(18.0)
        with Measure(number='40', width=507.16):
            with Note(default_x=21.03, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=101.31, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=142.63, default_y=-196.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=218.84, default_y=-181.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=260.16, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=260.16, default_y=-186.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=310.55, default_y=-211.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=310.55, default_y=-201.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=336.37, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=336.37, default_y=-196.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=388.02, default_y=-196.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=438.41, default_y=-191.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=464.23, default_y=-226.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=464.23, default_y=-201.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=21.03, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('3')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=71.42, default_y=-181.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=101.31, default_y=-186.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=142.63, default_y=-186.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=193.02, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=218.84, default_y=-211.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Forward():
                Duration(18.0)
            with Note(default_x=388.02, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('3')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(66.0)
            with Note(default_x=21.03, default_y=-341.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=218.84, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=260.16, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=388.02, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(72.0)
            with Note(default_x=21.03, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(12.0)
            with Note(default_x=218.84, default_y=-341.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=260.16, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=310.55, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=336.37, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=362.2, default_y=-341.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=388.02, default_y=-346.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=464.23, default_y=-341.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='41', width=437.88):
            with Note(default_x=12.66, default_y=-231.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.66, default_y=-206.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=77.71, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=77.71, default_y=-196.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=112.98, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=112.98, default_y=-196.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=178.03, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=178.03, default_y=-186.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=213.3, default_y=-211.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=213.3, default_y=-186.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=292.65, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=292.65, default_y=-191.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=401.01, default_y=-211.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-326.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=292.65, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=335.96, default_y=-331.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-336.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Forward():
                Duration(30.0)
            with Note(default_x=292.65, default_y=-346.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=335.96, default_y=-356.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=401.01, default_y=-351.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='42', width=406.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(73.67)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=83.44, default_y=-219.67, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=139.09, default_y=-224.67, dynamics=100.0):
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
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=83.44, default_y=-354.67, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=139.09, default_y=-344.67, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
        with Measure(number='43', width=507.03):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=79.97, default_y=-214.67, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=105.75, default_y=-219.67, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=146.99, default_y=-219.67, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=197.27, default_y=-209.67, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=223.94, default_y=-214.67, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=265.17, default_y=-209.67, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=315.46, default_y=-179.67, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=341.23, default_y=-184.67, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=382.47, default_y=-184.67, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=432.76, default_y=-214.67, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=458.53, default_y=-219.67, dynamics=111.11):
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
            with Forward():
                Duration(12.0)
            with Note(default_x=105.75, default_y=-209.67, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=146.99, default_y=-229.67, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=223.94, default_y=-224.67, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=265.17, default_y=-219.67, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=341.23, default_y=-209.67, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=382.47, default_y=-229.67, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=432.76, default_y=-234.67, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=458.53, default_y=-229.67, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=105.75, default_y=-334.67, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=146.99, default_y=-344.67, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=265.17, default_y=-334.67, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=341.23, default_y=-344.67, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=394.34, default_y=-349.67, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=432.76, default_y=-354.67, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=470.4, default_y=-349.67, dynamics=100.0):
                with Pitch():
                    Step('C')
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
                Duration(48.0)
            with Note(default_x=341.23, default_y=-334.67, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=382.47, default_y=-344.67, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=458.53, default_y=-344.67, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='44', width=284.14):
            with Note(default_x=13.8, default_y=-214.67, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-224.67, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=13.8, default_y=-354.67, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Note():
                Rest()
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Staff(2)
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-344.67, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Forward():
                Duration(54.0)
        with Measure(number='45', width=304.13):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='46', width=554.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(80.65)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='47', width=234.41):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='48', width=354.12):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=14.34, default_y=-231.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=14.34, default_y=-216.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=14.34, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=58.83, default_y=-236.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=58.83, default_y=-221.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=58.83, default_y=-211.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=91.19, default_y=-236.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=91.19, default_y=-221.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=91.19, default_y=-211.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=135.68, default_y=-241.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=135.68, default_y=-231.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=135.68, default_y=-216.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=168.04, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=207.49, default_y=-191.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=227.71, default_y=-196.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=260.07, default_y=-196.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=299.52, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=319.75, default_y=-221.0, dynamics=111.11):
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
            with Forward():
                Duration(36.0)
            with Note(default_x=168.04, default_y=-231.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=227.71, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=260.07, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=319.75, default_y=-236.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=11.02, default_y=-311.65, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(72.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=168.04, default_y=-301.65, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=227.71, default_y=-296.65, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=260.07, default_y=-301.65, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=319.75, default_y=-306.65, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='49', width=358.27):
            with Note(default_x=10.72, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=46.19, default_y=-191.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=64.37, default_y=-196.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=93.46, default_y=-196.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=128.93, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=147.11, default_y=-221.0, dynamics=111.11):
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
            with Note(default_x=185.63, default_y=-241.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=185.63, default_y=-231.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=185.63, default_y=-216.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=10.72, default_y=-231.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=64.37, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=93.46, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=147.11, default_y=-236.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-311.65, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=185.63, default_y=-311.65, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Backup():
                Duration(72.0)
            with Note(default_x=10.72, default_y=-301.65, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=64.37, default_y=-296.65, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=93.46, default_y=-301.65, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=147.11, default_y=-306.65, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(36.0)
        with Measure(number='50', width=526.18):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=86.76, default_y=-226.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=86.76, default_y=-216.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=86.76, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=143.92, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=143.92, default_y=-211.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=143.92, default_y=-196.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=185.48, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=185.48, default_y=-211.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=185.48, default_y=-196.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=242.64, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=242.64, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=242.64, default_y=-191.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=284.2, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=284.2, default_y=-191.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=483.02, default_y=-211.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=483.02, default_y=-201.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=284.2, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=334.89, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=360.87, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=402.43, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=453.12, default_y=-226.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=483.02, default_y=-231.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=83.44, default_y=-346.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(72.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=360.87, default_y=-336.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=360.87, default_y=-316.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=402.43, default_y=-331.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=402.43, default_y=-321.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Staff(2)
        with Measure(number='51', width=528.9):
            with Note(default_x=14.16, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=14.16, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=96.54, default_y=-196.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=139.58, default_y=-191.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=239.42, default_y=-186.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=239.42, default_y=-176.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=282.46, default_y=-191.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=282.46, default_y=-181.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=14.16, default_y=-226.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=66.64, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=96.54, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=139.58, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(27.0)
            with Note(default_x=13.8, default_y=-346.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=282.46, default_y=-346.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Backup():
                Duration(72.0)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=96.54, default_y=-316.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=139.58, default_y=-321.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(3.0)
                Voice('6')
                Type('16th')
                Staff(2)
            with Note(default_x=209.52, default_y=-331.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=239.42, default_y=-336.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=282.46, default_y=-331.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Forward():
                Duration(18.0)
        with Measure(number='52', width=446.5):
            with Note(default_x=17.12, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=17.12, default_y=-201.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=17.12, default_y=-191.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=73.47, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=73.47, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=73.47, default_y=-196.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=114.45, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=114.45, default_y=-206.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=114.45, default_y=-196.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=170.8, default_y=-226.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=170.8, default_y=-216.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=170.8, default_y=-201.0, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=211.78, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=261.75, default_y=-176.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=287.36, default_y=-181.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=328.34, default_y=-181.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=378.31, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=403.92, default_y=-206.0, dynamics=111.11):
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
            with Forward():
                Duration(36.0)
            with Note(default_x=211.78, default_y=-216.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=287.36, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=328.34, default_y=-201.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=403.92, default_y=-221.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-341.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(72.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=211.78, default_y=-331.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=287.36, default_y=-326.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=328.34, default_y=-331.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=403.92, default_y=-336.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='53', width=471.7):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=83.8, default_y=-214.65, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=123.95, default_y=-189.65, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=144.53, default_y=-194.65, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=177.46, default_y=-194.65, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=217.6, default_y=-214.65, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=244.27, default_y=-219.65, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=282.79, default_y=-214.65, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=83.8, default_y=-229.65, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=144.53, default_y=-219.65, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=177.46, default_y=-214.65, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=244.27, default_y=-234.65, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=282.79, default_y=-229.65, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(54.0)
            with Note(default_x=83.44, default_y=-354.65, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=282.79, default_y=-354.65, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(18.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Backup():
                Duration(72.0)
            with Note(default_x=83.8, default_y=-344.65, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=144.53, default_y=-339.65, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=177.46, default_y=-344.65, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=244.27, default_y=-349.65, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(36.0)
        with Measure(number='54', width=334.38):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='55', width=324.34):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='56', width=371.18):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('5')
                Staff(2)
        with Measure(number='57', width=345.19):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(68.86)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note(default_x=219.72, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=252.63, default_y=-201.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=277.9, default_y=-201.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=310.81, default_y=-196.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(48.0)
            with Note(default_x=252.63, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=277.9, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=310.81, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=219.36, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Tie(type='start')
                Voice('3')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Note(default_x=219.72, default_y=-299.86, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=252.63, default_y=-294.86, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=277.9, default_y=-294.86, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=310.81, default_y=-289.86, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='58', width=390.6):
            with Note(default_x=16.64, default_y=-196.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=81.21, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=112.6, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=170.51, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=209.03, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=298.32, default_y=-206.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=356.22, default_y=-201.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=32.81, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=209.03, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=266.93, default_y=-221.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=298.32, default_y=-221.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=356.22, default_y=-226.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=10.0, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(72.0)
                Tie(type='stop')
                Voice('3')
                Type('whole')
                Dot()
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(72.0)
            with Note(default_x=13.32, default_y=-289.86, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=81.21, default_y=-284.86, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=112.6, default_y=-284.86, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=170.51, default_y=-279.86, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=209.03, default_y=-279.86, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=298.32, default_y=-279.86, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=356.22, default_y=-299.86, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='59', width=360.87):
            with Note(default_x=17.12, default_y=-201.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=67.06, default_y=-196.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=95.94, default_y=-196.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=149.21, default_y=-191.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=178.09, default_y=-191.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=231.35, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=260.23, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=295.45, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=313.5, default_y=-211.0, dynamics=100.0):
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
            with Note(default_x=10.48, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(72.0)
                Tie(type='start')
                Voice('3')
                Type('whole')
                Dot()
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-299.86, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=67.06, default_y=-289.86, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=95.94, default_y=-289.86, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=149.21, default_y=-284.86, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=178.09, default_y=-284.86, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=231.35, default_y=-274.86, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=260.23, default_y=-274.86, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=313.5, default_y=-294.86, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=313.5, default_y=-284.86, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-274.86, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=67.06, default_y=-279.86, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=95.94, default_y=-279.86, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(42.0)
        with Measure(number='60', width=404.93):
            with Note(default_x=16.56, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=75.14, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=107.09, default_y=-231.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=171.52, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=209.43, default_y=-191.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=277.13, default_y=-211.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=277.13, default_y=-201.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=324.31, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=371.38, default_y=-216.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=371.38, default_y=-191.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=16.2, default_y=-231.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=75.14, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=107.09, default_y=-206.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=146.05, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Forward():
                Duration(6.0)
            with Note(default_x=209.43, default_y=-211.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.84, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('3')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=221.29, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=312.44, default_y=-216.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('3')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(66.0)
            with Note(default_x=16.2, default_y=-279.86, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=75.14, default_y=-289.86, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=107.09, default_y=-299.86, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=171.52, default_y=-279.86, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=209.43, default_y=-274.86, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=277.13, default_y=-274.86):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=312.44, default_y=-284.86):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=312.44, default_y=-274.86, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=371.38, default_y=-294.86):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=371.38, default_y=-284.86):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='61', width=660.04):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(79.51)
                with StaffLayout(number=2):
                    StaffDistance(75.65)
            with Note(default_x=81.21, default_y=-200.51, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=143.08, default_y=-205.51, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=174.78, default_y=-210.51, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=225.52, default_y=-210.51, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=287.38, default_y=-195.51, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=319.09, default_y=-200.51, dynamics=100.0):
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
            with Note(default_x=369.82, default_y=-195.51, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=431.69, default_y=-190.51, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=463.4, default_y=-185.51, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=514.13, default_y=-210.51, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=607.7, default_y=-200.51, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=81.21, default_y=-225.51, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=143.08, default_y=-230.51, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=174.78, default_y=-225.51, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=225.52, default_y=-220.51, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=319.09, default_y=-215.51, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=369.82, default_y=-210.51, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=431.69, default_y=-291.16, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=463.4, default_y=-286.16, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=514.13, default_y=-286.16, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=575.99, default_y=-291.16, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=607.7, default_y=-210.51, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=81.21, default_y=-301.16, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=225.52, default_y=-301.16, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=319.09, default_y=-316.16, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=369.82, default_y=-311.16, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=431.69, default_y=-306.16, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=463.4, default_y=-321.16, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=463.4, default_y=-301.16, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=514.13, default_y=-301.16, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=607.7, default_y=-281.16, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(72.0)
            with Note(default_x=81.21, default_y=-291.16, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=174.78, default_y=-316.16, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=225.52, default_y=-321.16, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=319.09, default_y=-306.16, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=369.82, default_y=-286.16, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(6.0)
            with Note(default_x=514.13, default_y=-316.16, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=607.7, default_y=-316.16, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='62', width=549.49):
            with Note(default_x=12.66, default_y=-220.51, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=12.66, default_y=-210.51, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=12.66, default_y=-195.51, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=344.88, default_y=-235.51, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=344.88, default_y=-225.51, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=344.88, default_y=-215.51, dynamics=111.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=344.88, default_y=-205.51, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=373.27, default_y=-230.51, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=373.27, default_y=-220.51, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=373.27, default_y=-210.51, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=418.69, default_y=-220.51, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=418.69, default_y=-210.51, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=474.08, default_y=-255.51, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=474.08, default_y=-230.51, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=502.47, default_y=-250.51, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=502.47, default_y=-235.51, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.66, default_y=-321.16, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Note():
                Rest()
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Note(default_x=418.69, default_y=-321.16, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=502.47, default_y=-316.16, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(72.0)
            with Forward():
                Duration(54.0)
            with Note(default_x=418.69, default_y=-301.16, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('7')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='63', width=292.06):
            with Note(default_x=13.8, default_y=-255.51, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-245.51):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-230.51, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=13.8, default_y=-321.16, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')