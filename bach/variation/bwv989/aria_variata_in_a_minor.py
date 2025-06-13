with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Aria Variata')
    with Identification():
        Creator('J.S. Bach', type='composer')
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
            Millimeters(6.256)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1786.45)
            PageWidth(1380.43)
            with PageMargins(type='even'):
                LeftMargin(63.9386)
                RightMargin(63.9386)
                TopMargin(63.9386)
                BottomMargin(127.877)
            with PageMargins(type='odd'):
                LeftMargin(63.9386)
                RightMargin(63.9386)
                TopMargin(63.9386)
                BottomMargin(127.877)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Aria Variata BWV989', default_x=690.217, default_y=1722.51, justify='center', valign='top', font_family='Segoe WP Black', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('alla maniera italiana', default_x=690.217, default_y=1658.57, justify='center', valign='top', font_family='Segoe WP Black', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach', default_x=1316.5, default_y=1622.51, justify='right', valign='bottom', font_family='Segoe WP Black', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Ossia')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Harpsichord')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=598.95):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(171.6)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time(symbol='common', color='#606060'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Andante ', default_x=-41.11, relative_x=-32.94, relative_y=33.75, font_weight='bold', font_family='Franklin Gothic Demi')
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-41.11, relative_x=-32.94, relative_y=33.75):
                        BeatUnit('quarter')
                        PerMinute('76')
                Sound(tempo=76.0)
            with Note(default_x=85.88, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(color='#606060', type='start', placement='below', number=1)
            with Note(default_x=111.7, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=137.52, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=174.8, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=223.56, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    Slur(color='#606060', type='start', placement='below', number=1)
            with Note(default_x=242.67, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=261.78, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=280.89, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=318.18, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=366.93, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(color='#606060', type='start', placement='below', number=1)
            with Note(default_x=392.75, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=418.57, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=474.03, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(color='#606060', type='start', placement='below', number=1)
            with Note(default_x=511.31, default_y=-28.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='2', width=482.01):
            with Note(default_x=12.0, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#606060')
            with Note(default_x=75.05, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(color='#606060', type='start', placement='below', number=1)
            with Note(default_x=111.09, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=147.12, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=169.64, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=192.16, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=214.68, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=237.2, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=273.23, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=309.26, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=345.29, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=381.32, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#606060')
        with Measure(number='3', width=510.36):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=75.61, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(color='#606060', type='start', placement='above', number=1)
            with Note(default_x=93.05, default_y=-3.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=110.48, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=138.38, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=155.81, default_y=3.5):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=173.25, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=190.68, default_y=3.5):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=208.12, default_y=7.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
            with Note(default_x=274.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=291.81, default_y=-3.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=313.49, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(color='#606060', type='start', placement='above', number=1)
            with Note(default_x=330.92, default_y=-3.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=348.36, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=376.25, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=414.61, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(color='#606060', type='start', placement='above', number=1)
            with Note(default_x=442.51, default_y=-3.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=470.4, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
        with Measure(number='4', width=403.4):
            with Attributes():
                with Clef(color='#606060', after_barline='yes'):
                    Sign('G')
                    Line(2)
            with Note(default_x=38.94, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(color='#606060', type='start', placement='below', number=1)
            with Note(default_x=61.26, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=83.59, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=126.82, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=164.1, default_y=-28.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=218.33, default_y=-28.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(color='#606060', type='start', placement='below', number=1)
            with Note(default_x=240.0, default_y=-31.5):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=256.95, default_y=-28.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=338.29, default_y=-28.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#606060')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='5', width=317.95):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=25.02, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
            with Note(default_x=56.26, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
            with Note(default_x=87.51, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
            with Note(default_x=118.75, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=150.0, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(color='#606060', type='start', placement='below', number=1)
            with Note(default_x=167.84, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=185.68, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=208.41, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=231.13, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=253.86, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#606060')
        with Measure(number='6', width=436.33):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=60.13, default_y=-3.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
            with Note(default_x=102.06, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
            with Note(default_x=142.3, default_y=-3.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
            with Note(default_x=182.54, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=222.77, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(color='#606060', type='start', placement='above', number=1)
            with Note(default_x=244.62, default_y=-3.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=266.47, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=295.73, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=325.0, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=354.26, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#606060')
        with Measure(number='7', width=417.6):
            with Attributes():
                with Clef(color='#606060', after_barline='yes'):
                    Sign('G')
                    Line(2)
            with Note(default_x=30.51, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(color='#606060', type='start', placement='above', number=1)
            with Note(default_x=49.79, default_y=-3.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=69.06, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=99.9, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=142.3, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
            with Note(default_x=184.71, default_y=-3.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=227.11, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=257.95, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=331.19, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
            with Note(default_x=373.59, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
        with Measure(number='8', width=377.78):
            with Note(default_x=16.2, default_y=-28.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Notehead('normal', color='#606060')
            with Note(default_x=150.31, default_y=-31.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#606060')
            with Note(default_x=206.78, default_y=-31.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(color='#606060', type='start', placement='below', number=1)
            with Note(default_x=224.42, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=242.07, default_y=-31.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=326.77, default_y=-31.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#606060')
                with Notations():
                    Tied(type='stop')
        with Measure(number='9', width=439.85):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    TopSystemDistance(110.0)
            with Note(default_x=59.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(color='#606060', type='start', placement='above', number=1)
            with Note(default_x=76.73, default_y=-3.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=93.7, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.84, default_y=3.5):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=158.15, default_y=3.5):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=185.29, default_y=7.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=212.43, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=269.46, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(color='#606060', type='start', placement='above', number=1)
            with Note(default_x=286.42, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=303.38, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=330.52, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=367.84, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=394.98, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
        with Measure(number='10', width=329.56):
            with Attributes():
                with Clef(color='#606060', after_barline='yes'):
                    Sign('G')
                    Line(2)
            with Note(default_x=30.51, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(color='#606060', type='start', placement='above', number=1)
            with Note(default_x=46.66, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=62.81, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=88.64, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=124.5, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=150.34, default_y=-3.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=176.17, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=211.7, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
            with Note(default_x=247.22, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=282.75, default_y=-28.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#606060')
        with Measure(number='11', width=462.3):
            with Note(default_x=12.72, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=31.43, default_y=-3.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=50.14, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=68.85, default_y=-3.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=87.56, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=122.89, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(color='#606060', type='start', placement='above', number=1)
            with Note(default_x=141.59, default_y=-3.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=160.3, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=187.32, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=255.45, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    Slur(color='#606060', type='start', placement='below', number=1)
            with Note(default_x=277.13, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=292.79, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=308.46, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=335.47, default_y=-28.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
            with Note(default_x=371.33, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(color='#606060', type='start', placement='below', number=1)
            with Note(default_x=398.35, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
        with Measure(number='12', width=1231.71):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=62.51, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=283.51, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=341.67, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=399.83, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(color='#606060', type='start', placement='below', number=1)
            with Note(default_x=457.99, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=516.15, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=644.1, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#606060')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=736.9, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Notehead('normal', color='#606060')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P2'):
        with Measure(number='1', width=598.95):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(104.73)
                with StaffLayout(number=2):
                    StaffDistance(91.07)
            with Attributes():
                Divisions(24.0)
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
            with Note(default_x=85.88, default_y=-157.73):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Note(default_x=174.8, default_y=-162.73):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=205.11, default_y=-162.73):
                Grace()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=223.56, default_y=-157.73):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Note(default_x=318.18, default_y=-152.73):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=366.93, default_y=-162.73):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=455.58, default_y=-167.73):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=474.03, default_y=-172.73):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=85.88, default_y=-172.73):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=223.56, default_y=-172.73):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=366.93, default_y=-172.73):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=474.03, default_y=-187.73):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=85.88, default_y=-263.8):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=223.56, default_y=-298.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=366.93, default_y=-278.8):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=548.6, default_y=-283.8):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=85.88, default_y=-253.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=174.8, default_y=-258.8):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=223.56, default_y=-253.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=318.18, default_y=-248.8):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=366.93, default_y=-258.8):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Note(default_x=474.03, default_y=-268.8):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
        with Measure(number='2', width=482.01):
            with Note(default_x=12.0, default_y=-157.73):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=56.61, default_y=-157.73):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=75.05, default_y=-152.73):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=218.75, default_y=-142.73):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=237.2, default_y=-147.73):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        Schleifer()
            with Note(default_x=309.26, default_y=-152.73):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=345.29, default_y=-157.73):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=381.32, default_y=-157.73):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49, relative_x=-11.09, relative_y=-19.49)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-172.73):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=75.05, default_y=-177.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=237.2, default_y=-182.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=381.32, default_y=-172.73):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-288.8):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=75.05, default_y=-303.8):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=237.2, default_y=-298.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=381.32, default_y=-263.8):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=430.86, default_y=-258.8):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-263.8):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Note(default_x=75.05, default_y=-278.8):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Note(default_x=237.2, default_y=-263.8):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Note(default_x=381.32, default_y=-253.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Forward():
                Duration(48.0)
            with Note(default_x=242.2, default_y=-293.8):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('8')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Forward():
                Duration(24.0)
        with Measure(number='3', width=510.36):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(117.07)
                with StaffLayout(number=2):
                    StaffDistance(111.26)
            with Note(default_x=75.61, default_y=-145.07):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Note(default_x=208.12, default_y=-135.07):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Ornaments():
                        Schleifer()
            with Note(default_x=276.57, default_y=-145.07):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=287.54, default_y=-150.07):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=313.49, default_y=-155.07):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=376.25, default_y=-165.07):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=396.17, default_y=-155.07):
                Grace()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=414.61, default_y=-150.07):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=470.4, default_y=-175.07):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=75.25, default_y=-170.07):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=313.49, default_y=-180.07):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=414.61, default_y=-185.07):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=87.48, default_y=-286.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=246.48, default_y=-291.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=274.37, default_y=-296.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=330.01, default_y=-291.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=376.25, default_y=-296.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=414.61, default_y=-301.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=470.4, default_y=-291.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=75.61, default_y=-281.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Note(default_x=208.12, default_y=-276.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Note(default_x=313.13, default_y=-291.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(48.0)
                Voice('7')
                Type('half')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
        with Measure(number='4', width=403.4):
            with Note(default_x=38.94, default_y=-180.07):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=164.1, default_y=-185.07):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=217.97, default_y=-185.07):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Backup():
                Duration(96.0)
            with Note(default_x=59.84, default_y=-185.07):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=126.82, default_y=-190.07):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=234.85, default_y=-185.07):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=338.29, default_y=-200.07):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=53.94, default_y=-286.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=126.82, default_y=-326.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=218.33, default_y=-311.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=338.29, default_y=-346.33):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=38.94, default_y=-291.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Note(default_x=126.82, default_y=-306.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=164.1, default_y=-301.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=191.21, default_y=-296.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('7')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=218.33, default_y=-296.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=284.06, default_y=-301.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=311.18, default_y=-306.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=338.29, default_y=-301.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='5', width=317.95):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=25.02, default_y=-160.07):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=56.26, default_y=-165.07):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=87.51, default_y=-160.07):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=118.75, default_y=-155.07):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=150.0, default_y=-165.07):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=208.41, default_y=-170.07):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=231.13, default_y=-175.07):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=253.86, default_y=-175.07):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=25.02, default_y=-185.07):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=56.26, default_y=-190.07):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=87.51, default_y=-185.07):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=118.75, default_y=-180.07):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=149.64, default_y=-190.07):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=25.02, default_y=-321.33):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=87.51, default_y=-356.33):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=166.17, default_y=-301.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=285.1, default_y=-306.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-181.62)
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=24.66, default_y=-301.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('7')
                Type('half')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=150.0, default_y=-301.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=208.41, default_y=-296.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=253.86, default_y=-291.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
        with Measure(number='6', width=436.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(108.89)
                with StaffLayout(number=2):
                    StaffDistance(120.6)
            with Note(default_x=60.13, default_y=-141.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=102.06, default_y=-146.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=142.3, default_y=-141.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=182.54, default_y=-136.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=222.77, default_y=-146.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=295.73, default_y=-151.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=325.0, default_y=-156.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=354.26, default_y=-156.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=60.13, default_y=-166.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=102.06, default_y=-171.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=142.3, default_y=-166.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=182.54, default_y=-161.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=222.41, default_y=-171.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=60.13, default_y=-312.49):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=142.3, default_y=-347.49):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=238.94, default_y=-292.49):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=394.5, default_y=-297.49):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-207.56)
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=59.77, default_y=-292.49):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(48.0)
                Voice('7')
                Type('half')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Note(default_x=222.77, default_y=-292.49):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=295.73, default_y=-287.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=354.26, default_y=-282.49):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
        with Measure(number='7', width=417.6):
            with Note(default_x=30.51, default_y=-146.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=99.9, default_y=-151.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=142.3, default_y=-146.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=184.71, default_y=-141.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=208.67, default_y=-146.89):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=227.11, default_y=-151.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=331.19, default_y=-146.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=373.59, default_y=-171.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=30.15, default_y=-176.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=227.11, default_y=-176.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=331.19, default_y=-181.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Forward():
                Duration(24.0)
            with Note(default_x=152.3, default_y=-196.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('4')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=237.11, default_y=-186.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('4')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=30.51, default_y=-302.49):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=142.3, default_y=-312.49):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=243.64, default_y=-297.49):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=288.79, default_y=-302.49):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=331.19, default_y=-307.49):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=373.59, default_y=-317.49):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=30.15, default_y=-292.49):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(48.0)
                Voice('7')
                Type('half')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Note(default_x=226.75, default_y=-297.49):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('7')
                Type('half')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
        with Measure(number='8', width=377.78):
            with Note(default_x=16.2, default_y=-176.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=150.31, default_y=-181.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=206.41, default_y=-181.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Backup():
                Duration(96.0)
            with Note(default_x=37.1, default_y=-181.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=111.49, default_y=-186.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=223.3, default_y=-181.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=326.77, default_y=-196.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=16.2, default_y=-337.49):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=55.02, default_y=-327.49):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=111.49, default_y=-332.49):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=206.78, default_y=-317.49):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=326.77, default_y=-352.49):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=16.2, default_y=-292.49):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=55.02, default_y=-297.49):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=83.25, default_y=-302.49):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=111.49, default_y=-297.49):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=150.31, default_y=-312.49):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=178.54, default_y=-302.49):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('7')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=206.78, default_y=-302.49):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=270.3, default_y=-307.49):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=298.53, default_y=-312.49):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('7')
                Type('16th')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=326.77, default_y=-307.49):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
        with Measure(number='9', width=439.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(128.6)
                with StaffLayout(number=2):
                    StaffDistance(90.54)
            with Note(default_x=59.77, default_y=-156.6):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Note(default_x=120.84, default_y=-151.6):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=139.71, default_y=-151.6):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=158.15, default_y=-146.6):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=212.43, default_y=-166.6):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=269.46, default_y=-171.6):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=330.52, default_y=-176.6):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=349.4, default_y=-176.6):
                Grace()
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=367.84, default_y=-181.6):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=59.77, default_y=-201.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=158.15, default_y=-196.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=269.46, default_y=-181.6):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=367.84, default_y=-196.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=64.77, default_y=-206.6):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(1)
            with Note(default_x=217.43, default_y=-216.6):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=59.77, default_y=-307.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=158.15, default_y=-312.14):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=212.43, default_y=-317.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=269.1, default_y=-322.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=59.77, default_y=-287.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(36.0)
                Voice('7')
                Type('quarter')
                Dot()
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Note(default_x=212.43, default_y=-272.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Note(default_x=269.46, default_y=-267.14):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=330.52, default_y=-272.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=367.84, default_y=-277.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
        with Measure(number='10', width=329.56):
            with Note(default_x=30.51, default_y=-171.6):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Note(default_x=88.64, default_y=-166.6):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=106.06, default_y=-166.6):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=124.5, default_y=-161.6):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=176.17, default_y=-181.6):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=211.7, default_y=-186.6):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=247.22, default_y=-191.6):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=282.75, default_y=-196.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=30.51, default_y=-196.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=176.17, default_y=-201.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=211.7, default_y=-196.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=282.75, default_y=-211.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=35.51, default_y=-206.6):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('3')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=45.51, default_y=-287.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=124.5, default_y=-292.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=176.17, default_y=-297.14):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=211.34, default_y=-302.14):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=30.51, default_y=-287.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Note(default_x=124.5, default_y=-282.14):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=176.17, default_y=-272.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=211.7, default_y=-282.14):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=247.22, default_y=-287.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=282.75, default_y=-292.14):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
        with Measure(number='11', width=462.3):
            with Note(default_x=12.72, default_y=-156.6):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Ornaments():
                        Schleifer()
            with Note(default_x=122.89, default_y=-166.6):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=187.32, default_y=-176.6):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=214.21, default_y=-206.6):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=255.45, default_y=-186.6):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=335.47, default_y=-196.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=352.89, default_y=-186.6):
                Grace()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=371.33, default_y=-181.6):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-201.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=255.45, default_y=-196.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(color='#FF0000'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=425.37, default_y=-206.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-307.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(72.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=371.33, default_y=-307.14):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-282.14):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(72.0)
                Voice('7')
                Type('half')
                Dot()
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Note(default_x=371.33, default_y=-297.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('7')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
        with Measure(number='12', width=1231.71):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(68.07)
                with StaffLayout(number=2):
                    StaffDistance(80.46)
            with Note(default_x=62.51, default_y=-121.07):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=283.51, default_y=-116.07):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=341.67, default_y=-111.07):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=399.83, default_y=-126.07):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=644.1, default_y=-121.07):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=731.07, default_y=-146.07):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=62.51, default_y=-151.07):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=190.46, default_y=-146.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=399.83, default_y=-141.07):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=749.38, default_y=-141.07):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=865.1, default_y=-146.07):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=958.15, default_y=-151.07):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=1039.49, default_y=-151.07):
                Grace()
                with Pitch():
                    Step('B')
                    Octave(3)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Note(default_x=1051.21, default_y=-146.07):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF0000')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Forward():
                Duration(48.0)
            with Note(default_x=736.79, default_y=-136.07):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('half')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=62.51, default_y=-231.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=399.83, default_y=-266.53):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Note(default_x=736.79, default_y=-251.53):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=62.15, default_y=-211.53):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(48.0)
                Voice('7')
                Type('half')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Note(default_x=736.79, default_y=-216.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('7')
                Type('half')
                Stem('up')
                Notehead('normal', color='#AA00FF')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')