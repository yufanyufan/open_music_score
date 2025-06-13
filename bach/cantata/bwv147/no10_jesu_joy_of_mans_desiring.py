with ScorePartwise(version='3.1'):
    with Identification():
        with Encoding():
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
            PageHeight(1683.27)
            PageWidth(1190.82)
            with PageMargins(type='even'):
                LeftMargin(51.0205)
                RightMargin(51.0205)
                TopMargin(73.6961)
                BottomMargin(90.7031)
            with PageMargins(type='odd'):
                LeftMargin(51.0205)
                RightMargin(51.0205)
                TopMargin(73.6961)
                BottomMargin(90.7031)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords("Jesu, Joy of Man's Desiring, BWV 147 (No. 10)", default_x=595.408, default_y=1609.57, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johan Sebastian Bach', default_x=1139.79, default_y=1509.57, justify='right', valign='bottom', font_size='12')
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
                Volume(83.4646)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Voice')
            PartAbbreviation('Vo.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Voice')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Acoustic Bass')
            PartAbbreviation('Bass')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Acoustic Bass')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(33)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=297.93):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(163.79)
                        RightMargin(-0.0)
                    TopSystemDistance(161.71)
                with StaffLayout(number=2):
                    StaffDistance(84.42)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(1)
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
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-40.16, default_y=18.51, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Staff(1)
                Sound(tempo=65.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=5.06, relative_x=-23.32, relative_y=19.51):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=125.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=146.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=167.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=189.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=210.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=231.08, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=252.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=273.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=104.83, default_y=-164.42):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=167.95, default_y=-129.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C/E', relative_y=40.0)
                Staff(2)
            with Note(default_x=231.08, default_y=-139.42):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='2', width=208.9):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=36.84, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=57.88, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=78.92, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=99.97, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=121.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=142.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=163.09, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=184.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-154.42):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=40.0)
                Staff(2)
            with Note(default_x=78.92, default_y=-139.42):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=142.05, default_y=-174.42):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='3', width=208.9):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=36.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=57.88, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=78.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=99.97, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=121.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=142.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=163.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=184.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-159.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=78.92, default_y=-154.42):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=40.0)
                Staff(2)
            with Note(default_x=142.05, default_y=-149.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='4', width=209.26):
            with Note(default_x=16.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=37.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=58.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=79.29, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=100.33, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=121.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=142.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=163.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=184.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=40.0)
                Staff(2)
            with Note(default_x=16.16, default_y=-144.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=79.29, default_y=-134.42):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=142.41, default_y=-144.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=259.58):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(98.41)
            with Note(default_x=83.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=102.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=121.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=140.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=159.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=178.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=196.97, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=215.89, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=234.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=83.41, default_y=-143.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=40.0)
                Staff(2)
            with Note(default_x=140.19, default_y=-153.41):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=40.0)
                Staff(2)
            with Note(default_x=196.97, default_y=-163.41):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='6', width=191.97):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=34.73, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=53.65, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=72.58, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=91.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=110.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=129.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=148.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=167.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-168.41):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=40.0)
                Staff(2)
            with Note(default_x=72.58, default_y=-153.41):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=129.35, default_y=-158.41):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='7', width=191.97):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=34.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=53.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=72.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=91.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=110.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=129.35, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=148.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=167.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/C', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-163.41):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A/C#', relative_y=40.0)
                Staff(2)
            with Note(default_x=72.58, default_y=-163.41):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D7', relative_y=40.0)
                Staff(2)
            with Note(default_x=129.35, default_y=-158.41):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='8', width=203.38):
            with Note(default_x=16.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=35.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=54.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=73.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=92.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=111.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=130.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=149.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=169.01, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=16.16, default_y=-178.41):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=73.48, default_y=-178.41):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=111.69, default_y=-143.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=130.8, default_y=-158.41):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=169.01, default_y=-168.41):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='9', width=84.24):
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=59.47, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=16.16, default_y=-143.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=37.82, default_y=-148.41):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C/E', relative_x=-7.77, relative_y=38.45)
                Staff(2)
            with Note(default_x=59.47, default_y=-153.41):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=84.24):
            with Note(default_x=15.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=59.47, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D/F#', relative_y=40.0)
                Staff(2)
            with Note(default_x=16.16, default_y=-148.41):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=37.82, default_y=-153.41):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=59.47, default_y=-158.41):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=235.68):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(85.97)
            with Note(default_x=83.41, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=183.98, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C/E', relative_y=40.0)
                Staff(2)
            with Note(default_x=83.77, default_y=-140.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D/F#', relative_y=40.0)
                Staff(2)
            with Note(default_x=133.88, default_y=-135.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=183.98, default_y=-130.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=262.69):
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=43.05, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=70.31, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=97.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=124.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=152.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=179.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=206.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=233.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=97.56, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=152.07, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=179.33, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=233.84, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='13', width=258.32):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=42.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=69.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=96.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=122.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=149.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=176.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=203.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=229.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D7', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-180.97):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=96.11, default_y=-180.97):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=149.65, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=176.41, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=229.95, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='14', width=258.68):
            with Note(default_x=16.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=42.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=69.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=96.47, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=123.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=150.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=176.78, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=203.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=230.31, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=16.16, default_y=-130.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=96.47, default_y=-135.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C/E', relative_y=40.0)
                Staff(2)
            with Note(default_x=176.78, default_y=-140.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=290.04):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(-0.0)
                    SystemDistance(111.1)
                with StaffLayout(number=2):
                    StaffDistance(82.87)
            with Note(default_x=83.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=106.46, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=129.15, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=151.84, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=174.52, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=197.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=219.9, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=242.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=265.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=83.77, default_y=-117.87):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=151.84, default_y=-152.87):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=40.0)
                Staff(2)
            with Note(default_x=219.9, default_y=-137.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=280.84):
            with Note(default_x=16.16, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=46.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=78.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=116.22, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=141.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=178.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=203.47, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=228.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=253.99, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/E', relative_y=40.0)
                Staff(2)
            with Note(default_x=16.16, default_y=-122.87):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=59.79, default_y=-117.87):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.82, default_y=-112.87):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=116.22, default_y=-117.87):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=203.47, default_y=-122.87):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_x=43.54, relative_y=38.45)
                Offset(-18.0)
                Staff(1)
        with Measure(number='17', width=222.43):
            with Note(default_x=16.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=38.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=61.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=84.22, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=106.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=129.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=152.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=174.97, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=197.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-127.87):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=40.0)
                Staff(2)
            with Note(default_x=152.29, default_y=-147.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='18', width=222.07):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=38.49, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=61.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=83.86, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=106.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=129.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=151.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=174.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=197.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-152.87):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=40.0)
                Staff(2)
            with Note(default_x=83.86, default_y=-137.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/E', relative_y=40.0)
                Staff(2)
            with Note(default_x=151.93, default_y=-172.87):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='19', width=257.78):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(-0.0)
                    SystemDistance(111.1)
                with StaffLayout(number=2):
                    StaffDistance(87.53)
            with Note(default_x=83.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=102.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=120.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=139.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=158.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=176.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=195.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=214.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=233.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am', relative_y=40.0)
                Staff(2)
            with Note(default_x=83.41, default_y=-162.53):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=139.51, default_y=-157.53):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/C', relative_y=40.0)
                Staff(2)
            with Note(default_x=195.61, default_y=-152.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='20', width=186.73):
            with Note(default_x=12.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=31.06, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=49.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=68.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=87.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=105.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=124.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=143.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=161.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=40.0)
                Staff(2)
            with Note(default_x=12.36, default_y=-147.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=68.46, default_y=-137.53):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D7', relative_y=40.0)
                Staff(2)
            with Note(default_x=124.56, default_y=-147.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='21', width=190.53):
            with Note(default_x=16.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=34.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=53.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=72.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=90.96, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=109.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=128.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=147.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=165.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=16.16, default_y=-132.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=72.26, default_y=-142.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=40.0)
                Staff(2)
            with Note(default_x=128.36, default_y=-152.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='22', width=190.17):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=34.5, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=53.2, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=71.9, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=90.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=109.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=128.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=146.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=165.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-157.53):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=40.0)
                Staff(2)
            with Note(default_x=71.9, default_y=-142.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=128.0, default_y=-147.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='23', width=190.17):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=34.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=53.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=71.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=90.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=109.3, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=128.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=146.7, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=165.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/C', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-152.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A/C#', relative_y=40.0)
                Staff(2)
            with Note(default_x=71.9, default_y=-152.53):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D7', relative_y=40.0)
                Staff(2)
            with Note(default_x=128.0, default_y=-147.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='24', width=215.52):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(85.97)
            with Note(default_x=83.41, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=170.54, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=83.77, default_y=-130.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=127.16, default_y=-135.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C/E', relative_y=40.0)
                Staff(2)
            with Note(default_x=170.54, default_y=-140.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='25', width=144.11):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=99.13, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D/F#', relative_y=40.0)
                Staff(2)
            with Note(default_x=12.36, default_y=-135.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=55.74, default_y=-140.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=99.13, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=147.91):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=102.93, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C/E', relative_y=40.0)
                Staff(2)
            with Note(default_x=16.16, default_y=-140.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D/F#', relative_y=40.0)
                Staff(2)
            with Note(default_x=59.54, default_y=-135.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_x=12.44, relative_y=38.89)
                Staff(2)
            with Note(default_x=102.93, default_y=-130.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='27', width=252.2):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=38.83, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=65.3, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=91.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=118.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=144.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=171.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=197.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=224.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=40.0)
                Staff(2)
            with Note(default_x=12.36, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=91.77, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=144.72, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=171.19, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=224.13, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='28', width=255.64):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=42.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=68.74, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=95.21, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=121.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=148.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=174.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=201.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=227.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D7', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-180.97):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=95.21, default_y=-180.97):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=148.16, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=174.63, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=227.57, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='29', width=292.55):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(-0.0)
                    SystemDistance(123.92)
                with StaffLayout(number=2):
                    StaffDistance(87.53)
            with Note(default_x=79.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=103.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=126.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=150.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=173.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=197.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=220.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=244.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=267.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=79.97, default_y=-132.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=150.3, default_y=-137.53):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C/E', relative_y=40.0)
                Staff(2)
            with Note(default_x=220.63, default_y=-142.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='30', width=228.74):
            with Note(default_x=16.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=39.6, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=63.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=86.49, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=109.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=133.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=156.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=180.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=203.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Bm', relative_y=40.0)
                Staff(2)
            with Note(default_x=16.16, default_y=-122.53):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=86.49, default_y=-157.53):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=40.0)
                Staff(2)
            with Note(default_x=156.81, default_y=-142.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='31', width=268.78):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=46.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=77.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=115.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=141.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=166.25, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=191.48, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=216.71, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=241.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/C', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-127.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=59.39, default_y=-122.53):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.4, default_y=-117.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=115.78, default_y=-122.53):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=40.0)
                Staff(2)
            with Note(default_x=191.48, default_y=-127.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='32', width=225.3):
            with Note(default_x=12.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=36.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=59.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=83.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=106.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=129.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=153.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=176.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=200.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=12.36, default_y=-132.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=40.0)
                Staff(2)
            with Note(default_x=153.38, default_y=-152.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='33', width=258.47):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(-0.0)
                    SystemDistance(123.92)
                with StaffLayout(number=2):
                    StaffDistance(87.53)
            with Note(default_x=83.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=102.2, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=120.99, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=139.77, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=158.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=177.34, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=196.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=214.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=233.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=83.41, default_y=-157.53):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=40.0)
                Staff(2)
            with Note(default_x=139.77, default_y=-142.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/E', relative_y=40.0)
                Staff(2)
            with Note(default_x=196.13, default_y=-177.53):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='34', width=190.86):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=34.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=53.37, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=72.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=90.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=109.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=128.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=147.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=166.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-162.53):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=72.16, default_y=-157.53):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/C', relative_y=40.0)
                Staff(2)
            with Note(default_x=128.52, default_y=-152.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='35', width=187.42):
            with Note(default_x=12.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=31.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=49.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=68.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=87.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=106.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=125.08, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=143.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=162.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=40.0)
                Staff(2)
            with Note(default_x=12.36, default_y=-147.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=68.72, default_y=-137.53):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=125.08, default_y=-147.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='36', width=187.78):
            with Note(default_x=12.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=31.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=50.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=69.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=87.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=106.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=125.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=144.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.01, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=12.72, default_y=-132.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=69.08, default_y=-142.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C/E', relative_y=40.0)
                Staff(2)
            with Note(default_x=125.44, default_y=-152.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='37', width=190.86):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=34.59, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=53.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=72.16, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=90.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=109.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=128.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=147.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=166.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-157.53):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=40.0)
                Staff(2)
            with Note(default_x=72.16, default_y=-142.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=128.52, default_y=-147.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='38', width=288.9):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(90.64)
            with Note(default_x=83.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=106.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=128.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=151.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=173.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=196.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=218.96, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=241.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=264.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/C', relative_y=40.0)
                Staff(2)
            with Note(default_x=83.41, default_y=-155.64):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A/C#', relative_y=40.0)
                Staff(2)
            with Note(default_x=151.18, default_y=-155.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=40.0)
                Staff(2)
            with Note(default_x=218.96, default_y=-150.64):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='39', width=234.58):
            with Note(default_x=12.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=36.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=60.31, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=84.11, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=107.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=131.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=155.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=179.29, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=209.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=12.72, default_y=-170.64):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=84.11, default_y=-170.64):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=131.7, default_y=-135.64):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=155.49, default_y=-140.64):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=209.18, default_y=-145.64):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='40', width=234.22):
            with Note(default_x=12.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=36.16, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=59.95, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=83.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=107.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=137.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=161.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=185.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=208.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=40.0)
                Staff(2)
            with Note(default_x=12.36, default_y=-150.64):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=83.75, default_y=-155.64):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=161.23, default_y=-160.64):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='41', width=257.68):
            with Note(default_x=16.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=41.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=66.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=91.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=122.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=148.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=174.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=204.26, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=230.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am', relative_y=40.0)
                Staff(2)
            with Note(default_x=16.16, default_y=-165.64):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=91.93, default_y=-130.64):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=132.96, default_y=-135.64):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=40.0)
                Staff(2)
            with Note(default_x=174.0, default_y=-140.64):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=215.04, default_y=-145.64):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='42', width=332.9):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(-0.0)
                    SystemDistance(122.36)
                with StaffLayout(number=2):
                    StaffDistance(87.53)
            with Note(default_x=91.65, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=115.63, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=139.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=163.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=182.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=222.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=259.37, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=283.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=307.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Bo/D', relative_y=40.0)
                Staff(2)
            with Note(default_x=91.65, default_y=-122.53):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=163.58, default_y=-122.53):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=205.0, default_y=-117.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=238.1, default_y=-112.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=40.0)
                Staff(2)
            with Note(default_x=259.37, default_y=-122.53):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='43', width=223.54):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=38.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=60.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=82.79, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=105.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=127.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=149.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=176.45, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=198.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-162.53):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=40.0)
                Staff(2)
            with Note(default_x=82.79, default_y=-162.53):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Dm', relative_y=40.0)
                Staff(2)
            with Note(default_x=149.78, default_y=-172.53):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
        with Measure(number='44', width=233.48):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=38.86, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=70.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=93.42, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=116.48, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=139.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=162.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=185.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=208.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/C', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-152.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=40.0)
                Staff(2)
            with Note(default_x=93.42, default_y=-137.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/E', relative_y=40.0)
                Staff(2)
            with Note(default_x=162.6, default_y=-142.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='45', width=225.46):
            with Note(default_x=14.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=36.4, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=58.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=81.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=103.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=126.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=148.4, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=170.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=200.69, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Dm', relative_y=40.0)
                Staff(2)
            with Note(default_x=14.0, default_y=-147.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D#o', relative_y=40.0)
                Staff(2)
            with Note(default_x=81.2, default_y=-147.53):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=40.0)
                Staff(2)
            with Note(default_x=148.4, default_y=-142.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='46', width=225.58):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(-0.0)
                    SystemDistance(122.36)
                with StaffLayout(number=2):
                    StaffDistance(85.97)
            with Note(default_x=83.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=102.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=120.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=138.74, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
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
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am', relative_y=40.0)
                Staff(2)
            with Note(default_x=83.77, default_y=-125.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=138.74, default_y=-160.97):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=188.24, default_y=-120.97):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='47', width=252.6):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=40.92, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=66.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=91.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=116.29, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=142.96, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=168.08, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=200.75, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=225.87, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-115.97):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am', relative_y=40.0)
                Staff(2)
            with Note(default_x=91.17, default_y=-125.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/E', relative_y=40.0)
                Staff(2)
            with Note(default_x=168.08, default_y=-140.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='48', width=297.35):
            with Note(default_x=14.0, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=42.12, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=75.23, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=108.35, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=141.46, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=169.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=211.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=239.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=267.64, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Dm/F', default_y=12.23, relative_y=40.0)
                Staff(2)
            with Note(default_x=14.0, default_y=-110.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Dm', default_y=8.83, relative_y=40.0)
                Staff(2)
            with Note(default_x=113.35, default_y=-110.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=156.91, default_y=-105.97):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.47, default_y=-100.97):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=211.41, default_y=-110.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='49', width=239.85):
            with Note(default_x=16.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=39.95, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=66.62, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=90.41, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=114.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=138.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=161.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=185.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=214.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=40.0)
                Staff(2)
            with Note(default_x=16.16, default_y=-140.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=90.41, default_y=-140.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=161.79, default_y=-150.97):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='50', width=541.55):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(84.42)
            with Note(default_x=88.41, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=138.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=188.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=238.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=289.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=339.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=389.44, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=439.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=489.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=40.0)
                Staff(2)
            with Note(default_x=88.41, default_y=-134.42):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Dm', relative_y=40.0)
                Staff(2)
            with Note(default_x=238.93, default_y=-144.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=389.44, default_y=-129.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='51', width=473.83):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=66.51, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=117.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=167.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=218.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=269.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=320.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=370.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=421.51, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-149.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=167.94, default_y=-149.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D7', default_y=1.7, relative_y=40.0)
                Staff(2)
            with Note(default_x=269.37, default_y=-149.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=320.08, default_y=-154.42):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=40.0)
                Staff(2)
            with Note(default_x=421.51, default_y=-144.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='52', width=252.5):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(0.0)
                    SystemDistance(111.88)
                with StaffLayout(number=2):
                    StaffDistance(85.97)
            with Note(default_x=79.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=98.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=116.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=135.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=153.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=172.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=190.79, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=209.26, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=227.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=79.97, default_y=-130.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=135.38, default_y=-135.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C/E', relative_y=40.0)
                Staff(2)
            with Note(default_x=190.79, default_y=-140.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='53', width=188.69):
            with Note(default_x=16.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=34.63, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=53.1, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=71.57, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=90.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=108.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=126.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=145.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=16.16, default_y=-120.97):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=71.57, default_y=-155.97):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=40.0)
                Staff(2)
            with Note(default_x=126.98, default_y=-120.97):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='54', width=188.33):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=34.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=52.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=71.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=89.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=108.15, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=126.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=145.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-115.97):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=71.21, default_y=-130.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=126.62, default_y=-140.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='55', width=197.54):
            with Note(default_x=12.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=31.47, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=50.57, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=69.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=88.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=107.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=127.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=153.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=172.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=40.0)
                Staff(2)
            with Note(default_x=12.36, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=69.68, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=127.0, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='56', width=188.33):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=34.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=52.74, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=71.21, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=89.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=108.15, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=126.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=145.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D7', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-180.97):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=71.21, default_y=-180.97):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=108.15, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=126.62, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=163.56, default_y=-145.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='57', width=292.55):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(-0.0)
                    SystemDistance(111.88)
                with StaffLayout(number=2):
                    StaffDistance(92.19)
            with Note(default_x=79.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=103.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=126.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=150.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=173.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=197.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=220.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=244.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=267.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=79.97, default_y=-137.19):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=150.3, default_y=-142.19):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C/E', relative_y=40.0)
                Staff(2)
            with Note(default_x=220.63, default_y=-147.19):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='58', width=228.74):
            with Note(default_x=16.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=39.6, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=63.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=86.49, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=109.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=133.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=156.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=180.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=203.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=16.16, default_y=-127.19):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=86.49, default_y=-162.19):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=40.0)
                Staff(2)
            with Note(default_x=156.81, default_y=-147.19):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='59', width=268.78):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=46.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=77.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=115.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=141.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=166.25, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=191.48, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=216.71, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=241.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/C', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-132.19):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=59.39, default_y=-127.19):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.4, default_y=-122.19):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=40.0)
                Staff(2)
            with Note(default_x=115.78, default_y=-127.19):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=191.48, default_y=-132.19):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='60', width=225.3):
            with Note(default_x=12.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=36.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=59.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=83.05, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=106.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=129.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=153.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=176.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=200.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=12.36, default_y=-137.19):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='61', width=261.71):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(80.94)
            with Note(default_x=88.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=107.3, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=125.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=144.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=162.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=181.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=199.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=218.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=236.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G7', relative_y=40.0)
                Staff(2)
            with Note(default_x=88.41, default_y=-195.94):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(36.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=88.41, default_y=-160.94):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(36.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am7/G', relative_y=40.0)
                Offset(-12.0)
                Staff(1)
        with Measure(number='62', width=190.17):
            with Note(default_x=17.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=35.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=54.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=72.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=91.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=109.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=128.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=146.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=165.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=17.23, default_y=-195.94):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=17.23, default_y=-160.94):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=72.44, default_y=-195.94):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=72.44, default_y=-160.94):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='63', width=189.1):
            with Note(default_x=16.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=34.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=53.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=71.73, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=90.25, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=108.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=127.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=145.81, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=164.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D7/G', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-195.94):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(36.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-160.94):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(36.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='64', width=185.66):
            with Note(default_x=12.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=31.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=49.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=68.29, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=86.81, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=105.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=123.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=142.37, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=160.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=12.72, default_y=-160.94):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=68.29, default_y=-125.94):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=123.85, default_y=-135.94):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='65', width=188.74):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=34.32, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=52.84, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=71.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=89.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=108.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=126.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=145.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-150.94):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=40.0)
                Staff(2)
            with Note(default_x=71.36, default_y=-135.94):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/C', relative_y=40.0)
                Staff(2)
            with Note(default_x=126.93, default_y=-170.94):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='66', width=543.21):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(-0.0)
                    SystemDistance(139.59)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=134.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=185.24, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=236.15, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=287.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=337.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=388.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=439.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=490.7, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am', relative_y=40.0)
                Staff(2)
            with Note(default_x=83.41, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=236.15, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/C', relative_y=40.0)
                Staff(2)
            with Note(default_x=388.88, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='67', width=472.16):
            with Note(default_x=12.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=63.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=114.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=165.1, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=216.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=266.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=317.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=368.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=419.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=40.0)
                Staff(2)
            with Note(default_x=12.36, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=165.1, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=317.83, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='68', width=333.35):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.4)
                        RightMargin(-0.0)
                    SystemDistance(139.59)
                with StaffLayout(number=2):
                    StaffDistance(83.15)
            with Note(default_x=79.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=107.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=135.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=163.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=191.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=219.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=247.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=275.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=303.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Note(default_x=79.97, default_y=-128.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=163.9, default_y=-138.15):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C/E', relative_y=40.0)
                Staff(2)
            with Note(default_x=247.82, default_y=-148.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='69', width=269.18):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=43.78, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=71.75, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=99.73, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=127.7, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=155.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=183.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=211.63, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=239.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G/B', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-153.15):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Em', relative_y=40.0)
                Staff(2)
            with Note(default_x=99.73, default_y=-138.15):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=183.65, default_y=-143.15):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='70', width=269.18):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=27.75, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Direction():
                with DirectionType():
                    Words('rit.', default_y=-40.0, relative_y=-35.0)
                Staff(1)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=43.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=71.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=20.25, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('50')
                Staff(1)
                Sound(tempo=50.0)
            with Note(default_x=99.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=127.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=155.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=7.75, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('31')
                Staff(1)
                Sound(tempo=31.0)
            with Note(default_x=183.65, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=211.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=239.6, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/C', relative_y=40.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-148.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Am/C#', relative_y=40.0)
                Staff(2)
            with Note(default_x=99.73, default_y=-148.15):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D7', relative_y=40.0)
                Staff(2)
            with Note(default_x=183.65, default_y=-143.15):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='71', width=143.68):
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=40.0)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-11.75, relative_y=7.14):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=15.8, default_y=-163.15):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-143.15):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=297.93):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=3.11, relative_y=10.15):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=104.47, default_y=-294.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=104.47, default_y=-284.42):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=104.47, default_y=-274.42):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=231.08, default_y=-279.42):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=231.08, default_y=-269.42):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=231.08, default_y=-259.42):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='2', width=208.9):
            with Note(default_x=15.8, default_y=-294.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-284.42):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-274.42):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.56, default_y=-304.42):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=78.56, default_y=-294.42):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=78.56, default_y=-284.42):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='3', width=208.9):
            with Note(default_x=15.8, default_y=-289.42):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-279.42):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-269.42):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.92, default_y=-294.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.92, default_y=-284.42):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.92, default_y=-274.42):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.05, default_y=-294.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.05, default_y=-279.42):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.05, default_y=-269.42):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=209.26):
            with Note(default_x=15.8, default_y=-309.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-299.42):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-289.42):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='5', width=259.58):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-308.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.41, default_y=-298.41):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.41, default_y=-288.41):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=140.19, default_y=-318.41):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=140.19, default_y=-308.41):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=140.19, default_y=-298.41):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=196.97, default_y=-308.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=196.97, default_y=-293.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=196.97, default_y=-283.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=191.97):
            with Note(default_x=15.8, default_y=-308.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-298.41):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-288.41):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.22, default_y=-318.41):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=72.22, default_y=-308.41):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=72.22, default_y=-298.41):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=191.97):
            with Note(default_x=15.8, default_y=-293.41):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-283.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-268.41):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.58, default_y=-293.41):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=72.58, default_y=-283.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.58, default_y=-268.41):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.35, default_y=-293.41):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=141.22, default_y=-288.41):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.35, default_y=-278.41):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.35, default_y=-268.41):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=203.38):
            with Note(default_x=15.8, default_y=-308.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-298.41):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-288.41):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='9', width=84.24):
            with Note(default_x=15.8, default_y=-308.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-298.41):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-288.41):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=59.47, default_y=-318.41):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.47, default_y=-308.41):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.47, default_y=-293.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='10', width=84.24):
            with Note(default_x=15.8, default_y=-313.41):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-303.41):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-288.41):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='11', width=235.68):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.3)
            with Note(default_x=83.77, default_y=-336.28):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.77, default_y=-326.28):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.77, default_y=-311.28):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=133.88, default_y=-331.28):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=133.88, default_y=-321.28):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=133.88, default_y=-306.28):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.98, default_y=-326.28):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.98, default_y=-316.28):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.98, default_y=-306.28):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='12', width=262.69):
            with Note(default_x=15.44, default_y=-306.28):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.44, default_y=-296.28):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.44, default_y=-286.28):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='13', width=258.32):
            with Note(default_x=15.44, default_y=-306.28):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.44, default_y=-296.28):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.44, default_y=-286.28):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.44, default_y=-276.28):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='14', width=258.68):
            with Note(default_x=15.8, default_y=-326.28):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-316.28):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-306.28):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=176.78, default_y=-311.28):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=176.78, default_y=-301.28):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=176.78, default_y=-291.28):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='15', width=290.04):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-292.87):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=83.41, default_y=-282.87):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=83.41, default_y=-272.87):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=219.9, default_y=-302.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=219.9, default_y=-292.87):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=219.9, default_y=-282.87):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=280.84):
            with Note(default_x=15.8, default_y=-277.87):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-267.87):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-252.87):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=203.47, default_y=-272.87):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=203.47, default_y=-262.87):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=203.47, default_y=-252.87):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='17', width=222.43):
            with Note(default_x=15.8, default_y=-292.87):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-282.87):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-272.87):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=152.29, default_y=-277.87):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=152.29, default_y=-267.87):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=152.29, default_y=-257.87):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='18', width=222.07):
            with Note(default_x=15.8, default_y=-292.87):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-282.87):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-272.87):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.86, default_y=-302.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.86, default_y=-292.87):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.86, default_y=-282.87):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=151.93, default_y=-287.87):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=151.93, default_y=-277.87):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=151.93, default_y=-267.87):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='19', width=257.78):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-292.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.41, default_y=-282.53):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.41, default_y=-272.53):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.51, default_y=-297.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.51, default_y=-287.53):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.51, default_y=-277.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=195.61, default_y=-282.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=195.61, default_y=-272.53):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=195.61, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=186.73):
            with Note(default_x=12.0, default_y=-277.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=12.0, default_y=-267.53):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=12.0, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=124.56, default_y=-282.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=136.43, default_y=-277.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=124.56, default_y=-267.53):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=124.56, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='21', width=190.53):
            with Note(default_x=15.8, default_y=-297.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-287.53):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-277.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=128.36, default_y=-282.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=128.36, default_y=-272.53):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=128.36, default_y=-262.53):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='22', width=190.17):
            with Note(default_x=15.8, default_y=-287.53):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-277.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-262.53):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.54, default_y=-272.53):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=71.54, default_y=-262.53):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=71.54, default_y=-252.53):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='23', width=190.17):
            with Note(default_x=15.8, default_y=-282.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-272.53):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.9, default_y=-282.53):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=71.9, default_y=-272.53):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.9, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=128.0, default_y=-282.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=139.87, default_y=-277.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=128.0, default_y=-267.53):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=128.0, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=215.52):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-260.97):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=83.41, default_y=-250.97):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=83.41, default_y=-240.97):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=170.54, default_y=-270.97):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=170.54, default_y=-260.97):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=170.54, default_y=-245.97):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='25', width=144.11):
            with Note(default_x=12.0, default_y=-265.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=12.0, default_y=-255.97):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=12.0, default_y=-240.97):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='26', width=147.91):
            with Note(default_x=16.16, default_y=-270.97):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=16.16, default_y=-260.97):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=16.16, default_y=-245.97):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.54, default_y=-265.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.54, default_y=-255.97):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.54, default_y=-240.97):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=102.93, default_y=-260.97):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=102.93, default_y=-250.97):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=102.93, default_y=-240.97):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='27', width=252.2):
            with Note(default_x=12.0, default_y=-275.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=12.0, default_y=-265.97):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=12.0, default_y=-255.97):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='28', width=255.64):
            with Note(default_x=15.44, default_y=-275.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.44, default_y=-265.97):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.44, default_y=-255.97):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.44, default_y=-245.97):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='29', width=292.55):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.61, default_y=-262.53):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=79.61, default_y=-252.53):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=79.61, default_y=-242.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=220.63, default_y=-272.53):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=220.63, default_y=-262.53):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=220.63, default_y=-247.53):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='30', width=228.74):
            with Note(default_x=15.8, default_y=-287.53):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-277.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-267.53):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=156.81, default_y=-272.53):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=156.81, default_y=-262.53):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=156.81, default_y=-252.53):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='31', width=268.78):
            with Note(default_x=15.8, default_y=-282.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-272.53):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=115.78, default_y=-262.53):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=115.78, default_y=-252.53):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=115.78, default_y=-242.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=191.48, default_y=-277.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=191.48, default_y=-267.53):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=191.48, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='32', width=225.3):
            with Note(default_x=12.36, default_y=-262.53):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=12.36, default_y=-252.53):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=12.36, default_y=-242.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=153.38, default_y=-272.53):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=153.38, default_y=-262.53):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=153.38, default_y=-247.53):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='33', width=258.47):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-287.53):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.41, default_y=-277.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.41, default_y=-262.53):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.77, default_y=-272.53):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.77, default_y=-262.53):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.77, default_y=-252.53):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=196.13, default_y=-282.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=196.13, default_y=-272.53):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=196.13, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='34', width=190.86):
            with Note(default_x=15.8, default_y=-292.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-282.53):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-272.53):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.16, default_y=-297.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.16, default_y=-287.53):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.16, default_y=-277.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=128.52, default_y=-282.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=128.52, default_y=-272.53):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=128.52, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='35', width=187.42):
            with Note(default_x=12.0, default_y=-277.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=12.0, default_y=-267.53):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=12.0, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='36', width=187.78):
            with Note(default_x=12.36, default_y=-262.53):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=12.36, default_y=-252.53):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=12.36, default_y=-242.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=125.44, default_y=-272.53):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=125.44, default_y=-262.53):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=125.44, default_y=-247.53):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='37', width=190.86):
            with Note(default_x=15.8, default_y=-287.53):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-277.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-262.53):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.8, default_y=-272.53):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=71.8, default_y=-262.53):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=71.8, default_y=-252.53):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='38', width=288.9):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-285.64):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.41, default_y=-275.64):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.41, default_y=-260.64):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=151.18, default_y=-285.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=151.18, default_y=-275.64):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=151.18, default_y=-260.64):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=218.96, default_y=-280.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=218.96, default_y=-270.64):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=218.96, default_y=-260.64):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='39', width=234.58):
            with Note(default_x=12.36, default_y=-265.64):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=12.36, default_y=-255.64):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=12.36, default_y=-245.64):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='40', width=234.22):
            with Note(default_x=12.0, default_y=-280.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=12.0, default_y=-270.64):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=12.0, default_y=-260.64):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=161.23, default_y=-290.64):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=161.23, default_y=-280.64):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=161.23, default_y=-265.64):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='41', width=257.68):
            with Note(default_x=15.8, default_y=-295.64):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-285.64):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-275.64):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=174.0, default_y=-270.64):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=174.0, default_y=-260.64):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=174.0, default_y=-250.64):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='42', width=332.9):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=91.65, default_y=-277.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=91.65, default_y=-267.53):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=91.65, default_y=-252.53):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=163.58, default_y=-287.53):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=163.58, default_y=-272.53):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=163.58, default_y=-262.53):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=259.37, default_y=-272.53):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=259.37, default_y=-262.53):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=259.37, default_y=-252.53):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='43', width=223.54):
            with Note(default_x=15.8, default_y=-292.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-282.53):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-272.53):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=82.79, default_y=-267.53):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=82.79, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=82.79, default_y=-247.53):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=149.78, default_y=-277.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=149.78, default_y=-267.53):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=149.78, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='44', width=233.48):
            with Note(default_x=15.8, default_y=-282.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-272.53):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=93.42, default_y=-267.53):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=93.42, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=93.42, default_y=-247.53):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=162.6, default_y=-272.53):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=162.6, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=162.6, default_y=-247.53):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='45', width=225.46):
            with Note(default_x=14.0, default_y=-277.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=14.0, default_y=-267.53):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=14.0, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.2, default_y=-277.53):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=81.2, default_y=-267.53):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=81.2, default_y=-257.53):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=148.4, default_y=-272.53):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=148.4, default_y=-262.53):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=148.4, default_y=-252.53):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='46', width=225.58):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-290.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=83.41, default_y=-280.97):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=83.41, default_y=-270.97):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=188.24, default_y=-285.97):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=188.24, default_y=-275.97):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=188.24, default_y=-260.97):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='47', width=252.6):
            with Note(default_x=15.8, default_y=-280.97):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-270.97):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-260.97):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=91.17, default_y=-290.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=91.17, default_y=-280.97):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=91.17, default_y=-270.97):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=168.08, default_y=-270.97):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=168.08, default_y=-255.97):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=168.08, default_y=-245.97):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='48', width=297.35):
            with Note(default_x=14.0, default_y=-265.97):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=14.0, default_y=-255.97):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=14.0, default_y=-240.97):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=98.35, default_y=-275.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=98.35, default_y=-265.97):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=98.35, default_y=-255.97):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=211.41, default_y=-260.97):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=211.41, default_y=-250.97):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=211.41, default_y=-240.97):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='49', width=239.85):
            with Note(default_x=15.8, default_y=-280.97):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-270.97):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-260.97):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='50', width=541.55):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.41, default_y=-264.42):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=88.41, default_y=-254.42):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.41, default_y=-244.42):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=238.93, default_y=-274.42):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=238.93, default_y=-264.42):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=238.93, default_y=-254.42):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=389.44, default_y=-259.42):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=389.44, default_y=-249.42):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=389.44, default_y=-239.42):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='51', width=473.83):
            with Note(default_x=15.8, default_y=-279.42):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=15.8, default_y=-269.42):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=15.8, default_y=-259.42):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=167.94, default_y=-279.42):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=167.94, default_y=-269.42):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=167.94, default_y=-259.42):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=269.37, default_y=-274.42):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=269.37, default_y=-264.42):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
            with Note(default_x=269.37, default_y=-254.42):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
            with Note(default_x=269.37, default_y=-244.42):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
            with Note(default_x=320.08, default_y=-259.42):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=320.08, default_y=-249.42):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
            with Note(default_x=320.08, default_y=-239.42):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
            with Note(default_x=421.51, default_y=-274.42):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=421.51, default_y=-264.42):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
            with Note(default_x=421.51, default_y=-254.42):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
        with Measure(number='52', width=252.5):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.61, default_y=-260.97):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=79.61, default_y=-250.97):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=79.61, default_y=-240.97):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=190.79, default_y=-270.97):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=190.79, default_y=-260.97):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=190.79, default_y=-245.97):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='53', width=188.69):
            with Note(default_x=15.8, default_y=-285.97):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-275.97):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-260.97):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=126.98, default_y=-270.97):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=126.98, default_y=-260.97):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=126.98, default_y=-250.97):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='54', width=188.33):
            with Note(default_x=15.8, default_y=-290.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-280.97):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-270.97):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=70.85, default_y=-285.97):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=70.85, default_y=-275.97):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=70.85, default_y=-260.97):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='55', width=197.54):
            with Note(default_x=12.0, default_y=-275.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=12.0, default_y=-265.97):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=12.0, default_y=-255.97):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='56', width=188.33):
            with Note(default_x=15.44, default_y=-275.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.44, default_y=-265.97):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.44, default_y=-255.97):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.44, default_y=-245.97):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='57', width=292.55):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(87.53)
            with Note(default_x=79.61, default_y=-289.72):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=79.61, default_y=-279.72):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=79.61, default_y=-269.72):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=220.63, default_y=-299.72):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=220.63, default_y=-289.72):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=220.63, default_y=-274.72):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='58', width=228.74):
            with Note(default_x=15.8, default_y=-314.72):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-304.72):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-289.72):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=156.81, default_y=-299.72):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=156.81, default_y=-289.72):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=156.81, default_y=-279.72):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='59', width=268.78):
            with Note(default_x=15.8, default_y=-309.72):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-299.72):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-284.72):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=115.42, default_y=-304.72):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=115.42, default_y=-294.72):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=115.42, default_y=-284.72):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='60', width=225.3):
            with Note(default_x=12.36, default_y=-289.72):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=12.36, default_y=-279.72):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=12.36, default_y=-269.72):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='61', width=261.71):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.41, default_y=-255.94):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=88.41, default_y=-245.94):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=88.41, default_y=-235.94):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=88.41, default_y=-225.94):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
            with Note(default_x=188.04, default_y=-255.94):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=199.9, default_y=-250.94):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=199.9, default_y=-240.94):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=199.9, default_y=-230.94):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='62', width=190.17):
            with Note(default_x=16.87, default_y=-255.94):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=16.87, default_y=-245.94):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=16.87, default_y=-235.94):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='63', width=189.1):
            with Note(default_x=15.8, default_y=-290.94):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-270.94):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-260.94):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-250.94):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-240.94):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='64', width=185.66):
            with Note(default_x=12.36, default_y=-255.94):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=12.36, default_y=-245.94):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=12.36, default_y=-235.94):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='65', width=188.74):
            with Note(default_x=15.8, default_y=-280.94):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-270.94):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-255.94):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.36, default_y=-265.94):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.36, default_y=-255.94):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.36, default_y=-245.94):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=126.93, default_y=-275.94):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=126.93, default_y=-265.94):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=126.93, default_y=-250.94):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='66', width=543.21):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-270.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.41, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.41, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=236.15, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=236.15, default_y=-255.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=236.15, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=388.88, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=388.88, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=388.88, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='67', width=472.16):
            with Note(default_x=12.0, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=12.0, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=12.0, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='68', width=333.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.61, default_y=-258.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=79.61, default_y=-248.15):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=79.61, default_y=-238.15):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=247.82, default_y=-268.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=247.82, default_y=-258.15):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=247.82, default_y=-243.15):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='69', width=269.18):
            with Note(default_x=15.8, default_y=-283.15):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-273.15):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-258.15):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=99.36, default_y=-268.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=99.36, default_y=-258.15):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=99.36, default_y=-248.15):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='70', width=269.18):
            with Note(default_x=15.8, default_y=-278.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-268.15):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-253.15):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=99.73, default_y=-278.15):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=99.73, default_y=-268.15):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=99.73, default_y=-253.15):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.65, default_y=-273.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.65, default_y=-263.15):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.65, default_y=-253.15):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.65, default_y=-243.15):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='71', width=143.68):
            with Note(default_x=15.8, default_y=-258.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=15.8, default_y=-248.15):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=15.8, default_y=-238.15):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=297.93):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
                with Transpose():
                    Diatonic(0)
                    Chromatic(0.0)
                    OctaveChange(-1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=104.83, default_y=-374.42):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=167.95, default_y=-339.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=231.08, default_y=-349.42):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=208.9):
            with Note(default_x=15.8, default_y=-364.42):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.92, default_y=-349.42):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=142.05, default_y=-384.42):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='3', width=208.9):
            with Note(default_x=15.8, default_y=-369.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.92, default_y=-364.42):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.05, default_y=-359.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=209.26):
            with Note(default_x=16.16, default_y=-354.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=79.29, default_y=-344.42):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=142.41, default_y=-354.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=259.58):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-353.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=140.19, default_y=-363.41):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=196.97, default_y=-373.41):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=191.97):
            with Note(default_x=15.8, default_y=-378.41):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.58, default_y=-363.41):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.35, default_y=-368.41):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=191.97):
            with Note(default_x=15.8, default_y=-373.41):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.58, default_y=-373.41):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=129.35, default_y=-368.41):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=203.38):
            with Note(default_x=16.16, default_y=-388.41):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=73.48, default_y=-388.41):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=111.69, default_y=-353.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=130.8, default_y=-368.41):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=169.01, default_y=-378.41):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='9', width=84.24):
            with Note(default_x=16.16, default_y=-353.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.82, default_y=-358.41):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=59.47, default_y=-363.41):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=84.24):
            with Note(default_x=16.16, default_y=-358.41):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.82, default_y=-363.41):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=59.47, default_y=-368.41):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='11', width=235.68):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.77, default_y=-381.28):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=133.88, default_y=-376.28):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.98, default_y=-371.28):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=262.69):
            with Note(default_x=15.8, default_y=-386.28):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=97.56, default_y=-386.28):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=152.07, default_y=-386.28):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=179.33, default_y=-386.28):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=233.84, default_y=-386.28):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='13', width=258.32):
            with Note(default_x=15.8, default_y=-421.28):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=96.11, default_y=-421.28):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=149.65, default_y=-386.28):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=176.41, default_y=-386.28):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=229.95, default_y=-386.28):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='14', width=258.68):
            with Note(default_x=16.16, default_y=-371.28):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=96.47, default_y=-376.28):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=176.78, default_y=-381.28):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=290.04):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.77, default_y=-327.87):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=151.84, default_y=-362.87):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=219.9, default_y=-347.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=280.84):
            with Note(default_x=15.8, default_y=-347.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=203.47, default_y=-352.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='17', width=222.43):
            with Note(default_x=15.8, default_y=-337.87):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=152.29, default_y=-357.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='18', width=222.07):
            with Note(default_x=15.8, default_y=-362.87):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.86, default_y=-347.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=151.93, default_y=-382.87):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='19', width=257.78):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-372.53):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.51, default_y=-367.53):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=195.61, default_y=-362.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=186.73):
            with Note(default_x=12.36, default_y=-357.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=68.46, default_y=-347.53):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=124.56, default_y=-357.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='21', width=190.53):
            with Note(default_x=16.16, default_y=-342.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.26, default_y=-352.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=128.36, default_y=-362.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='22', width=190.17):
            with Note(default_x=15.8, default_y=-367.53):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.9, default_y=-352.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=128.0, default_y=-357.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='23', width=190.17):
            with Note(default_x=15.8, default_y=-362.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.9, default_y=-362.53):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=128.0, default_y=-357.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=215.52):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.77, default_y=-340.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=127.16, default_y=-345.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=170.54, default_y=-350.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='25', width=144.11):
            with Note(default_x=12.36, default_y=-345.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=55.74, default_y=-350.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=99.13, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='26', width=147.91):
            with Note(default_x=16.16, default_y=-350.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=59.54, default_y=-345.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=102.93, default_y=-340.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='27', width=252.2):
            with Note(default_x=12.36, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=91.77, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=144.72, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=171.19, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=224.13, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='28', width=255.64):
            with Note(default_x=15.8, default_y=-390.97):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=95.21, default_y=-390.97):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=148.16, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=174.63, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=227.57, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='29', width=292.55):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.97, default_y=-342.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=150.3, default_y=-347.53):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=220.63, default_y=-352.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='30', width=228.74):
            with Note(default_x=16.16, default_y=-332.53):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.49, default_y=-367.53):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=156.81, default_y=-352.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='31', width=268.78):
            with Note(default_x=15.8, default_y=-352.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=115.42, default_y=-357.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='32', width=225.3):
            with Note(default_x=12.36, default_y=-342.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=153.38, default_y=-362.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='33', width=258.47):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-367.53):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.77, default_y=-352.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=196.13, default_y=-387.53):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='34', width=190.86):
            with Note(default_x=15.8, default_y=-372.53):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.16, default_y=-367.53):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=128.52, default_y=-362.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='35', width=187.42):
            with Note(default_x=12.36, default_y=-357.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=68.72, default_y=-347.53):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=125.08, default_y=-357.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=187.78):
            with Note(default_x=12.72, default_y=-342.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.08, default_y=-352.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=125.44, default_y=-362.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='37', width=190.86):
            with Note(default_x=15.8, default_y=-367.53):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.16, default_y=-352.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=128.52, default_y=-357.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='38', width=288.9):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-365.64):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=151.18, default_y=-365.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=218.96, default_y=-360.64):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='39', width=234.58):
            with Note(default_x=12.72, default_y=-380.64):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=84.11, default_y=-380.64):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=131.7, default_y=-345.64):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=155.49, default_y=-350.64):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=209.18, default_y=-355.64):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='40', width=234.22):
            with Note(default_x=12.36, default_y=-360.64):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.75, default_y=-365.64):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=161.23, default_y=-370.64):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='41', width=257.68):
            with Note(default_x=15.8, default_y=-330.64):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=174.0, default_y=-330.64):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='42', width=332.9):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=91.65, default_y=-357.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=163.58, default_y=-367.53):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=259.37, default_y=-352.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='43', width=223.54):
            with Note(default_x=15.8, default_y=-372.53):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=82.79, default_y=-372.53):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=149.78, default_y=-382.53):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
        with Measure(number='44', width=233.48):
            with Note(default_x=15.8, default_y=-362.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=93.42, default_y=-347.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=162.6, default_y=-352.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='45', width=225.46):
            with Note(default_x=14.0, default_y=-357.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.2, default_y=-357.53):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=148.4, default_y=-352.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='46', width=225.58):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.77, default_y=-335.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=138.74, default_y=-370.97):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=188.24, default_y=-330.97):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='47', width=252.6):
            with Note(default_x=15.8, default_y=-325.97):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=91.17, default_y=-335.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=168.08, default_y=-350.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='48', width=297.35):
            with Note(default_x=14.0, default_y=-345.97):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=98.35, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=211.41, default_y=-340.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='49', width=239.85):
            with Note(default_x=15.8, default_y=-350.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=161.79, default_y=-360.97):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='50', width=541.55):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.41, default_y=-344.42):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=238.93, default_y=-354.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=389.44, default_y=-339.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='51', width=473.83):
            with Note(default_x=15.8, default_y=-359.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=167.94, default_y=-359.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=269.37, default_y=-359.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=320.08, default_y=-364.42):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=421.51, default_y=-354.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='52', width=252.5):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.97, default_y=-340.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.38, default_y=-345.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=190.79, default_y=-350.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='53', width=188.69):
            with Note(default_x=16.16, default_y=-330.97):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.57, default_y=-365.97):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=126.98, default_y=-330.97):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='54', width=188.33):
            with Note(default_x=15.8, default_y=-325.97):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.21, default_y=-340.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=126.62, default_y=-350.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='55', width=197.54):
            with Note(default_x=12.36, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.68, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=127.0, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='56', width=188.33):
            with Note(default_x=15.8, default_y=-390.97):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=71.21, default_y=-390.97):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=108.15, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=126.62, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=163.56, default_y=-355.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='57', width=292.55):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.97, default_y=-369.72):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=150.3, default_y=-374.72):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=220.63, default_y=-379.72):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='58', width=228.74):
            with Note(default_x=16.16, default_y=-359.72):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.49, default_y=-394.72):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=156.81, default_y=-379.72):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='59', width=268.78):
            with Note(default_x=15.8, default_y=-379.72):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=115.42, default_y=-384.72):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='60', width=225.3):
            with Note(default_x=12.36, default_y=-369.72):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='61', width=261.71):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.41, default_y=-370.94):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='62', width=190.17):
            with Note(default_x=17.23, default_y=-370.94):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=72.44, default_y=-370.94):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='63', width=189.1):
            with Note(default_x=15.8, default_y=-370.94):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(36.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='64', width=185.66):
            with Note(default_x=12.72, default_y=-370.94):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=68.29, default_y=-335.94):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=123.85, default_y=-345.94):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='65', width=188.74):
            with Note(default_x=15.8, default_y=-360.94):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.36, default_y=-345.94):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=126.93, default_y=-380.94):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='66', width=543.21):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=236.15, default_y=-345.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=388.88, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='67', width=472.16):
            with Note(default_x=12.36, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=165.1, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=317.83, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='68', width=333.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.6)
            with Note(default_x=79.97, default_y=-338.75):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=163.9, default_y=-348.75):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=247.82, default_y=-358.75):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='69', width=269.18):
            with Note(default_x=15.8, default_y=-363.75):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=99.73, default_y=-348.75):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.65, default_y=-353.75):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='70', width=269.18):
            with Note(default_x=15.8, default_y=-358.75):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=99.73, default_y=-358.75):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=183.65, default_y=-353.75):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='71', width=143.68):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=15.8, default_y=-373.75):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')