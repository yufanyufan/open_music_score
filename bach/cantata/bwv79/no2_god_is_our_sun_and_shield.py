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
        CreditWords("Gott ist unsre Sonn' und Schild", default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('BWV 79/2', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach\n', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
        CreditWords('arr. André Papillon\n')
        CreditWords(None)
    with PartList():
        with ScorePart(id='P1'):
            PartName('Flûte')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Flûte')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(74)
                Volume(74.8031)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Piano')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=375.11):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(85.0)
                        RightMargin(-0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('6')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-34.94, relative_y=20.0):
                        BeatUnit('quarter')
                        BeatUnitDot()
                        PerMinute('50')
                Sound(tempo=75.0)
            with Note(default_x=111.15, default_y=0.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=150.02, default_y=-5.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=227.75, default_y=-10.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=252.05, default_y=0.0, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.34, default_y=-25.0, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=300.63, default_y=-15.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=324.92, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=349.21, default_y=0.0, dynamics=95.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='2', width=270.4):
            with Note(default_x=13.8, default_y=5.0, dynamics=102.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=51.58, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=127.13, default_y=-5.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=150.75, default_y=5.0, dynamics=92.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=174.36, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.97, default_y=-15.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.58, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.19, default_y=5.0, dynamics=95.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='3', width=346.99):
            with Note(default_x=13.62, default_y=10.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.27, default_y=-15.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.92, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=96.56, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=124.21, default_y=-20.0, dynamics=73.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.86, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=179.5, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.15, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.8, default_y=5.0, dynamics=96.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.44, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=290.09, default_y=0.0, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.74, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='4', width=420.63):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(85.62)
            with Note(default_x=95.01, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=122.01, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.02, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.02, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.02, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.02, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=257.02, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=284.02, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=311.03, default_y=0.0, dynamics=96.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=338.03, default_y=-5.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=365.03, default_y=-5.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=392.03, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='5', width=378.53):
            with Note(default_x=10.0, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.58, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.15, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=101.73, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.31, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.89, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=193.46, default_y=-10.0, dynamics=74.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=224.04, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.62, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.2, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=315.77, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=346.35, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='6', width=257.33):
            with Note(default_x=10.0, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=47.81, default_y=-10.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=71.43, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.06, default_y=-20.0, dynamics=74.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=118.69, default_y=-15.0, dynamics=82.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=142.32, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='7', width=410.16):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(85.62)
            with Note(default_x=91.21, default_y=-5.0, dynamics=96.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=117.88, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.3, default_y=0.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.73, default_y=-5.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.15, default_y=10.0, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=223.58, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=250.0, default_y=-15.0, dynamics=74.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=276.43, default_y=-5.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.86, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=329.28, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=355.71, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=382.13, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='8', width=318.11):
            with Note(default_x=13.8, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.03, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.25, default_y=0.0, dynamics=95.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.48, default_y=-5.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.7, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.93, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=165.16, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=190.38, default_y=-5.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.61, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=240.84, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.06, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=291.29, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='9', width=328.22):
            with Note(default_x=13.8, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.87, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.94, default_y=0.0, dynamics=96.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.01, default_y=15.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=118.07, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.14, default_y=-10.0, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=170.21, default_y=-15.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=196.28, default_y=-5.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=222.35, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=248.42, default_y=5.0, dynamics=95.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=274.49, default_y=0.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=300.55, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='10', width=323.2):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(85.62)
            with Note(default_x=91.21, default_y=-25.0, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=117.88, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.67, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.45, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.24, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.03, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=221.82, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='11', width=308.79):
            with Note(default_x=10.0, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=34.3, default_y=-20.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.6, default_y=-25.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=82.9, default_y=-30.0, dynamics=76.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.8, default_y=-15.0, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.1, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=161.39, default_y=-25.0, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=185.69, default_y=-15.0, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.99, default_y=-20.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.29, default_y=-25.0, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.59, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.89, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=164.85):
            with Note(default_x=10.0, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=35.54, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=61.08, default_y=-15.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=86.63, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='13', width=259.65):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='14', width=372.06):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='15', width=307.72):
            with Note(default_x=22.58, default_y=0.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=64.59, default_y=-5.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=148.6, default_y=-10.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.85, default_y=0.0, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.11, default_y=-25.0, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.36, default_y=-15.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.61, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=279.87, default_y=0.0, dynamics=95.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='16', width=376.71):
            with Note(default_x=10.0, default_y=5.0, dynamics=102.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=60.36, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=186.26, default_y=-5.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=217.73, default_y=-15.0, dynamics=76.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.21, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=280.68, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=312.16, default_y=-25.0, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=343.63, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='17', width=419.22):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(115.01)
            with Note(default_x=103.25, default_y=-5.0, dynamics=102.22):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=242.59, default_y=-5.0, dynamics=102.22):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=271.62, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=301.51, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.54, default_y=10.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=359.57, default_y=5.0, dynamics=91.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=388.6, default_y=10.0, dynamics=92.22):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='18', width=316.61):
            with Note(default_x=17.23, default_y=-5.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=160.99, default_y=-5.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=186.66, default_y=-10.0, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.33, default_y=-10.0, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=238.0, default_y=-15.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=263.67, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=289.34, default_y=-20.0, dynamics=75.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='19', width=320.66):
            with Note(default_x=17.23, default_y=-15.0, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=150.42, default_y=-15.0, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=178.17, default_y=0.0, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.07, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.81, default_y=0.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=263.56, default_y=-5.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=291.31, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='20', width=378.58):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(115.01)
            with Note(default_x=103.25, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=224.91, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=250.25, default_y=-20.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.6, default_y=-20.0, dynamics=78.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=300.95, default_y=-25.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=326.29, default_y=-25.0, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=351.64, default_y=-15.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='21', width=350.59):
            with Note(default_x=16.44, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.85, default_y=-25.0, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.27, default_y=-25.0, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=103.16, default_y=-30.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=131.58, default_y=-30.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.99, default_y=-35.0, dynamics=73.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=188.4, default_y=-40.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='22', width=327.32):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=185.19, default_y=-5.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=213.3, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.4, default_y=-15.0, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=269.51, default_y=5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.61, default_y=0.0, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=454.56):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(115.01)
            with Note(default_x=91.57, default_y=0.0, dynamics=95.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.69, default_y=-10.0, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.8, default_y=-15.0, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.92, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.04, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=242.15, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=272.27, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=302.38, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=332.5, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=362.61, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=392.73, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=422.85, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=307.81):
            with Note(default_x=13.8, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.79, default_y=-10.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=86.9, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.02, default_y=-20.0, dynamics=74.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.13, default_y=-15.0, dynamics=82.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=171.25, default_y=-10.0, dynamics=86.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='25', width=294.12):
            with Note(default_x=17.23, default_y=-10.0, dynamics=86.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='26', width=359.81):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=91.21, default_y=-15.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=129.92, default_y=-20.0, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=207.35, default_y=-25.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=231.54, default_y=-15.0, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.73, default_y=-40.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.63, default_y=-30.0, dynamics=81.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=309.83, default_y=-25.0, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=334.02, default_y=-15.0, dynamics=95.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=348.34):
            with Note(default_x=17.23, default_y=-20.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.47, default_y=-10.0, dynamics=96.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.71, default_y=-15.0, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=98.94, default_y=-20.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=126.18, default_y=-5.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.42, default_y=-25.0, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=183.32, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=210.55, default_y=-20.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.79, default_y=-40.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=265.03, default_y=-35.0, dynamics=72.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=292.26, default_y=-30.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.5, default_y=-25.0, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=348.34):
            with Note(default_x=17.23, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.47, default_y=-10.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.71, default_y=-15.0, dynamics=96.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=98.94, default_y=-20.0, dynamics=87.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=126.18, default_y=-5.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.42, default_y=-25.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=183.32, default_y=-30.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=210.55, default_y=-20.0, dynamics=86.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.79, default_y=-40.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=265.03, default_y=-35.0, dynamics=72.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=292.26, default_y=-30.0, dynamics=78.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.5, default_y=-25.0, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=434.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(109.07)
            with Note(default_x=103.25, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=130.48, default_y=-10.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.7, default_y=-15.0, dynamics=96.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.92, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.14, default_y=-5.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.36, default_y=-25.0, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=269.26, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=296.48, default_y=-20.0, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=323.7, default_y=-25.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=350.93, default_y=-10.0, dynamics=95.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=378.15, default_y=-15.0, dynamics=92.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=405.37, default_y=-35.0, dynamics=72.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='30', width=274.13):
            with Note(default_x=10.0, default_y=-40.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.67, default_y=-30.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=60.73, default_y=-35.0, dynamics=72.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=84.8, default_y=-20.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.87, default_y=-25.0, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.94, default_y=-40.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=157.01, default_y=-45.0, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='31', width=348.17):
            with Note(default_x=17.23, default_y=-45.0, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=44.45, default_y=-35.0, dynamics=84.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.68, default_y=-40.0, dynamics=81.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=98.9, default_y=-45.0, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.79, default_y=-30.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.02, default_y=-25.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=183.24, default_y=-40.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=210.46, default_y=-30.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.68, default_y=-35.0, dynamics=84.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.9, default_y=-40.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=292.13, default_y=-10.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.35, default_y=-15.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='32', width=360.83):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(109.07)
            with Note(default_x=95.01, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=134.16, default_y=-25.0, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=173.3, default_y=-30.0, dynamics=81.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=212.44, default_y=-25.0, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=236.91, default_y=-30.0, dynamics=81.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=261.37, default_y=-25.0, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.83, default_y=-20.0, dynamics=92.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=310.3, default_y=-15.0, dynamics=95.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=334.76, default_y=-10.0, dynamics=96.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='33', width=346.49):
            with Note(default_x=26.96, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=72.38, default_y=-40.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='34', width=349.17):
            with Note(default_x=17.23, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=64.36, default_y=-40.0, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='35', width=397.76):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(109.07)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=117.59, default_y=-10.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.92, default_y=-15.0, dynamics=84.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.24, default_y=-20.0, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.57, default_y=-15.0, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.89, default_y=5.0, dynamics=96.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=244.21, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=269.54, default_y=5.0, dynamics=95.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.86, default_y=0.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=320.19, default_y=-5.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=345.51, default_y=0.0, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=370.84, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='36', width=316.55):
            with Note(default_x=10.0, default_y=-20.0, dynamics=76.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=60.83, default_y=-5.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=111.65, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=187.89, default_y=-10.0, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=213.3, default_y=-15.0, dynamics=76.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=238.71, default_y=-20.0, dynamics=74.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.13, default_y=-15.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=289.54, default_y=-5.0, dynamics=92.22):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='37', width=342.18):
            with Note(default_x=19.67, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=46.87, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.07, default_y=0.0, dynamics=95.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=101.27, default_y=-5.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.47, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.67, default_y=15.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=182.87, default_y=-5.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=242.66, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='38', width=454.56):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=309.45, default_y=-10.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=338.16, default_y=-15.0, dynamics=82.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=366.86, default_y=-20.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=395.56, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=424.26, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='39', width=310.72):
            with Note(default_x=13.62, default_y=10.0, dynamics=102.22):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.29, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.73, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.17, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=113.61, default_y=-20.0, dynamics=74.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.05, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=162.48, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.92, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=211.36, default_y=5.0, dynamics=96.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.8, default_y=0.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.24, default_y=0.0, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=284.68, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='40', width=291.21):
            with Note(default_x=13.8, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.77, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.74, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=82.7, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.67, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.64, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=151.61, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.58, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.54, default_y=0.0, dynamics=96.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.51, default_y=-5.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=243.48, default_y=-5.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.45, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=441.41):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(116.65)
            with Note(default_x=91.21, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=119.84, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.47, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.1, default_y=-35.0, dynamics=72.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.72, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.35, default_y=-20.0, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=262.98, default_y=-5.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=291.61, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=320.23, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=348.86, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=382.56, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=411.19, default_y=15.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='42', width=319.19):
            with Note(default_x=13.8, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.7, default_y=-5.0, dynamics=81.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=81.89, default_y=-10.0, dynamics=74.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.08, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.27, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=160.45, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='43', width=295.89):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='44', width=375.65):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(116.65)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='45', width=338.52):
            with Note(default_x=10.0, default_y=-5.0, dynamics=90.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.24, default_y=5.0, dynamics=86.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.49, default_y=0.0, dynamics=85.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.73, default_y=-5.0, dynamics=81.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=118.97, default_y=10.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.22, default_y=-10.0, dynamics=74.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=173.46, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=200.71, default_y=-5.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.95, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.19, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.44, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=309.68, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='46', width=342.32):
            with Note(default_x=13.8, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.04, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.29, default_y=0.0, dynamics=95.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.53, default_y=-5.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=122.77, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.02, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=177.26, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=204.51, default_y=-5.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=231.75, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.99, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.24, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=313.48, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='47', width=422.69):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(116.65)
            with Note(default_x=91.21, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=118.7, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.19, default_y=0.0, dynamics=96.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.68, default_y=15.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.17, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.66, default_y=-10.0, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=256.15, default_y=-15.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=283.64, default_y=-5.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=311.13, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=338.62, default_y=5.0, dynamics=95.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=366.11, default_y=0.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=393.6, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='48', width=283.5):
            with Note(default_x=10.0, default_y=-25.0, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.67, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=61.69, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.71, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.74, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.76, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=161.78, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='49', width=350.3):
            with Note(default_x=10.0, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=38.07, default_y=-20.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.15, default_y=-25.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.22, default_y=-30.0, dynamics=76.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=124.12, default_y=-15.0, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.19, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.26, default_y=-25.0, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=208.34, default_y=-15.0, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.41, default_y=-20.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.48, default_y=-25.0, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=292.56, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=320.63, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='50', width=366.94):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=91.21, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=131.82, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=172.44, default_y=-15.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=213.05, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=238.43, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=263.81, default_y=0.0, dynamics=96.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=289.19, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.58, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=339.96, default_y=5.0, dynamics=95.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='51', width=312.96):
            with Note(default_x=22.22, default_y=10.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='52', width=376.59):
            with Note(default_x=24.99, default_y=10.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=193.96, default_y=10.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=224.13, default_y=-15.0, dynamics=84.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.3, default_y=-20.0, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=284.47, default_y=-25.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.65, default_y=5.0, dynamics=96.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=344.82, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='53', width=360.4):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(99.63)
            with Note(default_x=91.21, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=130.86, default_y=-5.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=210.14, default_y=-10.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=234.92, default_y=0.0, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=259.69, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=284.47, default_y=-15.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=309.25, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=334.02, default_y=0.0, dynamics=95.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='54', width=362.36):
            with Note(default_x=10.0, default_y=5.0, dynamics=102.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=58.38, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=179.33, default_y=-5.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=209.57, default_y=-15.0, dynamics=76.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.81, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.04, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=300.28, default_y=-25.0, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.52, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='55', width=333.74):
            with Note(default_x=10.12, default_y=-5.0, dynamics=102.22):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.95, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.79, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.62, default_y=-5.0, dynamics=91.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=117.46, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.29, default_y=-10.0, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=171.13, default_y=-15.0, dynamics=74.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=197.96, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.8, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.63, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.47, default_y=-15.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.3, default_y=-10.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='56', width=402.85):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(99.63)
            with Note(default_x=91.21, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=117.05, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.88, default_y=0.0, dynamics=96.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.72, default_y=-5.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.56, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.39, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=246.23, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=272.07, default_y=-5.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.9, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=323.74, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=349.57, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=375.41, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='57', width=339.41):
            with Note(default_x=10.0, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.32, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.64, default_y=0.0, dynamics=96.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.95, default_y=15.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.27, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.59, default_y=-10.0, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=173.91, default_y=-15.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=201.22, default_y=-5.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.54, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.86, default_y=5.0, dynamics=95.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=283.18, default_y=0.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=310.49, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='58', width=314.24):
            with Note(default_x=14.0, default_y=-25.0, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.67, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.32, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.98, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=117.64, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.3, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=168.95, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='59', width=406.09):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(99.63)
            with Note(default_x=91.21, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='60', width=351.43):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='61', width=298.97):
            with Note(default_x=30.57, default_y=0.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=70.1, default_y=-5.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=149.15, default_y=-10.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=173.86, default_y=0.0, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.56, default_y=-25.0, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=223.26, default_y=-15.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=247.97, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=272.67, default_y=0.0, dynamics=95.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='62', width=361.75):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=95.01, default_y=5.0, dynamics=102.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=134.29, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=212.85, default_y=-5.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=237.4, default_y=5.0, dynamics=92.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=261.95, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.5, default_y=-15.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=311.05, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=335.6, default_y=5.0, dynamics=95.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='63', width=357.12):
            with Note(default_x=13.62, default_y=10.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.11, default_y=-15.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.61, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=99.1, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.59, default_y=-20.0, dynamics=73.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.08, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=184.57, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=213.06, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.56, default_y=5.0, dynamics=96.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.05, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=298.54, default_y=0.0, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=327.03, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='64', width=337.62):
            with Note(default_x=13.8, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.65, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.5, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.35, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.21, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.06, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=174.91, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=201.76, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.61, default_y=0.0, dynamics=96.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.46, default_y=-5.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.31, default_y=-5.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=309.17, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='65', width=456.13):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(124.43)
            with Note(default_x=91.21, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.49, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.77, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=182.04, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.32, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=242.6, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=272.87, default_y=-10.0, dynamics=74.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=303.15, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=333.43, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=363.7, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=393.98, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=424.25, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='66', width=253.72):
            with Note(default_x=10.0, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=47.25, default_y=-10.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=70.53, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.81, default_y=-20.0, dynamics=74.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=117.09, default_y=-15.0, dynamics=82.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=140.37, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='67', width=346.64):
            with Note(default_x=10.0, default_y=-5.0, dynamics=96.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.92, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.84, default_y=0.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.76, default_y=-5.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.68, default_y=10.0, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.6, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=177.52, default_y=-15.0, dynamics=74.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=205.44, default_y=-5.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=233.36, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=261.28, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=289.2, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.12, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='68', width=420.16):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(124.43)
            with Note(default_x=95.01, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.97, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.94, default_y=0.0, dynamics=95.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.9, default_y=-5.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.86, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=229.82, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=256.79, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=283.75, default_y=-5.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=310.71, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=337.67, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=364.64, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=391.6, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='69', width=349.06):
            with Note(default_x=13.8, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.6, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.41, default_y=0.0, dynamics=96.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.21, default_y=15.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.02, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.82, default_y=-10.0, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.63, default_y=-15.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=208.43, default_y=-5.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.24, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.04, default_y=5.0, dynamics=95.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=291.85, default_y=0.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.65, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='70', width=287.27):
            with Note(default_x=10.0, default_y=-25.0, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.67, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.07, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.48, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.89, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.3, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=163.71, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='71', width=1056.49):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(124.43)
            with Note(default_x=91.21, default_y=-30.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=171.52, default_y=-20.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.83, default_y=-25.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=332.13, default_y=-30.0, dynamics=76.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=412.44, default_y=-15.0, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=492.75, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=573.05, default_y=-25.0, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=653.36, default_y=-15.0, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=733.67, default_y=-20.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=813.97, default_y=-25.0, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=894.28, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=974.59, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='72', width=398.26):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(395.64)
                    TopSystemDistance(70.0)
            with Note(default_x=91.21, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=142.12, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=193.03, default_y=-15.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=243.94, default_y=-10.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='73', width=262.59):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=375.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('6')
                    BeatType('8')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=115.1, default_y=-140.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=115.1, default_y=-130.0, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=153.97, default_y=-155.0, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=153.97, default_y=-130.0, dynamics=86.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=231.7, default_y=-150.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=231.7, default_y=-130.0, dynamics=85.56):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=111.15, default_y=-195.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=150.02, default_y=-210.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=188.89, default_y=-215.0, dynamics=80.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=227.75, default_y=-220.0, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='2', width=270.4):
            with Note(default_x=17.75, default_y=-145.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=55.53, default_y=-140.0, dynamics=84.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=93.31, default_y=-150.0, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=131.08, default_y=-155.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-165.0, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-235.0, dynamics=84.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=51.58, default_y=-230.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=89.36, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=127.13, default_y=-210.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='3', width=346.99):
            with Note(default_x=17.57, default_y=-130.0, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=72.87, default_y=-135.0, dynamics=86.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=128.16, default_y=-140.0, dynamics=84.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=183.45, default_y=-125.0, dynamics=92.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=238.75, default_y=-115.0, dynamics=95.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=294.04, default_y=-125.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.62, default_y=-150.0, dynamics=93.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=179.5, default_y=-140.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.62, default_y=-220.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=68.92, default_y=-215.0, dynamics=85.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=124.21, default_y=-210.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=179.5, default_y=-230.0, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=234.8, default_y=-240.0, dynamics=75.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=290.09, default_y=-230.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='4', width=420.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=98.96, default_y=-135.0, dynamics=96.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=152.97, default_y=-140.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=206.97, default_y=-145.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=260.97, default_y=-130.0, dynamics=92.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=314.98, default_y=-120.0, dynamics=95.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=368.98, default_y=-130.0, dynamics=85.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=95.01, default_y=-160.0, dynamics=93.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=257.02, default_y=-145.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=95.01, default_y=-225.0, dynamics=91.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=149.02, default_y=-220.0, dynamics=90.0):
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
            with Note(default_x=203.02, default_y=-215.0, dynamics=91.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=257.02, default_y=-235.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=311.03, default_y=-245.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=365.03, default_y=-235.0, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='5', width=378.53):
            with Note(default_x=13.95, default_y=-140.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=13.95, default_y=-130.0, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=136.26, default_y=-145.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=136.26, default_y=-130.0, dynamics=86.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=197.41, default_y=-140.0, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=319.72, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=193.46, default_y=-150.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=315.77, default_y=-160.0, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-230.0, dynamics=91.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=71.15, default_y=-195.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=132.31, default_y=-200.0, dynamics=96.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=193.46, default_y=-205.0, dynamics=92.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=254.62, default_y=-220.0, dynamics=78.89):
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
            with Note(default_x=315.77, default_y=-215.0, dynamics=84.44):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='6', width=257.33):
            with Note(default_x=13.95, default_y=-155.0, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=13.95, default_y=-145.0, dynamics=86.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=51.75, default_y=-160.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=51.75, default_y=-140.0, dynamics=85.56):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=99.01, default_y=-150.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=99.01, default_y=-135.0, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=146.27, default_y=-155.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=146.27, default_y=-130.0, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-210.0, dynamics=91.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=47.81, default_y=-230.0, dynamics=74.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.06, default_y=-225.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=142.32, default_y=-245.0, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=180.12, default_y=-235.0, dynamics=81.11):
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
            with Note(default_x=217.93, default_y=-225.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='7', width=410.16):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=95.16, default_y=-155.0, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=201.1, default_y=-150.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=253.95, default_y=-155.0, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=253.95, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=359.66, default_y=-160.0, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-210.0, dynamics=102.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=144.3, default_y=-215.0, dynamics=91.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=197.15, default_y=-220.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=250.0, default_y=-225.0, dynamics=82.22):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=355.71, default_y=-230.0, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='8', width=318.11):
            with Note(default_x=17.75, default_y=-145.0, dynamics=95.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=68.2, default_y=-140.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=118.65, default_y=-150.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=169.11, default_y=-145.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-165.0, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-235.0, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=64.25, default_y=-230.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=114.7, default_y=-220.0, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=165.16, default_y=-210.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=215.61, default_y=-200.0, dynamics=96.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=266.06, default_y=-190.0, dynamics=96.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='9', width=328.22):
            with Note(default_x=17.75, default_y=-145.0, dynamics=90.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=69.89, default_y=-140.0, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=122.02, default_y=-150.0, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=174.16, default_y=-155.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=226.3, default_y=-150.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=278.44, default_y=-160.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-200.0, dynamics=95.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=65.94, default_y=-210.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=118.07, default_y=-220.0, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=170.21, default_y=-210.0, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=222.35, default_y=-220.0, dynamics=76.67):
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
            with Note(default_x=274.49, default_y=-230.0, dynamics=74.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='10', width=323.2):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(81.42)
            with Note(default_x=95.16, default_y=-165.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=142.62, default_y=-160.0, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=184.19, default_y=-150.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=225.77, default_y=-160.0, dynamics=93.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=225.77, default_y=-145.0, dynamics=93.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-236.42, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=138.67, default_y=-246.42, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=180.24, default_y=-256.42, dynamics=76.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=221.82, default_y=-241.42, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=255.08, default_y=-256.42, dynamics=78.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=288.34, default_y=-246.42, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='11', width=308.79):
            with Note(default_x=13.95, default_y=-165.0, dynamics=92.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=13.95, default_y=-145.0, dynamics=92.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=116.75, default_y=-165.0, dynamics=85.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=116.75, default_y=-150.0, dynamics=85.56):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=165.34, default_y=-165.0, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=165.34, default_y=-155.0, dynamics=83.33):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=262.54, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=262.54, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=262.54, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-251.42, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=58.6, default_y=-241.42, dynamics=90.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=112.8, default_y=-236.42, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=161.39, default_y=-231.42, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=209.99, default_y=-251.42, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=258.59, default_y=-261.42, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='12', width=164.85):
            with Note(default_x=13.95, default_y=-130.0, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=90.58, default_y=-130.0, dynamics=87.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-150.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=10.0, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=61.08, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=61.08, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=86.63, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=86.63, default_y=-140.0, dynamics=87.78):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-246.42, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=35.54, default_y=-271.42, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=61.08, default_y=-261.42, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=86.63, default_y=-246.42, dynamics=91.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=112.17, default_y=-236.42, dynamics=95.56):
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
            with Note(default_x=137.71, default_y=-226.42, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='13', width=259.65):
            with Note(default_x=22.58, default_y=-140.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=7.02, default_y=-45.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott ')
            with Note(default_x=58.72, default_y=-145.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-45.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist ')
            with Note(default_x=130.99, default_y=-150.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-45.6, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=167.13, default_y=-155.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=0.4, default_y=-45.6, relative_y=-30.0):
                    Syllabic('end')
                    Text('sre ')
                    Extend()
            with Note(default_x=189.71, default_y=-150.0, dynamics=83.33):
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
            with Note(default_x=212.3, default_y=-145.0, dynamics=88.89):
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
            with Note(default_x=234.88, default_y=-140.0, dynamics=93.33):
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
                Duration(12.0)
            with Note(default_x=22.58, default_y=-211.42, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=58.72, default_y=-226.42, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=94.85, default_y=-231.42, dynamics=82.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=130.99, default_y=-236.42, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=167.13, default_y=-241.42, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=212.3, default_y=-246.42, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='14', width=372.06):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=91.21, default_y=-135.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=9.01, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text("Sonn' ")
            with Note(default_x=136.39, default_y=-140.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.53, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und ')
            with Note(default_x=242.79, default_y=-145.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=10.03, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schild! ')
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-235.0, dynamics=82.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=136.39, default_y=-230.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=162.99, default_y=-225.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.59, default_y=-220.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=216.19, default_y=-215.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=242.79, default_y=-210.0, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=285.35, default_y=-245.0, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=327.9, default_y=-250.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='15', width=307.72):
            with Note(default_x=22.58, default_y=-130.0, dynamics=95.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=7.02, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott ')
            with Note(default_x=64.59, default_y=-135.0, dynamics=85.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist ')
            with Note(default_x=148.6, default_y=-140.0, dynamics=83.33):
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
                with Lyric(number='1', default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=201.11, default_y=-145.0, dynamics=81.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=253.61, default_y=-150.0, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.67, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('sre ')
            with Backup():
                Duration(12.0)
            with Note(default_x=22.58, default_y=-255.0, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=64.59, default_y=-250.0, dynamics=78.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.59, default_y=-245.0, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=148.6, default_y=-265.0, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='16', width=376.71):
            with Note(default_x=10.0, default_y=-125.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_x=0.4, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text("Sonn'")
                    Extend()
            with Note(default_x=60.36, default_y=-130.0, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=123.31, default_y=-115.0, dynamics=95.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.53, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und ')
            with Note(default_x=186.26, default_y=-120.0, dynamics=92.22):
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
                with Lyric(number='1', default_x=10.03, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schild! ')
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-235.0, dynamics=95.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=60.36, default_y=-230.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=91.83, default_y=-225.0, dynamics=92.22):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=123.31, default_y=-220.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.78, default_y=-215.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=186.26, default_y=-210.0, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=249.21, default_y=-205.0, dynamics=96.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=312.16, default_y=-210.0, dynamics=91.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='17', width=419.22):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(68.59)
            with Note(default_x=103.25, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
            with Note(default_x=149.7, default_y=-120.0, dynamics=86.67):
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
            with Note(default_x=196.14, default_y=-115.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.63, default_y=-47.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('rum ')
            with Note(default_x=242.59, default_y=-120.0, dynamics=84.44):
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
                with Lyric(number='1', default_y=-47.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rüh')
            with Note(default_x=301.51, default_y=-115.0, dynamics=86.67):
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
            with Note(default_x=330.54, default_y=-120.0, dynamics=84.44):
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
            with Note(default_x=359.57, default_y=-125.0, dynamics=78.89):
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
                with Lyric(number='1', default_y=-47.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('met ')
                    Extend()
            with Note(default_x=388.6, default_y=-130.0, dynamics=74.44):
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
            with Backup():
                Duration(12.0)
            with Note(default_x=103.25, default_y=-218.59, dynamics=91.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=149.7, default_y=-223.59, dynamics=80.0):
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
            with Note(default_x=196.14, default_y=-228.59, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=242.59, default_y=-213.59, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='18', width=316.61):
            with Note(default_x=17.23, default_y=-125.0, dynamics=86.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('des')
            with Note(default_x=58.3, default_y=-110.0, dynamics=95.56):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=109.65, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.69, default_y=-47.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen ')
            with Note(default_x=160.99, default_y=-120.0, dynamics=84.44):
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
                with Lyric(number='1', default_y=-47.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Gü')
            with Note(default_x=212.33, default_y=-125.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=263.67, default_y=-130.0, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.59, default_y=-47.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('te ')
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-218.59, dynamics=91.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=58.3, default_y=-223.59, dynamics=83.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=83.98, default_y=-228.59, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.65, default_y=-223.59, dynamics=84.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.32, default_y=-218.59, dynamics=90.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=160.99, default_y=-213.59, dynamics=92.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='19', width=320.66):
            with Note(default_x=17.23, default_y=-135.0, dynamics=81.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=61.63, default_y=-130.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=106.02, default_y=-125.0, dynamics=86.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.67, default_y=-47.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser ')
            with Note(default_x=150.42, default_y=-130.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dank')
            with Note(default_x=208.07, default_y=-125.0, dynamics=87.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=235.81, default_y=-130.0, dynamics=82.22):
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
            with Note(default_x=263.56, default_y=-135.0, dynamics=80.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-47.77, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ba')
            with Note(default_x=291.31, default_y=-140.0, dynamics=75.56):
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
                Duration(12.0)
            with Note(default_x=17.23, default_y=-228.59, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=61.63, default_y=-233.59, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.02, default_y=-238.59, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=150.42, default_y=-223.59, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='20', width=378.58):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(78.87)
            with Note(default_x=103.25, default_y=-135.0, dynamics=87.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('res ')
                    Extend()
            with Note(default_x=143.81, default_y=-120.0, dynamics=95.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=184.36, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-50.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ge')
            with Note(default_x=224.91, default_y=-130.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.85, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mü')
            with Note(default_x=275.6, default_y=-135.0, dynamics=80.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=326.29, default_y=-140.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=9.39, default_y=-50.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('te, ')
            with Backup():
                Duration(12.0)
            with Note(default_x=103.25, default_y=-238.87, dynamics=91.11):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=143.81, default_y=-248.87, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=184.36, default_y=-238.87, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=224.91, default_y=-233.87, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=326.29, default_y=-238.87, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='21', width=350.59):
            with Note(default_x=16.44, default_y=-125.0, dynamics=96.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.56, default_y=-50.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('die ')
            with Note(default_x=73.27, default_y=-115.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=0.4, default_y=-50.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('er ')
                    Extend()
            with Note(default_x=188.4, default_y=-115.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=233.86, default_y=-120.0, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-50.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('für ')
                    Extend()
            with Note(default_x=262.27, default_y=-125.0, dynamics=83.33):
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
            with Note(default_x=290.68, default_y=-130.0, dynamics=80.0):
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
                with Lyric(number='1', default_x=0.4, default_y=-50.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein ')
                    Extend()
            with Note(default_x=320.58, default_y=-135.0, dynamics=77.78):
                with Pitch():
                    Step('G')
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
            with Backup():
                Duration(12.0)
            with Note(default_x=16.44, default_y=-243.87, dynamics=86.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=73.27, default_y=-248.87, dynamics=81.11):
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
            with Note(default_x=131.58, default_y=-253.87, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=188.4, default_y=-228.87, dynamics=95.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=233.86, default_y=-223.87, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=290.68, default_y=-218.87, dynamics=95.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='22', width=327.32):
            with Note(default_x=10.94, default_y=-140.0, dynamics=78.89):
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
                with Lyric(number='1', default_y=-50.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Häuf')
            with Note(default_x=39.04, default_y=-145.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=67.15, default_y=-120.0, dynamics=96.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=112.12, default_y=-125.0, dynamics=91.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.43, default_y=-50.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein ')
            with Note(default_x=157.09, default_y=-130.0, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-50.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('hegt, ')
                    Extend()
            with Backup():
                Duration(12.0)
            with Note(default_x=10.94, default_y=-248.87, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=67.15, default_y=-243.87, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=112.12, default_y=-238.87, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=157.09, default_y=-258.87, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=213.3, default_y=-253.87, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=269.51, default_y=-248.87, dynamics=84.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='23', width=454.56):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(75.78)
            with Note(default_x=91.21, default_y=-130.0, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=91.57, default_y=-240.78, dynamics=92.22):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=151.8, default_y=-205.78, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=212.04, default_y=-210.78, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=272.27, default_y=-215.78, dynamics=92.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=332.5, default_y=-210.78, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=392.73, default_y=-205.78, dynamics=92.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='24', width=307.81):
            with Note(default_x=13.8, default_y=-130.0, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=171.25, default_y=-130.0, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=216.24, default_y=-135.0, dynamics=84.44):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.56, default_y=-49.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('die ')
            with Note(default_x=261.22, default_y=-140.0, dynamics=83.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.71, default_y=-49.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('er ')
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-210.78, dynamics=92.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=58.79, default_y=-220.78, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=115.02, default_y=-225.78, dynamics=76.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=171.25, default_y=-230.78, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=216.24, default_y=-215.78, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=261.22, default_y=-220.78, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='25', width=294.12):
            with Note(default_x=17.23, default_y=-145.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.7, default_y=-49.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('für ')
            with Note(default_x=61.28, default_y=-125.0, dynamics=92.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_x=0.4, default_y=-49.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein ')
                    Extend()
            with Note(default_x=105.33, default_y=-120.0, dynamics=93.33):
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
            with Note(default_x=132.85, default_y=-115.0, dynamics=94.44):
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
            with Note(default_x=160.38, default_y=-120.0, dynamics=91.11):
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
                with Lyric(number='1', default_y=-49.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Häuf')
            with Note(default_x=204.43, default_y=-130.0, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=248.48, default_y=-135.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.43, default_y=-49.96, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein ')
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-225.78, dynamics=86.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=61.28, default_y=-230.78, dynamics=78.89):
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
            with Note(default_x=105.33, default_y=-235.78, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=160.38, default_y=-220.78, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=204.43, default_y=-245.78, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=248.48, default_y=-235.78, dynamics=82.22):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='26', width=359.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(72.3)
            with Note(default_x=91.21, default_y=-130.0, dynamics=86.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=9.38, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hegt. ')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=211.3, default_y=-165.0, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=211.3, default_y=-145.0, dynamics=77.78):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-252.3, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=129.92, default_y=-232.3, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=168.63, default_y=-237.3, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=207.35, default_y=-242.3, dynamics=82.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='27', width=348.34):
            with Note(default_x=21.18, default_y=-160.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=75.66, default_y=-155.0, dynamics=84.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=130.13, default_y=-165.0, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=187.26, default_y=-160.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-257.3, dynamics=86.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=71.71, default_y=-252.3, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=126.18, default_y=-242.3, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=183.32, default_y=-232.3, dynamics=92.22):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=292.26, default_y=-227.3, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='28', width=348.34):
            with Note(default_x=21.18, default_y=-160.0, dynamics=90.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=75.66, default_y=-155.0, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=130.13, default_y=-165.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=187.26, default_y=-160.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-222.3, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=71.71, default_y=-217.3, dynamics=92.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=126.18, default_y=-242.3, dynamics=76.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=183.32, default_y=-232.3, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=237.79, default_y=-222.3, dynamics=91.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=292.26, default_y=-212.3, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='29', width=434.19):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=107.2, default_y=-145.0, dynamics=95.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=216.09, default_y=-165.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=273.21, default_y=-160.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=327.65, default_y=-145.0, dynamics=92.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=382.1, default_y=-155.0, dynamics=84.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=103.25, default_y=-215.0, dynamics=91.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=157.7, default_y=-225.0, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=212.14, default_y=-235.0, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=269.26, default_y=-225.0, dynamics=82.22):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=323.7, default_y=-235.0, dynamics=78.89):
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
            with Note(default_x=378.15, default_y=-245.0, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='30', width=274.13):
            with Note(default_x=13.95, default_y=-165.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=112.82, default_y=-155.0, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=160.96, default_y=-160.0, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-235.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=60.73, default_y=-245.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=108.87, default_y=-255.0, dynamics=78.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=157.01, default_y=-240.0, dynamics=86.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=195.52, default_y=-220.0, dynamics=97.78):
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
            with Note(default_x=234.03, default_y=-210.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='31', width=348.17):
            with Note(default_x=21.18, default_y=-160.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=132.74, default_y=-145.0, dynamics=90.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=187.19, default_y=-145.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=296.07, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=296.07, default_y=-135.0, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-215.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=71.68, default_y=-205.0, dynamics=95.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=128.79, default_y=-200.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=183.24, default_y=-195.0, dynamics=93.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=237.68, default_y=-215.0, dynamics=78.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=292.13, default_y=-225.0, dynamics=74.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='32', width=360.83):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(76.32)
            with Note(default_x=98.96, default_y=-130.0, dynamics=95.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=138.11, default_y=-145.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=177.25, default_y=-150.0, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=216.39, default_y=-155.0, dynamics=76.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=95.01, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=173.3, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=212.44, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=95.01, default_y=-221.32, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=134.16, default_y=-246.32, dynamics=74.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=173.3, default_y=-236.32, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=212.44, default_y=-256.32, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=261.37, default_y=-246.32, dynamics=82.22):
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
            with Note(default_x=310.3, default_y=-236.32, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='33', width=346.49):
            with Note(default_x=26.96, default_y=-120.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.64, default_y=-50.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('Denn ')
            with Note(default_x=72.38, default_y=-125.0, dynamics=90.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.71, default_y=-50.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('er ')
            with Note(default_x=185.93, default_y=-130.0, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.54, default_y=-50.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('will ')
            with Note(default_x=231.35, default_y=-135.0, dynamics=82.22):
                with Pitch():
                    Step('G')
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
                with Lyric(number='1', default_y=-50.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns ')
                    Extend()
            with Note(default_x=259.73, default_y=-130.0, dynamics=84.44):
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
            with Note(default_x=288.12, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=316.51, default_y=-120.0, dynamics=93.33):
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
                Duration(12.0)
            with Note(default_x=26.96, default_y=-221.32, dynamics=102.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=72.38, default_y=-226.32, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=100.77, default_y=-231.32, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=129.15, default_y=-236.32, dynamics=81.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.54, default_y=-241.32, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=185.93, default_y=-246.32, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=231.35, default_y=-251.32, dynamics=75.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=288.12, default_y=-256.32, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='34', width=349.17):
            with Note(default_x=17.23, default_y=-115.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-50.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fer')
            with Note(default_x=64.36, default_y=-120.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.53, default_y=-50.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('ner ')
            with Note(default_x=182.18, default_y=-125.0, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-50.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schüt')
            with Note(default_x=229.31, default_y=-130.0, dynamics=78.89):
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
                with Lyric(number='1', default_y=-50.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('zen, ')
                    Extend()
            with Note(default_x=259.21, default_y=-135.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=288.66, default_y=-140.0, dynamics=74.44):
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
            with Note(default_x=318.12, default_y=-145.0, dynamics=72.22):
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
                Duration(12.0)
            with Note(default_x=17.23, default_y=-261.32, dynamics=81.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=64.36, default_y=-256.32, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.82, default_y=-251.32, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=123.27, default_y=-246.32, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.73, default_y=-241.32, dynamics=92.22):
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
            with Note(default_x=182.18, default_y=-236.32, dynamics=95.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=288.66, default_y=-241.32, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='35', width=397.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(92.44)
            with Note(default_x=92.27, default_y=-110.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.88, default_y=-64.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('ob ')
            with Note(default_x=142.92, default_y=-130.0, dynamics=86.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.56, default_y=-64.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('die ')
            with Note(default_x=244.21, default_y=-125.0, dynamics=87.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-64.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Fein')
            with Note(default_x=294.86, default_y=-120.0, dynamics=91.11):
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
            with Note(default_x=345.51, default_y=-115.0, dynamics=91.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.61, default_y=-64.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('de ')
            with Backup():
                Duration(12.0)
            with Note(default_x=92.27, default_y=-262.44, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=142.92, default_y=-247.44, dynamics=94.44):
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
            with Note(default_x=193.57, default_y=-252.44, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=244.21, default_y=-257.44, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=294.86, default_y=-262.44, dynamics=81.11):
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
            with Note(default_x=345.51, default_y=-267.44, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='36', width=316.55):
            with Note(default_x=10.0, default_y=-135.0, dynamics=80.0):
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
                with Lyric(number='1', default_y=-64.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Pfei')
            with Note(default_x=35.41, default_y=-145.0, dynamics=72.22):
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
            with Note(default_x=60.83, default_y=-140.0, dynamics=76.67):
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
            with Note(default_x=86.24, default_y=-135.0, dynamics=81.11):
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
            with Note(default_x=111.65, default_y=-130.0, dynamics=87.78):
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
                with Lyric(number='1', default_y=-64.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('le ')
                    Extend()
            with Note(default_x=137.06, default_y=-125.0, dynamics=94.44):
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
            with Note(default_x=162.48, default_y=-120.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-64.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schnit')
            with Note(default_x=187.89, default_y=-125.0, dynamics=91.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=213.3, default_y=-130.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=264.13, default_y=-135.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.54, default_y=-64.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('zen ')
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-252.44, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=162.48, default_y=-237.44, dynamics=92.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=213.3, default_y=-252.44, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=264.13, default_y=-272.44, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='37', width=342.18):
            with Note(default_x=19.67, default_y=-140.0, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.53, default_y=-64.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('und ')
            with Note(default_x=74.07, default_y=-130.0, dynamics=86.67):
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
                with Lyric(number='1', default_x=0.4, default_y=-64.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('ein ')
                    Extend()
            with Note(default_x=101.27, default_y=-135.0, dynamics=80.0):
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
            with Note(default_x=128.47, default_y=-140.0, dynamics=76.67):
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
            with Note(default_x=155.67, default_y=-145.0, dynamics=73.33):
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
            with Note(default_x=182.87, default_y=-125.0, dynamics=96.67):
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
                with Lyric(number='1', default_y=-64.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Lä')
            with Note(default_x=212.77, default_y=-130.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=242.66, default_y=-135.0, dynamics=84.44):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=269.86, default_y=-140.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=297.06, default_y=-110.0, dynamics=97.78):
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
                Duration(12.0)
            with Note(default_x=19.67, default_y=-257.44, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=74.07, default_y=-237.44, dynamics=95.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=128.47, default_y=-222.44, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=182.87, default_y=-242.44, dynamics=84.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=242.66, default_y=-262.44, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=297.06, default_y=-272.44, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='38', width=454.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(86.9)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=120.97, default_y=-115.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ster')
            with Note(default_x=164.8, default_y=-120.0, dynamics=95.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.45, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('hund ')
            with Note(default_x=210.72, default_y=-125.0, dynamics=84.44):
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
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('gleich ')
                    Extend()
            with Note(default_x=252.05, default_y=-130.0, dynamics=81.11):
                with Pitch():
                    Step('A')
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
            with Note(default_x=280.75, default_y=-125.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=9.44, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('billt. ')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=92.27, default_y=-261.9, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=164.8, default_y=-241.9, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=210.72, default_y=-276.9, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=280.75, default_y=-226.9, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=338.16, default_y=-221.9, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=395.56, default_y=-216.9, dynamics=95.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='39', width=310.72):
            with Note(default_x=17.57, default_y=-130.0, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=68.68, default_y=-135.0, dynamics=86.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=117.56, default_y=-140.0, dynamics=84.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=166.43, default_y=-125.0, dynamics=92.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=215.31, default_y=-115.0, dynamics=95.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=264.19, default_y=-125.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.62, default_y=-150.0, dynamics=93.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=162.48, default_y=-140.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.62, default_y=-241.9, dynamics=84.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=64.73, default_y=-236.9, dynamics=82.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=113.61, default_y=-231.9, dynamics=85.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=162.48, default_y=-251.9, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=211.36, default_y=-261.9, dynamics=74.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=260.24, default_y=-251.9, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='40', width=291.21):
            with Note(default_x=17.75, default_y=-135.0, dynamics=96.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=63.69, default_y=-140.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=109.62, default_y=-145.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=155.56, default_y=-130.0, dynamics=92.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=201.49, default_y=-120.0, dynamics=95.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=247.43, default_y=-130.0, dynamics=85.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-160.0, dynamics=93.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=151.61, default_y=-145.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-246.9, dynamics=90.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=59.74, default_y=-241.9, dynamics=90.0):
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
            with Note(default_x=105.67, default_y=-236.9, dynamics=91.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=151.61, default_y=-256.9, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=197.54, default_y=-266.9, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=243.48, default_y=-256.9, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='41', width=441.41):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(66.42)
            with Note(default_x=95.16, default_y=-150.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=152.42, default_y=-160.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=266.93, default_y=-165.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=324.18, default_y=-155.0, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=386.51, default_y=-150.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-231.42, dynamics=91.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=148.47, default_y=-231.42, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=205.72, default_y=-226.42, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=262.98, default_y=-236.42, dynamics=82.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=320.23, default_y=-246.42, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=382.56, default_y=-256.42, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='42', width=319.19):
            with Note(default_x=17.75, default_y=-140.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=59.65, default_y=-135.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=112.03, default_y=-145.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=164.4, default_y=-160.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=164.4, default_y=-150.0, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-160.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=108.08, default_y=-165.0, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-266.42, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=55.7, default_y=-261.42, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=108.08, default_y=-256.42, dynamics=84.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=160.45, default_y=-241.42, dynamics=92.22):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.64, default_y=-206.42, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.83, default_y=-211.42, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.02, default_y=-216.42, dynamics=96.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=265.21, default_y=-221.42, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=291.4, default_y=-226.42, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='43', width=295.89):
            with Note(default_x=22.58, default_y=-140.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=7.02, default_y=-45.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott ')
            with Note(default_x=64.38, default_y=-145.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-45.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist ')
            with Note(default_x=147.99, default_y=-150.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-45.6, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=189.79, default_y=-155.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=0.4, default_y=-45.6, relative_y=-30.0):
                    Syllabic('end')
                    Text('sre ')
                    Extend()
            with Note(default_x=215.92, default_y=-150.0, dynamics=83.33):
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
            with Note(default_x=242.04, default_y=-145.0, dynamics=88.89):
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
            with Note(default_x=268.17, default_y=-140.0, dynamics=93.33):
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
                Duration(12.0)
            with Note(default_x=22.58, default_y=-231.42, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=64.38, default_y=-211.42, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.19, default_y=-216.42, dynamics=90.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=147.99, default_y=-221.42, dynamics=85.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=189.79, default_y=-226.42, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=242.04, default_y=-231.42, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='44', width=375.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=91.21, default_y=-135.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=9.01, default_y=-40.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("Sonn' ")
            with Note(default_x=136.39, default_y=-140.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.53, default_y=-40.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('und ')
            with Note(default_x=244.42, default_y=-145.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=10.03, default_y=-40.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schild! ')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-235.0, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=136.39, default_y=-230.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=163.4, default_y=-225.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.4, default_y=-220.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.41, default_y=-215.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=244.42, default_y=-210.0, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=287.63, default_y=-225.0, dynamics=81.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=330.84, default_y=-235.0, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='45', width=338.52):
            with Note(default_x=13.95, default_y=-155.0, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=122.92, default_y=-150.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=177.41, default_y=-155.0, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=286.39, default_y=-160.0, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-245.0, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=64.49, default_y=-250.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=118.97, default_y=-255.0, dynamics=77.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=173.46, default_y=-260.0, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=282.44, default_y=-265.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='46', width=342.32):
            with Note(default_x=17.75, default_y=-145.0, dynamics=95.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=72.24, default_y=-140.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=126.72, default_y=-150.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=181.21, default_y=-145.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-165.0, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-270.0, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=68.29, default_y=-265.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=122.77, default_y=-255.0, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=177.26, default_y=-245.0, dynamics=91.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=231.75, default_y=-235.0, dynamics=94.44):
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
            with Note(default_x=286.24, default_y=-225.0, dynamics=95.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='47', width=422.69):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=95.16, default_y=-145.0, dynamics=90.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=150.14, default_y=-140.0, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=205.12, default_y=-150.0, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=260.1, default_y=-155.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=315.08, default_y=-150.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=370.06, default_y=-160.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-235.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=146.19, default_y=-245.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=201.17, default_y=-255.0, dynamics=78.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=256.15, default_y=-245.0, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=311.13, default_y=-255.0, dynamics=81.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=366.11, default_y=-265.0, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='48', width=283.5):
            with Note(default_x=13.95, default_y=-165.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=65.64, default_y=-160.0, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=115.69, default_y=-150.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=165.73, default_y=-160.0, dynamics=93.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=165.73, default_y=-145.0, dynamics=93.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-220.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=61.69, default_y=-230.0, dynamics=92.22):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=111.74, default_y=-240.0, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=161.78, default_y=-225.0, dynamics=93.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=201.82, default_y=-240.0, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=241.86, default_y=-230.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='49', width=350.3):
            with Note(default_x=13.95, default_y=-165.0, dynamics=92.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=13.95, default_y=-145.0, dynamics=92.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=128.07, default_y=-165.0, dynamics=85.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=128.07, default_y=-150.0, dynamics=85.56):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=184.21, default_y=-165.0, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=184.21, default_y=-155.0, dynamics=83.33):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=296.5, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=296.5, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=296.5, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-235.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=66.15, default_y=-225.0, dynamics=90.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=124.12, default_y=-220.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=180.26, default_y=-215.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=236.41, default_y=-235.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=292.56, default_y=-245.0, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='50', width=366.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(69.22)
            with Note(default_x=95.16, default_y=-130.0, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=217.0, default_y=-130.0, dynamics=87.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-150.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=91.21, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=172.44, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=172.44, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=213.05, default_y=-140.0, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-234.22, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=131.82, default_y=-224.22, dynamics=93.33):
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
            with Note(default_x=172.44, default_y=-214.22, dynamics=95.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=213.05, default_y=-199.22, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=263.81, default_y=-214.22, dynamics=87.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=314.58, default_y=-224.22, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='51', width=312.96):
            with Note(default_x=22.58, default_y=-140.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=7.02, default_y=-45.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott ')
            with Note(default_x=67.01, default_y=-145.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-45.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist ')
            with Note(default_x=155.87, default_y=-150.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-45.6, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=200.29, default_y=-155.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=0.4, default_y=-45.6, relative_y=-30.0):
                    Syllabic('end')
                    Text('sre ')
                    Extend()
            with Note(default_x=228.06, default_y=-150.0, dynamics=83.33):
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
            with Note(default_x=255.83, default_y=-145.0, dynamics=88.89):
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
            with Note(default_x=283.6, default_y=-140.0, dynamics=93.33):
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
                Duration(12.0)
            with Note(default_x=22.58, default_y=-234.22, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=67.01, default_y=-214.22, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=111.44, default_y=-219.22, dynamics=84.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=155.87, default_y=-224.22, dynamics=82.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=200.29, default_y=-229.22, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=255.83, default_y=-234.22, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='52', width=376.59):
            with Note(default_x=24.99, default_y=-135.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=9.01, default_y=-45.6, relative_y=-30.0):
                    Syllabic('single')
                    Text("Sonn' ")
            with Note(default_x=73.27, default_y=-140.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.53, default_y=-45.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('und ')
            with Note(default_x=193.96, default_y=-145.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=9.23, default_y=-45.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schild, ')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=24.99, default_y=-239.22, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=73.27, default_y=-234.22, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=103.44, default_y=-229.22, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.61, default_y=-224.22, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.78, default_y=-219.22, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=193.96, default_y=-214.22, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=254.3, default_y=-209.22, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=314.65, default_y=-204.22, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='53', width=360.4):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(81.27)
            with Note(default_x=91.21, default_y=-130.0, dynamics=95.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=7.02, default_y=-45.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott ')
            with Note(default_x=130.86, default_y=-135.0, dynamics=85.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-45.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist ')
            with Note(default_x=210.14, default_y=-140.0, dynamics=83.33):
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
                with Lyric(number='1', default_y=-45.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=259.69, default_y=-145.0, dynamics=81.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=309.25, default_y=-150.0, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.67, default_y=-45.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('sre ')
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-211.27, dynamics=102.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=130.86, default_y=-231.27, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=170.5, default_y=-226.27, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=210.14, default_y=-221.27, dynamics=87.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='54', width=362.36):
            with Note(default_x=10.0, default_y=-125.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_x=0.4, default_y=-45.45, relative_y=-30.0):
                    Syllabic('single')
                    Text("Sonn' ")
                    Extend()
            with Note(default_x=58.38, default_y=-130.0, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=118.86, default_y=-115.0, dynamics=95.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.53, default_y=-45.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('und ')
            with Note(default_x=179.33, default_y=-120.0, dynamics=92.22):
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
                with Lyric(number='1', default_x=9.23, default_y=-45.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schild. ')
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-251.27, dynamics=82.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=58.38, default_y=-246.27, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=88.62, default_y=-241.27, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=118.86, default_y=-236.27, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.09, default_y=-231.27, dynamics=91.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=179.33, default_y=-226.27, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=239.81, default_y=-241.27, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=300.28, default_y=-251.27, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='55', width=333.74):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=63.79, default_y=-120.0, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=7.02, default_y=-45.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott ')
            with Note(default_x=117.46, default_y=-115.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-45.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist ')
            with Note(default_x=171.13, default_y=-130.0, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=224.8, default_y=-135.0, dynamics=76.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=278.47, default_y=-140.0, dynamics=77.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.67, default_y=-45.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('sre ')
            with Backup():
                Duration(12.0)
            with Note(default_x=10.12, default_y=-261.27, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=63.79, default_y=-231.27, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=117.46, default_y=-236.27, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=224.8, default_y=-241.27, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=278.47, default_y=-246.27, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='56', width=402.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(92.7)
            with Note(default_x=91.21, default_y=-145.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_x=0.4, default_y=-54.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("Sonn' ")
                    Extend()
            with Note(default_x=142.88, default_y=-120.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=194.56, default_y=-115.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.53, default_y=-54.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('und ')
            with Note(default_x=246.23, default_y=-130.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=0.4, default_y=-54.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schild, ')
                    Extend()
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-262.7, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=142.88, default_y=-242.7, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=194.56, default_y=-247.7, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=297.9, default_y=-252.7, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=349.57, default_y=-257.7, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='57', width=339.41):
            with Note(default_x=10.0, default_y=-130.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=64.64, default_y=-150.0, dynamics=78.89):
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
                with Lyric(number='1', default_y=-54.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=91.95, default_y=-145.0, dynamics=82.22):
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
            with Note(default_x=119.27, default_y=-140.0, dynamics=86.67):
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
                with Lyric(number='1', default_x=0.4, default_y=-54.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('sre ')
                    Extend()
            with Note(default_x=146.59, default_y=-135.0, dynamics=88.89):
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
            with Note(default_x=173.91, default_y=-130.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Lyric(number='1', default_x=0.4, default_y=-54.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("Sonn' ")
                    Extend()
            with Note(default_x=228.54, default_y=-120.0, dynamics=96.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=255.86, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=283.18, default_y=-120.0, dynamics=95.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.53, default_y=-54.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('und ')
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-262.7, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=64.64, default_y=-257.7, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=119.27, default_y=-267.7, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=228.54, default_y=-282.7, dynamics=78.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=283.18, default_y=-272.7, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='58', width=314.24):
            with Note(default_x=14.0, default_y=-120.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=0.4, default_y=-54.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schild ')
                    Extend()
            with Note(default_x=168.95, default_y=-120.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=210.01, default_y=-125.0, dynamics=85.56):
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
                with Lyric(number='1', default_y=-54.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=235.66, default_y=-130.0, dynamics=82.22):
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
            with Note(default_x=261.32, default_y=-125.0, dynamics=85.56):
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
                with Lyric(number='1', default_x=0.4, default_y=-54.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('sre ')
                    Extend()
            with Note(default_x=286.98, default_y=-115.0, dynamics=92.22):
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
                Duration(12.0)
            with Note(default_x=14.0, default_y=-282.7, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=66.32, default_y=-292.7, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=117.64, default_y=-282.7, dynamics=84.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=168.95, default_y=-277.7, dynamics=85.56):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=210.01, default_y=-242.7, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=261.32, default_y=-247.7, dynamics=96.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='59', width=406.09):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(91.2)
            with Note(default_x=91.21, default_y=-120.0, dynamics=94.44):
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
                with Lyric(number='1', default_x=0.4, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("Sonn' ")
                    Extend()
            with Note(default_x=119.18, default_y=-125.0, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.16, default_y=-130.0, dynamics=76.67):
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
            with Note(default_x=175.13, default_y=-135.0, dynamics=73.33):
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
            with Note(default_x=203.1, default_y=-140.0, dynamics=72.22):
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
            with Note(default_x=231.07, default_y=-145.0, dynamics=72.22):
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
            with Note(default_x=259.04, default_y=-140.0, dynamics=74.44):
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
            with Note(default_x=287.01, default_y=-150.0, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=314.98, default_y=-125.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=359.74, default_y=-130.0, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.53, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('und ')
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-251.2, dynamics=96.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=147.16, default_y=-261.2, dynamics=83.33):
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
            with Note(default_x=203.1, default_y=-271.2, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=259.04, default_y=-256.2, dynamics=86.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=314.98, default_y=-276.2, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='60', width=351.43):
            with Note(default_x=11.06, default_y=-130.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=0.4, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schild, ')
                    Extend()
            with Note(default_x=199.26, default_y=-130.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=249.45, default_y=-115.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=9.01, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("Sonn' ")
            with Note(default_x=299.64, default_y=-145.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.53, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('und ')
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=42.42, default_y=-241.2, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=73.79, default_y=-246.2, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.16, default_y=-251.2, dynamics=85.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.53, default_y=-256.2, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.9, default_y=-261.2, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=199.26, default_y=-246.2, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=249.45, default_y=-281.2, dynamics=73.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=299.64, default_y=-271.2, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='61', width=298.97):
            with Note(default_x=30.57, default_y=-150.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=10.03, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schild! ')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=153.1, default_y=-150.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=153.1, default_y=-130.0, dynamics=85.56):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=30.57, default_y=-291.2, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=70.1, default_y=-236.2, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=109.63, default_y=-241.2, dynamics=95.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=149.15, default_y=-246.2, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='62', width=361.75):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=98.96, default_y=-145.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=138.24, default_y=-140.0, dynamics=84.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=177.52, default_y=-150.0, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=216.8, default_y=-155.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=95.01, default_y=-165.0, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=95.01, default_y=-235.0, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=134.29, default_y=-230.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=173.57, default_y=-220.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=212.85, default_y=-210.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='63', width=357.12):
            with Note(default_x=17.57, default_y=-130.0, dynamics=96.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=74.56, default_y=-135.0, dynamics=86.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=131.54, default_y=-140.0, dynamics=84.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=188.52, default_y=-125.0, dynamics=92.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=245.51, default_y=-115.0, dynamics=95.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=302.49, default_y=-125.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.62, default_y=-150.0, dynamics=93.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=184.57, default_y=-140.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.62, default_y=-220.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=70.61, default_y=-215.0, dynamics=85.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=127.59, default_y=-210.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=184.57, default_y=-230.0, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=241.56, default_y=-240.0, dynamics=75.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=298.54, default_y=-230.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='64', width=337.62):
            with Note(default_x=17.75, default_y=-135.0, dynamics=96.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=71.45, default_y=-140.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=125.16, default_y=-145.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=178.86, default_y=-130.0, dynamics=92.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=232.56, default_y=-120.0, dynamics=95.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=286.26, default_y=-130.0, dynamics=85.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-160.0, dynamics=93.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=174.91, default_y=-145.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-225.0, dynamics=91.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=67.5, default_y=-220.0, dynamics=90.0):
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
            with Note(default_x=121.21, default_y=-215.0, dynamics=91.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=174.91, default_y=-235.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=228.61, default_y=-245.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=282.31, default_y=-235.0, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='65', width=456.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=95.16, default_y=-140.0, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=95.16, default_y=-130.0, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=216.27, default_y=-145.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=216.27, default_y=-130.0, dynamics=86.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=276.82, default_y=-140.0, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=397.93, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=272.87, default_y=-150.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=333.43, default_y=-155.0, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=393.98, default_y=-160.0, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-230.0, dynamics=91.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=151.77, default_y=-195.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=212.32, default_y=-200.0, dynamics=96.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=272.87, default_y=-205.0, dynamics=92.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=333.43, default_y=-220.0, dynamics=78.89):
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
            with Note(default_x=393.98, default_y=-215.0, dynamics=84.44):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='66', width=253.72):
            with Note(default_x=13.95, default_y=-155.0, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=13.95, default_y=-145.0, dynamics=86.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=51.2, default_y=-160.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=51.2, default_y=-140.0, dynamics=85.56):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=97.76, default_y=-150.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=97.76, default_y=-135.0, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=144.32, default_y=-155.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=144.32, default_y=-130.0, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-210.0, dynamics=91.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=47.25, default_y=-230.0, dynamics=74.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=93.81, default_y=-225.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=140.37, default_y=-245.0, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=177.62, default_y=-235.0, dynamics=81.11):
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
            with Note(default_x=214.87, default_y=-225.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='67', width=346.64):
            with Note(default_x=13.95, default_y=-155.0, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=125.63, default_y=-150.0, dynamics=84.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=181.47, default_y=-155.0, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=293.15, default_y=-160.0, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-210.0, dynamics=102.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=65.84, default_y=-215.0, dynamics=91.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=121.68, default_y=-220.0, dynamics=86.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=177.52, default_y=-225.0, dynamics=82.22):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=289.2, default_y=-230.0, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='68', width=420.16):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=98.96, default_y=-145.0, dynamics=95.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=152.89, default_y=-140.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=206.81, default_y=-150.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=260.74, default_y=-145.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=95.01, default_y=-165.0, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=95.01, default_y=-235.0, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=148.94, default_y=-230.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.86, default_y=-220.0, dynamics=91.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=256.79, default_y=-210.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=310.71, default_y=-200.0, dynamics=96.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=364.64, default_y=-190.0, dynamics=96.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='69', width=349.06):
            with Note(default_x=17.75, default_y=-145.0, dynamics=90.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=73.36, default_y=-140.0, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=128.97, default_y=-150.0, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=184.58, default_y=-155.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=240.19, default_y=-150.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=295.8, default_y=-160.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-200.0, dynamics=95.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=69.41, default_y=-210.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=125.02, default_y=-220.0, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=180.63, default_y=-210.0, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=236.24, default_y=-220.0, dynamics=76.67):
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
            with Note(default_x=291.85, default_y=-230.0, dynamics=74.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='70', width=287.27):
            with Note(default_x=13.95, default_y=-165.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=66.02, default_y=-160.0, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=116.84, default_y=-150.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=167.66, default_y=-160.0, dynamics=93.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=167.66, default_y=-145.0, dynamics=93.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=62.07, default_y=-230.0, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=112.89, default_y=-240.0, dynamics=76.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=163.71, default_y=-225.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=204.37, default_y=-240.0, dynamics=78.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=245.02, default_y=-230.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='71', width=1056.49):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=95.16, default_y=-165.0, dynamics=92.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=95.16, default_y=-145.0, dynamics=92.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=416.39, default_y=-165.0, dynamics=85.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=416.39, default_y=-150.0, dynamics=85.56):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=577.0, default_y=-165.0, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=577.0, default_y=-155.0, dynamics=83.33):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=898.23, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=898.23, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=898.23, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-235.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=251.83, default_y=-225.0, dynamics=90.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=412.44, default_y=-220.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=573.05, default_y=-215.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=733.67, default_y=-235.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=894.28, default_y=-245.0, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='72', width=398.26):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=95.16, default_y=-130.0, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=247.89, default_y=-130.0, dynamics=87.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-150.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=91.21, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=193.03, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=193.03, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=243.94, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=243.94, default_y=-140.0, dynamics=87.78):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=91.21, default_y=-230.0, dynamics=90.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=142.12, default_y=-255.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=193.03, default_y=-245.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=243.94, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=294.85, default_y=-220.0):
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
            with Note(default_x=345.75, default_y=-210.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='73', width=262.59):
            with Note(default_x=17.75, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=17.75, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter', size='cue')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')