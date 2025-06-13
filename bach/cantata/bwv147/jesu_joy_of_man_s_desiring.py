with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Jesu Bleibet Meine Freude')
    with Identification():
        Creator('J. S. Bach', type='composer')
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
        CreditWords('Jesu Bleibet Meine Freude', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords("Jesu, Joy of Man's Desiring", default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J. S. Bach', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
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
        with ScorePart(id='P2'):
            PartName('Flauta doce Soprano')
            PartAbbreviation('S. fla. doce')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Flauta doce Soprano')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(75)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Flauta doce Tenor')
            PartAbbreviation('T. Fla. Doce')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Flauta doce Tenor')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(75)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=283.79):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(204.0)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
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
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='2', width=196.57):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='3', width=196.57):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='4', width=196.57):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='5', width=264.05):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.4)
                        RightMargin(0.0)
                    SystemDistance(137.07)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='6', width=198.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='7', width=198.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='8', width=198.37):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='9', width=90.64):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='10', width=156.16):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.4)
                        RightMargin(0.0)
                    SystemDistance(137.07)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='11', width=90.48):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='12', width=197.85):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='13', width=197.85):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='14', width=90.48):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='15', width=90.48):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='16', width=125.79):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='17', width=286.8):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.4)
                        RightMargin(0.0)
                    SystemDistance(137.07)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='18', width=220.76):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='19', width=220.76):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='20', width=220.76):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='21', width=266.9):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.4)
                        RightMargin(0.0)
                    SystemDistance(137.07)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='22', width=200.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='23', width=200.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=93.49):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='25', width=93.49):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='26', width=93.49):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='27', width=261.02):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.4)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='28', width=194.98):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='29', width=87.61):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='30', width=87.61):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='31', width=122.91):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='32', width=194.98):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='33', width=286.8):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.4)
                        RightMargin(0.0)
                    SystemDistance(100.66)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=220.76):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=220.76):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=220.76):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='37', width=269.42):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.4)
                        RightMargin(0.0)
                    SystemDistance(100.66)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='38', width=203.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='39', width=219.75):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='40', width=95.65):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='41', width=160.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='42', width=179.51):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.4)
                        RightMargin(-0.0)
                    SystemDistance(100.66)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='43', width=198.18):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='44', width=208.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='45', width=203.9):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='46', width=81.24):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='47', width=78.16):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='48', width=208.46):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.4)
                        RightMargin(0.0)
                    SystemDistance(100.66)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='49', width=220.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='50', width=220.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='51', width=213.77):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='52', width=85.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='53', width=155.98):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.4)
                        RightMargin(0.0)
                    SystemDistance(100.66)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='54', width=90.41):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='55', width=198.4):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='56', width=197.67):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='57', width=90.3):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='58', width=90.3):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='59', width=126.03):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='60', width=285.18):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.4)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='61', width=220.77):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='62', width=224.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='63', width=219.14):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='64', width=286.8):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.4)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='65', width=220.76):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='66', width=220.76):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='67', width=220.76):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='68', width=318.23):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.4)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='69', width=252.19):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='70', width=252.19):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='71', width=126.49):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=283.79):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
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
                    ClefOctaveChange(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=119.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=139.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=159.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=179.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=199.09, default_y=-15.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=219.07, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=239.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=259.02, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='2', width=196.57):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=31.98, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=51.95, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=71.93, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=91.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=111.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=131.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=151.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=171.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='3', width=196.57):
            with Note(default_x=12.0, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=31.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=51.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=71.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=91.9, default_y=-15.0):
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
                Beam('continue', number=1)
            with Note(default_x=111.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=131.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=151.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=171.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='4', width=196.57):
            with Note(default_x=12.0, default_y=-35.0):
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
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=31.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=51.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=71.93, default_y=-45.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=91.9, default_y=-35.0):
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
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=111.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=131.85, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=151.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=171.8, default_y=-25.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='5', width=264.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=78.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=98.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=118.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=138.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=158.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=178.82, default_y=-15.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=198.98, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=219.13, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=239.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='6', width=198.01):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=32.16, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=52.31, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=72.47, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=92.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=112.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=132.94, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=153.09, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=173.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='7', width=198.01):
            with Note(default_x=12.0, default_y=-40.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=32.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=52.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=72.47, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=92.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=112.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=132.94, default_y=-45.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=153.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=173.25, default_y=-35.0):
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
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='8', width=198.37):
            with Note(default_x=12.36, default_y=-30.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=32.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=52.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=72.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=92.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=113.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=133.3, default_y=-30.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=153.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=173.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='9', width=90.64):
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=63.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=156.16):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=78.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.17, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='11', width=90.48):
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=63.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=197.85):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=32.14, default_y=-45.0):
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
                Beam('continue', number=1)
            with Note(default_x=52.27, default_y=-40.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=72.41, default_y=-35.0):
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
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=92.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=112.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=132.81, default_y=-25.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=152.95, default_y=-15.0):
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
                Beam('continue', number=1)
            with Note(default_x=173.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='13', width=197.85):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=32.14, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=52.27, default_y=-35.0):
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
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=72.41, default_y=-45.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=92.54, default_y=-35.0):
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
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=112.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=132.81, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=152.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=173.09, default_y=-25.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='14', width=90.48):
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=63.49, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=90.48):
            with Note(default_x=12.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=63.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=125.79):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=33.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=49.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=64.89, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=94.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='17', width=286.8):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=78.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=101.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=124.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=147.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=170.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=193.04, default_y=-15.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=216.04, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=239.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=262.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='18', width=220.76):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=35.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=58.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=81.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=104.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=127.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=150.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=173.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=196.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='19', width=220.76):
            with Note(default_x=12.0, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=35.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=58.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=81.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=104.0, default_y=-15.0):
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
                Beam('continue', number=1)
            with Note(default_x=127.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=150.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=173.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=196.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='20', width=220.76):
            with Note(default_x=12.0, default_y=-35.0):
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
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=35.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=58.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=81.0, default_y=-45.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=104.0, default_y=-35.0):
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
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=127.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=150.0, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=173.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=196.0, default_y=-25.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='21', width=266.9):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=78.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=98.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=119.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=139.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=160.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=180.6, default_y=-15.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=201.11, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=221.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=242.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='22', width=200.86):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=32.51, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=53.02, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=73.54, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=94.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=114.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=135.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=155.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=176.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='23', width=200.86):
            with Note(default_x=12.0, default_y=-40.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=32.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=53.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=73.54, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=94.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=114.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=135.07, default_y=-45.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=155.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=176.1, default_y=-35.0):
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
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='24', width=93.49):
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=65.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='25', width=93.49):
            with Note(default_x=12.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=65.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='26', width=93.49):
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=65.5, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='27', width=261.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=78.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=97.82, default_y=-45.0):
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
                Beam('continue', number=1)
            with Note(default_x=117.59, default_y=-40.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=137.37, default_y=-35.0):
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
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=157.15, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=176.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=196.7, default_y=-25.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=216.47, default_y=-15.0):
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
                Beam('continue', number=1)
            with Note(default_x=236.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='28', width=194.98):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=31.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=51.55, default_y=-35.0):
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
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=71.33, default_y=-45.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=91.11, default_y=-35.0):
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
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=110.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=130.66, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=150.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=170.21, default_y=-25.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='29', width=87.61):
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=61.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='30', width=87.61):
            with Note(default_x=12.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=61.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='31', width=122.91):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=48.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=64.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=92.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='32', width=194.98):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=31.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=51.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=71.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=91.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=110.88, default_y=-15.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=130.66, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=150.43, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=170.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='33', width=286.8):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=78.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=101.04, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=124.04, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=147.04, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=170.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=193.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=216.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=239.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=262.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='34', width=220.76):
            with Note(default_x=12.0, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=35.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=58.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=81.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=104.0, default_y=-15.0):
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
                Beam('continue', number=1)
            with Note(default_x=127.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=150.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=173.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=196.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='35', width=220.76):
            with Note(default_x=12.0, default_y=-35.0):
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
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=35.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=58.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=81.0, default_y=-45.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=104.0, default_y=-35.0):
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
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=127.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=150.0, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=173.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=196.0, default_y=-25.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='36', width=220.76):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=35.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=58.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=81.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=104.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=127.0, default_y=-15.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=150.0, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=173.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=196.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='37', width=269.42):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=78.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=98.87, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=119.7, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=140.52, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=161.35, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=182.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=203.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=223.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=244.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='38', width=203.38):
            with Note(default_x=12.0, default_y=-40.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=32.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=53.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=74.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=95.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=116.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=136.96, default_y=-45.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=157.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=178.62, default_y=-35.0):
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
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='39', width=219.75):
            with Note(default_x=12.0, default_y=-30.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=33.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=55.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=77.61, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=99.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=121.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=143.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=165.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=194.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='40', width=95.65):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=66.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='41', width=160.88):
            with Note(default_x=15.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=108.49, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='42', width=179.51):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=78.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=121.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=152.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='43', width=198.18):
            with Note(default_x=12.0, default_y=-25.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=31.25, default_y=-15.0):
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
                Beam('continue', number=1)
            with Note(default_x=50.5, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=69.75, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=89.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=108.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=127.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=154.16, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=173.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='44', width=208.12):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=31.98, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=63.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=83.46, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=103.44, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=123.42, default_y=-15.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=143.39, default_y=-25.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=163.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=183.35, default_y=-15.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='45', width=203.9):
            with Note(default_x=14.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=33.32, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=52.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=71.96, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=91.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=110.59, default_y=-25.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=129.91, default_y=-40.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=149.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=179.13, default_y=-30.0):
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
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='46', width=81.24):
            with Note(default_x=15.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=56.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='47', width=78.16):
            with Note(default_x=12.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=53.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='48', width=208.46):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=86.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=136.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=162.71, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=178.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='49', width=220.86):
            with Note(default_x=12.0, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=33.43, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=60.09, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=81.52, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=102.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=124.38, default_y=-15.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=145.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=167.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=196.1, default_y=-20.0):
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
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='50', width=220.33):
            with Note(default_x=14.0, default_y=-25.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=35.37, default_y=-15.0):
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
                Beam('continue', number=1)
            with Note(default_x=56.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=78.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=99.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=126.16, default_y=-35.0):
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
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=147.53, default_y=-45.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=168.9, default_y=-40.0):
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
                Beam('continue', number=1)
            with Note(default_x=195.57, default_y=-35.0):
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
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='51', width=213.77):
            with Note(default_x=12.0, default_y=-40.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=33.02, default_y=-50.0):
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
                Beam('continue', number=1)
            with Note(default_x=54.03, default_y=-45.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=75.05, default_y=-40.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=96.06, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=125.96, default_y=-35.0):
                with Pitch():
                    Step('F')
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=146.97, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=167.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=189.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='52', width=85.66):
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=60.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='53', width=155.98):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=78.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='54', width=90.41):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='55', width=198.4):
            with Note(default_x=12.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=32.84, default_y=-45.0):
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
                Beam('continue', number=1)
            with Note(default_x=52.95, default_y=-40.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=73.06, default_y=-35.0):
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
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=93.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=113.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=133.4, default_y=-25.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=153.52, default_y=-15.0):
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
                Beam('continue', number=1)
            with Note(default_x=173.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='56', width=197.67):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=32.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=52.23, default_y=-35.0):
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
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=72.34, default_y=-45.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=92.45, default_y=-35.0):
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
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=112.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=132.68, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=152.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=172.91, default_y=-25.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='57', width=90.3):
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=63.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='58', width=90.3):
            with Note(default_x=12.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=63.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='59', width=126.03):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=33.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=49.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=64.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='60', width=285.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=78.4, default_y=-30.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=101.15, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=123.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=146.66, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=169.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=192.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=214.91, default_y=-30.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=237.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=260.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='61', width=220.77):
            with Note(default_x=14.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=36.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=59.5, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=82.25, default_y=-30.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=105.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=127.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=150.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=173.26, default_y=-15.0):
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
                Beam('continue', number=1)
            with Note(default_x=196.01, default_y=-25.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='62', width=224.01):
            with Note(default_x=17.23, default_y=-35.0):
                with Pitch():
                    Step('F')
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=39.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=62.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=85.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=108.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=130.99, default_y=-30.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=153.74, default_y=-40.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=176.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=199.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='63', width=219.14):
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=35.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=57.86, default_y=-35.0):
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
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=80.61, default_y=-45.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=103.37, default_y=-35.0):
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
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=126.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=148.87, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=171.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=194.37, default_y=-25.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='64', width=286.8):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=78.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=101.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=124.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=147.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=170.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=193.04, default_y=-15.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=216.04, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=239.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=262.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='65', width=220.76):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=35.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=58.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=81.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=104.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=127.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=150.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=173.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=196.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='66', width=220.76):
            with Note(default_x=12.0, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=35.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=58.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=81.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=104.0, default_y=-15.0):
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
                Beam('continue', number=1)
            with Note(default_x=127.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=150.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=173.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=196.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='67', width=220.76):
            with Note(default_x=12.0, default_y=-35.0):
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
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=35.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=58.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=81.0, default_y=-45.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=104.0, default_y=-35.0):
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
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=127.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=150.0, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=173.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=196.0, default_y=-25.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='68', width=318.23):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=78.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=104.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=131.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=157.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=184.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=210.59, default_y=-15.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=237.1, default_y=-15.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=263.61, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=290.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='69', width=252.19):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=38.51, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=65.02, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=91.53, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=118.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=144.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=171.06, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=197.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=224.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='70', width=252.19):
            with Note(default_x=12.0, default_y=-40.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=38.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=65.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=91.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=118.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=144.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=171.06, default_y=-45.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=197.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=224.08, default_y=-35.0):
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
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='71', width=126.49):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=283.79):
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
            with Note(default_x=99.22, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=159.14, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=219.07, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=196.57):
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.93, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=131.85, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='3', width=196.57):
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.93, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=131.85, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=196.57):
            with Note(default_x=12.0, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.93, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=131.85, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=264.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.04, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=138.51, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=198.98, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=198.01):
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.47, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=132.94, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=198.01):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.47, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=132.94, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=198.37):
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='9', width=90.64):
            with Note(default_x=12.72, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.16, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=63.6, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='10', width=156.16):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.4, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.79, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.17, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='11', width=90.48):
            with Note(default_x=12.72, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.11, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=63.49, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='12', width=197.85):
            with Note(default_x=12.0, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.41, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=132.81, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=197.85):
            with Note(default_x=12.0, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.41, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=132.81, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='14', width=90.48):
            with Note(default_x=12.72, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.11, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=63.49, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='15', width=90.48):
            with Note(default_x=12.72, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.11, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=63.49, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=125.79):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=64.89, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=94.54, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='17', width=286.8):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.04, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=147.04, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=216.04, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=220.76):
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.0, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=150.0, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='19', width=220.76):
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=150.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=220.76):
            with Note(default_x=12.0, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.0, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.0, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='21', width=266.9):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.04, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=139.58, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=201.11, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='22', width=200.86):
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=73.54, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.07, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='23', width=200.86):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.54, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=135.07, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=93.49):
            with Note(default_x=12.72, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.11, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=65.5, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='25', width=93.49):
            with Note(default_x=12.72, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.11, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=65.5, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='26', width=93.49):
            with Note(default_x=12.72, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.11, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=65.5, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='27', width=261.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.04, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=137.37, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=196.7, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='28', width=194.98):
            with Note(default_x=12.0, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.33, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=130.66, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='29', width=87.61):
            with Note(default_x=12.72, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.15, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.58, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='30', width=87.61):
            with Note(default_x=12.72, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.15, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=61.58, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='31', width=122.91):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=64.13, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=92.72, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='32', width=194.98):
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.33, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=130.66, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='33', width=286.8):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.04, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=147.04, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=216.04, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='34', width=220.76):
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=150.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='35', width=220.76):
            with Note(default_x=12.0, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.0, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.0, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=220.76):
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.0, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=150.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='37', width=269.42):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.04, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=140.52, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=203.0, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='38', width=203.38):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=74.48, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=136.96, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='39', width=219.75):
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=77.61, default_y=-135.0):
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
                Stem('up')
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    Slur(type='stop', number=1)
            with Note(default_x=121.35, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
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
            with Note(default_x=143.22, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
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
            with Note(default_x=194.98, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
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
        with Measure(number='40', width=95.65):
            with Note(default_x=12.36, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.59, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=66.82, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='41', width=160.88):
            with Note(default_x=15.8, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.43, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=81.83, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.49, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=133.89, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='42', width=179.51):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.04, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=103.17, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=152.78, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='43', width=198.18):
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.75, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=127.5, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='44', width=208.12):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.46, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=143.39, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='45', width=203.9):
            with Note(default_x=14.0, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.96, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=129.91, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='46', width=81.24):
            with Note(default_x=15.8, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=36.14, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=56.47, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='47', width=78.16):
            with Note(default_x=12.72, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=33.06, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=53.39, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='48', width=208.46):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=86.84, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=115.33, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=178.38, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='49', width=220.86):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.52, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=145.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='50', width=220.33):
            with Note(default_x=14.0, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=78.12, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=147.53, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='51', width=213.77):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=75.05, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
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
                    Slur(type='stop', number=1)
            with Note(default_x=125.96, default_y=-120.0):
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
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=146.97, default_y=-125.0):
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
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=189.0, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
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
        with Measure(number='52', width=85.66):
            with Note(default_x=12.72, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=36.5, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=60.28, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='53', width=155.98):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.4, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=103.73, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.06, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='54', width=90.41):
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.6, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=63.21, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='55', width=198.4):
            with Note(default_x=12.36, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=133.4, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='56', width=197.67):
            with Note(default_x=12.0, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.34, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=132.68, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='57', width=90.3):
            with Note(default_x=12.72, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.05, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=63.38, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='58', width=90.3):
            with Note(default_x=12.72, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.05, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=63.38, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='59', width=126.03):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=65.22, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=94.82, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='60', width=285.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.04, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=214.91, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='61', width=220.77):
            with Note(default_x=14.0, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=82.25, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.51, default_y=-135.0):
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
        with Measure(number='62', width=224.01):
            with Note(default_x=17.23, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=85.48, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=153.74, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='63', width=219.14):
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=148.87, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='64', width=286.8):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.04, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=147.04, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=216.04, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='65', width=220.76):
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.0, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=150.0, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='66', width=220.76):
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=150.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='67', width=220.76):
            with Note(default_x=12.0, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.0, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.0, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='68', width=318.23):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.04, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=157.57, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=237.1, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='69', width=252.19):
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=91.53, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=171.06, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='70', width=252.19):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=91.53, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=171.06, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='71', width=126.49):
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')