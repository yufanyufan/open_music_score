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
        CreditWords('Magnificat in E-flat major', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('BWV 243a', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J. S. Bach', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Trumpet')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('C トランペット')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(57)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Trumpet')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('C トランペット')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(3)
                MidiProgram(57)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Trumpet')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('C トランペット')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(5)
                MidiProgram(57)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Timpani')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('ティンパニ')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(7)
                MidiProgram(48)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P5'):
            PartName('Oboe')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('オーボエ')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(8)
                MidiProgram(69)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P6'):
            PartName('Oboe')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('オーボエ')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(9)
                MidiProgram(69)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P7'):
            PartName('Violin')
            with ScoreInstrument(id='P7-I1'):
                InstrumentName('ヴァイオリン')
            MidiDevice(None, id='P7-I1', port=1)
            with MidiInstrument(id='P7-I1'):
                MidiChannel(11)
                MidiProgram(41)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P8'):
            PartName('Violin')
            with ScoreInstrument(id='P8-I1'):
                InstrumentName('ヴァイオリン')
            MidiDevice(None, id='P8-I1', port=1)
            with MidiInstrument(id='P8-I1'):
                MidiChannel(14)
                MidiProgram(41)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P9'):
            PartName('Viola')
            with ScoreInstrument(id='P9-I1'):
                InstrumentName('ヴィオラ')
            MidiDevice(None, id='P9-I1', port=2)
            with MidiInstrument(id='P9-I1'):
                MidiChannel(1)
                MidiProgram(42)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P10'):
            PartName('Soprano')
            with ScoreInstrument(id='P10-I1'):
                InstrumentName('ソプラノ')
            MidiDevice(None, id='P10-I1', port=2)
            with MidiInstrument(id='P10-I1'):
                MidiChannel(4)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P11'):
            PartName('Soprano')
            with ScoreInstrument(id='P11-I1'):
                InstrumentName('ソプラノ')
            MidiDevice(None, id='P11-I1', port=2)
            with MidiInstrument(id='P11-I1'):
                MidiChannel(5)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P12'):
            PartName('Alto')
            with ScoreInstrument(id='P12-I1'):
                InstrumentName('アルト')
            MidiDevice(None, id='P12-I1', port=2)
            with MidiInstrument(id='P12-I1'):
                MidiChannel(6)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P13'):
            PartName('Tenor')
            with ScoreInstrument(id='P13-I1'):
                InstrumentName('テナー')
            MidiDevice(None, id='P13-I1', port=2)
            with MidiInstrument(id='P13-I1'):
                MidiChannel(7)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P14'):
            PartName('Bariton')
            with ScoreInstrument(id='P14-I1'):
                InstrumentName('バリトン')
            MidiDevice(None, id='P14-I1', port=2)
            with MidiInstrument(id='P14-I1'):
                MidiChannel(8)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P15'):
            PartName('Organ')
            with ScoreInstrument(id='P15-I1'):
                InstrumentName('オルガン')
            MidiDevice(None, id='P15-I1', port=2)
            with MidiInstrument(id='P15-I1'):
                MidiChannel(9)
                MidiProgram(20)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P16'):
            PartName('Violoncello')
            with ScoreInstrument(id='P16-I1'):
                InstrumentName('チェロ')
            MidiDevice(None, id='P16-I1', port=2)
            with MidiInstrument(id='P16-I1'):
                MidiChannel(11)
                MidiProgram(43)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=255.05):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(119.2)
                        RightMargin(0.0)
                    TopSystemDistance(92.71)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('12: Gloria Patri - Sicut erat in principio', relative_x=113.16, relative_y=70.71, font_size='16')
            with Note(default_x=120.77, default_y=25.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=171.03, default_y=25.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.42, default_y=25.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=315.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=387.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(50.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=149.49):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=120.23):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='7', width=352.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(50.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=378.03):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=124.36):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=126.16):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(50.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=356.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=318.27):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(50.0)
            with Note(default_x=110.92, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=152.02, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=244.48, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=20.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=100.34, default_y=20.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=128.15, default_y=20.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='17', width=247.17):
            with Note(default_x=18.64, default_y=0.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.37, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=103.74, default_y=10.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=131.74, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='18', width=219.25):
            with Note(default_x=19.12, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=71.36, default_y=10.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=97.49, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=123.25, default_y=10.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    TopSystemDistance(50.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=158.89, default_y=-30.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=196.9, default_y=-20.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=234.9, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=272.9, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=310.9, default_y=-20.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=249.58):
            with Note(default_x=15.8, default_y=-30.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.8, default_y=-20.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=91.8, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=129.81, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=167.81, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=205.81, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='22', width=227.88):
            with Note(default_x=12.12, default_y=-20.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=245.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(50.0)
            with Note(default_x=103.52, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=157.99, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=340.45):
            with Note(default_x=12.0, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.48, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='26', width=305.07):
            with Note(default_x=12.12, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=52.31, default_y=-20.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(50.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='28', width=250.42):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=47.67, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=67.58, default_y=0.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=87.5, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.42, default_y=10.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=130.68, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=162.55, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=185.82, default_y=10.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.73, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=225.65, default_y=0.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=228.11):
            with Note(default_x=15.8, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='30', width=237.76):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(50.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='32', width=280.06):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='33', width=231.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=239.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(50.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=318.45):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=66.28, default_y=-30.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=116.39, default_y=-20.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=166.51, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=216.62, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=266.74, default_y=-20.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='37', width=318.45):
            with Note(default_x=16.16, default_y=-30.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=66.28, default_y=-20.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=116.39, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=166.51, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=216.62, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=266.74, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(50.0)
            with Note(default_x=100.08, default_y=-20.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=150.66, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=201.24, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=251.81, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=302.39, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=327.68, default_y=10.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=352.97, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=378.26, default_y=0.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='39', width=342.73):
            with Note(default_x=15.8, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.02, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='40', width=329.62):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=67.84, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=119.87, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=171.91, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=223.94, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.96, default_y=10.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.98, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.0, default_y=0.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(50.0)
            with Note(default_x=103.52, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=153.53, default_y=0.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.55, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.57, default_y=10.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=303.59, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=20.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=433.63, default_y=15.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=483.65, default_y=10.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=533.67, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=583.68, default_y=0.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=633.7, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-5.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=255.05):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=120.77, default_y=-80.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=171.03, default_y=-80.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.42, default_y=-80.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=315.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=387.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=149.49):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=120.23):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='7', width=352.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=378.03):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=124.36):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=126.16):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=356.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=318.27):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=110.92, default_y=-90.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=152.02, default_y=-90.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=-90.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=-90.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=244.48, default_y=-90.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=100.34, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=128.15, default_y=-85.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='17', width=247.17):
            with Note(default_x=18.64, default_y=-80.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=47.01, default_y=-85.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=75.37, default_y=-90.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=103.74, default_y=-95.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=131.74, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='18', width=219.25):
            with Note(default_x=15.8, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('whole')
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=-95.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=158.89, default_y=-135.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=196.9, default_y=-125.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=234.9, default_y=-115.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=272.9, default_y=-115.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=310.9, default_y=-125.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='21', width=249.58):
            with Note(default_x=15.8, default_y=-135.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.8, default_y=-125.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=91.8, default_y=-115.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=129.81, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=167.81, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=205.81, default_y=-115.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='22', width=227.88):
            with Note(default_x=12.12, default_y=-125.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=245.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-90.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=157.99, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=340.45):
            with Note(default_x=12.0, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.48, default_y=-115.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='26', width=305.07):
            with Note(default_x=12.12, default_y=-115.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.31, default_y=-125.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='28', width=250.42):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=47.67, default_y=-90.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=67.58, default_y=-95.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=87.5, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.42, default_y=-95.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=130.68, default_y=-90.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=162.55, default_y=-95.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=205.73, default_y=-115.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='29', width=228.11):
            with Note(default_x=15.8, default_y=-125.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='30', width=237.76):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='32', width=280.06):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='33', width=231.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=239.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=318.45):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=66.28, default_y=-135.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=116.39, default_y=-125.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=166.51, default_y=-115.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=216.62, default_y=-115.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=266.74, default_y=-125.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='37', width=318.45):
            with Note(default_x=16.16, default_y=-135.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=66.28, default_y=-125.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=116.39, default_y=-115.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=166.51, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=216.62, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=266.74, default_y=-115.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=100.08, default_y=-125.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=150.66, default_y=-115.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=201.24, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=251.81, default_y=-90.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=302.39, default_y=-90.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=327.68, default_y=-95.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=352.97, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=378.26, default_y=-95.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='39', width=342.73):
            with Note(default_x=15.8, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.02, default_y=-125.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='40', width=329.62):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=67.84, default_y=-115.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=119.87, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=171.91, default_y=-90.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=223.94, default_y=-90.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.96, default_y=-95.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.98, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.0, default_y=-105.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=153.53, default_y=-95.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.55, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.57, default_y=-95.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=303.59, default_y=-90.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=483.65, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=583.68, default_y=-115.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-115.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=255.05):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=120.77, default_y=-190.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=171.03, default_y=-190.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.42, default_y=-190.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=315.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=387.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=149.49):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=120.23):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='7', width=352.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=378.03):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=124.36):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=126.16):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=356.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=318.27):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=110.92, default_y=-195.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=152.02, default_y=-195.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=-195.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=-195.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=244.48, default_y=-195.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=-180.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=43.98, default_y=-175.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=72.16, default_y=-180.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=100.34, default_y=-185.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=128.15, default_y=-190.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=247.17):
            with Note(default_x=18.64, default_y=-190.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=75.01, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=188.83, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=219.25):
            with Note(default_x=19.12, default_y=-220.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.36, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=97.49, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=123.61, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=165.4, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=158.89, default_y=-245.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=196.9, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=234.9, default_y=-220.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=272.9, default_y=-220.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=310.9, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='21', width=249.58):
            with Note(default_x=15.8, default_y=-245.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.8, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=91.8, default_y=-220.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=129.81, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=167.81, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=205.81, default_y=-220.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='22', width=227.88):
            with Note(default_x=12.12, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=245.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-195.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=157.99, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=340.45):
            with Note(default_x=12.0, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=66.48, default_y=-220.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='26', width=305.07):
            with Note(default_x=12.12, default_y=-220.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.31, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='28', width=250.42):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=47.67, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=67.58, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=87.5, default_y=-195.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.68, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=162.55, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=205.73, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='29', width=228.11):
            with Note(default_x=15.8, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='30', width=237.76):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='32', width=280.06):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='33', width=231.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=239.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=318.45):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=66.28, default_y=-245.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=116.39, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=166.51, default_y=-220.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=216.62, default_y=-220.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=266.74, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='37', width=318.45):
            with Note(default_x=16.16, default_y=-245.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=66.28, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=116.39, default_y=-220.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=166.51, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=216.62, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=266.74, default_y=-220.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=100.08, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=150.66, default_y=-220.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=201.24, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=251.81, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=277.1, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=302.39, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=327.68, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=352.97, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=378.26, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='39', width=342.73):
            with Note(default_x=15.8, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.02, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='40', width=329.62):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=67.84, default_y=-220.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=119.87, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=171.91, default_y=-195.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=223.94, default_y=-195.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=275.98, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=203.55, default_y=-220.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=303.59, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=-230.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=483.65, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=583.68, default_y=-210.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-220.0, dynamics=71.11):
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
    with Part(id='P4'):
        with Measure(number='1', width=255.05):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=120.77, default_y=-315.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=171.03, default_y=-315.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=196.42, default_y=-315.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='2', width=315.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=387.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=149.49):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=120.23):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='7', width=352.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=378.03):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=124.36):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=126.16):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=356.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=318.27):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=110.92, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=152.02, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=244.48, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='17', width=247.17):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=75.37, default_y=-315.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=103.74, default_y=-315.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=132.1, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=188.83, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=219.25):
            with Note(default_x=19.12, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.36, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=97.49, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=123.61, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=165.4, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=-315.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=120.89, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='21', width=249.58):
            with Note(default_x=15.8, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='22', width=227.88):
            with Note(default_x=12.12, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=245.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=340.45):
            with Note(default_x=12.0, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='26', width=305.07):
            with Note(default_x=12.12, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='28', width=250.42):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=47.67, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=67.58, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=87.5, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.68, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=162.55, default_y=-315.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=205.73, default_y=-315.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='29', width=228.11):
            with Note(default_x=15.8, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='30', width=237.76):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='32', width=280.06):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='33', width=231.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=239.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=318.45):
            with Note(default_x=16.16, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='37', width=318.45):
            with Note(default_x=16.16, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=100.08, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=251.81, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=302.39, default_y=-315.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=352.97, default_y=-315.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='39', width=342.73):
            with Note(default_x=15.8, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.02, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='40', width=329.62):
            with Note(default_x=15.8, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=171.91, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=223.94, default_y=-315.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=275.98, default_y=-315.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=203.55, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=253.57, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=303.59, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=483.65, default_y=-315.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=583.68, default_y=-315.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-300.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=255.05):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=120.77, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=171.03, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.42, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=315.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=387.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=149.49):
            with Note(default_x=14.0, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=64.71, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=90.35, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='6', width=120.23):
            with Note(default_x=14.36, default_y=-395.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=66.32, default_y=-395.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='7', width=352.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=378.03):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=124.36):
            with Note(default_x=14.0, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=53.24, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=78.15, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=126.16):
            with Note(default_x=15.8, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=55.04, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=79.95, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=356.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=318.27):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=110.92, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=152.02, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=244.48, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=100.34, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=128.15, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='17', width=247.17):
            with Note(default_x=18.28, default_y=-390.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=131.74, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='18', width=219.25):
            with Note(default_x=19.12, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=45.24, default_y=-390.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=71.36, default_y=-395.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=97.49, default_y=-390.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=123.25, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=-390.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=120.89, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.89, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.89, default_y=-390.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.89, default_y=-395.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=196.9, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=215.9, default_y=-405.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.9, default_y=-410.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.9, default_y=-405.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=272.9, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=291.9, default_y=-395.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=310.9, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=329.9, default_y=-395.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='21', width=249.58):
            with Note(default_x=15.8, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.8, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.8, default_y=-390.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=72.8, default_y=-395.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=91.8, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=110.81, default_y=-405.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=129.81, default_y=-410.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.81, default_y=-405.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=167.81, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.81, default_y=-395.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.81, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.81, default_y=-395.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='22', width=227.88):
            with Note(default_x=12.12, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=245.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=185.23, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=212.47, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=239.7, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.94, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.18, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=321.42, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=348.65, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=375.89, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=403.13, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='25', width=340.45):
            with Note(default_x=12.0, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=93.71, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=120.95, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=148.19, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.43, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.66, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=229.9, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=257.14, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=284.38, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=311.61, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='26', width=305.07):
            with Note(default_x=12.12, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=134.2, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=157.47, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.73, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=202.21, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=225.47, default_y=-365.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=268.43, default_y=-365.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=291.7, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.96, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.44, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=250.42):
            with Note(default_x=15.8, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.58, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=87.5, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=228.11):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='30', width=237.76):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='32', width=280.06):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=47.39, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=69.43, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=91.48, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=114.74, default_y=-365.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=138.01, default_y=-360.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=182.09, default_y=-360.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=205.36, default_y=-365.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.63, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.29, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='33', width=231.12):
            with Note(default_x=15.8, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='34', width=239.86):
            with Note(default_x=15.8, default_y=-370.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-370.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
        with Measure(number='36', width=318.45):
            with Note(default_x=16.16, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.22, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.28, default_y=-390.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.33, default_y=-395.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=116.39, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.45, default_y=-405.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.51, default_y=-410.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.56, default_y=-405.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=216.62, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=241.68, default_y=-395.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.74, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=291.79, default_y=-395.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='37', width=318.45):
            with Note(default_x=16.16, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.22, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.28, default_y=-390.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.33, default_y=-395.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=116.39, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.45, default_y=-405.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.51, default_y=-410.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.56, default_y=-405.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=216.62, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=241.68, default_y=-395.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.74, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=291.79, default_y=-395.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=100.08, default_y=-400.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='39', width=342.73):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=70.02, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=97.13, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=124.24, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=151.35, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=178.46, default_y=-365.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=232.68, default_y=-365.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=259.79, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.9, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.02, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='40', width=329.62):
            with Note(default_x=15.8, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.82, default_y=-390.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.84, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.85, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.87, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.89, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=171.91, default_y=-365.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=223.94, default_y=-365.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.96, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.98, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.0, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=153.53, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.55, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.57, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=303.59, default_y=-365.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=-360.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=433.63, default_y=-365.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=483.65, default_y=-370.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=533.67, default_y=-375.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=583.68, default_y=-380.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=633.7, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-385.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P6'):
        with Measure(number='1', width=255.05):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=120.77, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=171.03, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.42, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=315.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=387.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=149.49):
            with Note(default_x=14.0, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=64.71, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=90.35, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='6', width=120.23):
            with Note(default_x=14.36, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
            with Note(default_x=66.32, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=352.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=378.03):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=124.36):
            with Note(default_x=14.0, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=53.24, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=78.15, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=126.16):
            with Note(default_x=15.8, default_y=-490.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=55.04, default_y=-490.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=79.95, default_y=-490.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=356.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=318.27):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=110.92, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=152.02, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=244.48, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=-490.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=100.34, default_y=-490.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=128.15, default_y=-490.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='17', width=247.17):
            with Note(default_x=15.32, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='18', width=219.25):
            with Note(default_x=18.76, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=123.61, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=165.4, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=191.53, default_y=-490.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=-510.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=120.89, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=177.89, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=196.9, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=215.9, default_y=-510.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.9, default_y=-515.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.9, default_y=-510.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=272.9, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=291.9, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=310.9, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=329.9, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='21', width=249.58):
            with Note(default_x=15.8, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=72.8, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=91.8, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=110.81, default_y=-510.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=129.81, default_y=-515.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.81, default_y=-510.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=167.81, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.81, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.81, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.81, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='22', width=227.88):
            with Note(default_x=12.12, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=245.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=130.75, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.99, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.23, default_y=-490.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=212.47, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=239.7, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.94, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.18, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=321.42, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=348.65, default_y=-490.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=375.89, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=403.13, default_y=-490.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='25', width=340.45):
            with Note(default_x=12.0, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.24, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.48, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.71, default_y=-490.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=120.95, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=148.19, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.43, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.66, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=229.9, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=257.14, default_y=-490.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=284.38, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=311.61, default_y=-490.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='26', width=305.07):
            with Note(default_x=12.12, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=134.2, default_y=-470.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=157.47, default_y=-475.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.73, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=202.21, default_y=-475.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=225.47, default_y=-470.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=268.43, default_y=-470.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=291.7, default_y=-475.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.96, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.44, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=250.42):
            with Note(default_x=15.8, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.58, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=87.5, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=228.11):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='30', width=237.76):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='32', width=280.06):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=47.39, default_y=-490.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=91.48, default_y=-475.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=114.74, default_y=-470.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=138.01, default_y=-465.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=182.09, default_y=-465.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=205.36, default_y=-470.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.63, default_y=-475.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.29, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='33', width=231.12):
            with Note(default_x=15.8, default_y=-475.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='34', width=239.86):
            with Note(default_x=15.8, default_y=-475.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-475.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
        with Measure(number='36', width=318.45):
            with Note(default_x=16.16, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.22, default_y=-490.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.28, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.33, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=116.39, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.45, default_y=-510.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.51, default_y=-515.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.56, default_y=-510.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=216.62, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=241.68, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.74, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=291.79, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='37', width=318.45):
            with Note(default_x=16.16, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=91.33, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=116.39, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.45, default_y=-510.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.51, default_y=-515.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.56, default_y=-510.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=216.62, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=241.68, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.74, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=291.79, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=100.08, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='39', width=342.73):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=70.02, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=124.24, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=151.35, default_y=-475.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=178.46, default_y=-470.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=232.68, default_y=-470.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=259.79, default_y=-475.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.9, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.02, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='40', width=329.62):
            with Note(default_x=15.8, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.84, default_y=-505.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.85, default_y=-500.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.87, default_y=-495.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=171.91, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=223.94, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.96, default_y=-475.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.98, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.0, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=153.53, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.55, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.57, default_y=-475.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=303.59, default_y=-470.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=483.65, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=583.68, default_y=-485.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-480.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P7'):
        with Measure(number='1', width=255.05):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=120.77, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=171.03, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.42, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=315.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=387.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=149.49):
            with Note(default_x=14.0, default_y=-550.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=64.71, default_y=-550.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=90.35, default_y=-550.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='6', width=120.23):
            with Note(default_x=14.36, default_y=-550.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=66.32, default_y=-550.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='7', width=352.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=378.03):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=124.36):
            with Note(default_x=14.0, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=53.24, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=78.15, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=126.16):
            with Note(default_x=15.8, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=55.04, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=79.95, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=356.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=318.27):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=110.92, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=152.02, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=244.48, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=-560.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=100.34, default_y=-560.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=128.15, default_y=-560.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='17', width=247.17):
            with Note(default_x=18.28, default_y=-570.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=131.74, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='18', width=219.25):
            with Note(default_x=18.76, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=123.61, default_y=-570.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=165.4, default_y=-575.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=120.89, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.89, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='21', width=249.58):
            with Note(default_x=15.8, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.8, default_y=-575.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='22', width=227.88):
            with Note(default_x=12.12, default_y=-575.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=40.95, default_y=-590.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=245.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=157.99, default_y=-590.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=212.47, default_y=-575.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=266.94, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=321.42, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=375.89, default_y=-575.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='25', width=340.45):
            with Note(default_x=12.0, default_y=-590.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.48, default_y=-575.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=120.95, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=175.43, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=229.9, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=284.38, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='26', width=305.07):
            with Note(default_x=12.12, default_y=-575.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=134.2, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=180.73, default_y=-550.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=225.47, default_y=-575.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=246.95, default_y=-570.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=268.43, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=291.7, default_y=-560.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=314.96, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='28', width=250.42):
            with Note(default_x=15.8, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.58, default_y=-560.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=87.5, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=228.11):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='30', width=237.76):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=40.05, default_y=-595.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=68.92, default_y=-590.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=86.37, default_y=-585.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=115.24, default_y=-580.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=132.7, default_y=-575.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=160.63, default_y=-575.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=178.08, default_y=-580.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.54, default_y=-585.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=213.0, default_y=-590.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.83, default_y=-595.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='32', width=280.06):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='33', width=231.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=239.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=318.45):
            with Note(default_x=16.16, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.28, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='37', width=318.45):
            with Note(default_x=16.16, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.28, default_y=-575.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(62.92)
            with Note(default_x=100.08, default_y=-582.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=150.66, default_y=-597.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=251.81, default_y=-582.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=302.39, default_y=-572.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=352.97, default_y=-562.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='39', width=342.73):
            with Note(default_x=15.8, default_y=-562.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=178.46, default_y=-582.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=232.68, default_y=-572.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=286.9, default_y=-562.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='40', width=329.62):
            with Note(default_x=15.8, default_y=-547.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.84, default_y=-582.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.85, default_y=-577.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.87, default_y=-572.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.89, default_y=-567.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=171.91, default_y=-562.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=223.94, default_y=-562.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.96, default_y=-567.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.98, default_y=-572.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.0, default_y=-577.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=153.53, default_y=-570.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.55, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.57, default_y=-560.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=303.59, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=-550.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=433.63, default_y=-555.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=483.65, default_y=-560.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=533.67, default_y=-565.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=583.68, default_y=-570.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=633.7, default_y=-575.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-575.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P8'):
        with Measure(number='1', width=255.05):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=120.77, default_y=-675.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=171.03, default_y=-675.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.42, default_y=-675.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=315.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=387.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=149.49):
            with Note(default_x=14.0, default_y=-660.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=64.71, default_y=-660.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=90.35, default_y=-660.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='6', width=120.23):
            with Note(default_x=14.36, default_y=-665.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=66.32, default_y=-665.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='7', width=352.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=378.03):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=124.36):
            with Note(default_x=14.0, default_y=-675.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=53.24, default_y=-675.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=78.15, default_y=-675.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=126.16):
            with Note(default_x=15.8, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=55.04, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=79.95, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=356.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=318.27):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=110.92, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=152.02, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=244.48, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=100.34, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=128.15, default_y=-680.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='17', width=247.17):
            with Note(default_x=18.28, default_y=-675.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=131.74, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='18', width=219.25):
            with Note(default_x=19.12, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=45.24, default_y=-665.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=71.36, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=97.49, default_y=-675.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=123.25, default_y=-680.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=-665.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=120.89, default_y=-660.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.89, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='21', width=249.58):
            with Note(default_x=15.8, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.8, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='22', width=227.88):
            with Note(default_x=12.12, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=40.95, default_y=-695.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=245.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=157.99, default_y=-695.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=212.47, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=266.94, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=321.42, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=375.89, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='25', width=340.45):
            with Note(default_x=12.0, default_y=-695.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=66.48, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=120.95, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=175.43, default_y=-660.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=229.9, default_y=-660.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=284.38, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='26', width=305.07):
            with Note(default_x=12.12, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=134.2, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=180.73, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=202.21, default_y=-675.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=225.47, default_y=-680.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=246.95, default_y=-675.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=268.43, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=314.96, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='28', width=250.42):
            with Note(default_x=15.8, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.58, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=87.5, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=228.11):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='30', width=237.76):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=40.05, default_y=-680.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=68.92, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=86.37, default_y=-690.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=115.24, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=132.7, default_y=-680.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=160.63, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=195.54, default_y=-695.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.83, default_y=-700.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='32', width=280.06):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='33', width=231.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=239.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=318.45):
            with Note(default_x=16.16, default_y=-660.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.28, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='37', width=318.45):
            with Note(default_x=16.16, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.28, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=100.08, default_y=-692.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=150.66, default_y=-702.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=251.81, default_y=-692.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=302.39, default_y=-677.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=352.97, default_y=-667.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='39', width=342.73):
            with Note(default_x=15.8, default_y=-667.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=178.46, default_y=-692.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=232.68, default_y=-677.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=286.9, default_y=-667.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='40', width=329.62):
            with Note(default_x=15.8, default_y=-667.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.84, default_y=-702.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.85, default_y=-697.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.87, default_y=-692.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=171.91, default_y=-677.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=223.94, default_y=-677.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.96, default_y=-672.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.98, default_y=-677.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.0, default_y=-682.92, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=153.53, default_y=-675.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.55, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.57, default_y=-665.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=303.59, default_y=-660.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=483.65, default_y=-670.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=583.68, default_y=-675.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-685.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P9'):
        with Measure(number='1', width=255.05):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('C')
                    Line(3)
            with Note(default_x=120.77, default_y=-765.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=171.03, default_y=-765.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.42, default_y=-765.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=315.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=387.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=149.49):
            with Note(default_x=14.0, default_y=-745.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=64.71, default_y=-745.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=90.35, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='6', width=120.23):
            with Note(default_x=14.36, default_y=-755.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
            with Note(default_x=66.32, default_y=-755.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='7', width=352.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=378.03):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=124.36):
            with Note(default_x=14.0, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=53.24, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=78.15, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=126.16):
            with Note(default_x=15.8, default_y=-745.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=55.04, default_y=-745.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=79.95, default_y=-745.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=356.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=318.27):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=110.92, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=152.02, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=244.48, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=-745.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=100.34, default_y=-745.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=128.15, default_y=-765.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='17', width=247.17):
            with Note(default_x=18.28, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=132.1, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=160.47, default_y=-755.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=188.83, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=217.2, default_y=-765.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='18', width=219.25):
            with Note(default_x=18.76, default_y=-770.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=123.61, default_y=-790.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=165.4, default_y=-755.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=-740.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=120.89, default_y=-735.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.89, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='21', width=249.58):
            with Note(default_x=15.8, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.8, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='22', width=227.88):
            with Note(default_x=12.12, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=40.95, default_y=-770.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=245.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=157.99, default_y=-770.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=212.47, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=266.94, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=321.42, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=375.89, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='25', width=340.45):
            with Note(default_x=12.0, default_y=-770.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.48, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=120.95, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=175.43, default_y=-735.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=229.9, default_y=-735.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=284.38, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='26', width=305.07):
            with Note(default_x=12.12, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=134.2, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=180.73, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=225.47, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=246.95, default_y=-765.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=268.43, default_y=-770.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=291.7, default_y=-765.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.96, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.44, default_y=-755.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=250.42):
            with Note(default_x=15.8, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.58, default_y=-755.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=87.5, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=228.11):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='30', width=237.76):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=40.05, default_y=-770.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=68.92, default_y=-775.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=86.37, default_y=-770.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=132.7, default_y=-755.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=160.63, default_y=-770.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=195.54, default_y=-770.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.83, default_y=-780.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='32', width=280.06):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='33', width=231.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=239.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=318.45):
            with Note(default_x=16.16, default_y=-735.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.28, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='37', width=318.45):
            with Note(default_x=16.16, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.28, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=100.08, default_y=-767.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=150.66, default_y=-777.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=251.81, default_y=-777.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=302.39, default_y=-757.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=352.97, default_y=-742.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='39', width=342.73):
            with Note(default_x=15.8, default_y=-742.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=178.46, default_y=-777.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=232.68, default_y=-757.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=286.9, default_y=-742.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='40', width=329.62):
            with Note(default_x=15.8, default_y=-767.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.82, default_y=-762.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.84, default_y=-767.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.85, default_y=-772.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.87, default_y=-777.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=171.91, default_y=-792.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=223.94, default_y=-757.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=275.98, default_y=-757.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=203.55, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=303.59, default_y=-770.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=-770.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=483.65, default_y=-750.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=583.68, default_y=-755.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-760.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P10'):
        with Measure(number='1', width=255.05):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=120.77, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=171.03, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.42, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=315.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=387.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
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
            with Note(default_x=136.12, default_y=-890.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=170.62, default_y=-885.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=205.13, default_y=-880.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
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
            with Note(default_x=232.73, default_y=-875.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=260.34, default_y=-870.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=287.94, default_y=-865.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=315.54, default_y=-875.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=343.15, default_y=-870.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=370.75, default_y=-865.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=398.35, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=425.96, default_y=-855.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='5', width=149.49):
            with Note(default_x=14.0, default_y=-850.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=64.71, default_y=-850.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=90.35, default_y=-850.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='6', width=120.23):
            with Note(default_x=14.36, default_y=-870.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=66.32, default_y=-870.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='7', width=352.61):
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
            with Note(default_x=40.16, default_y=-890.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=68.2, default_y=-885.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=96.23, default_y=-880.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
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
            with Note(default_x=124.27, default_y=-875.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=152.31, default_y=-870.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=180.35, default_y=-865.0, dynamics=71.11):
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
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=236.43, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=264.46, default_y=-855.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=292.5, default_y=-850.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=322.97, default_y=-845.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(5)
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
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.83, default_y=-870.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=127.63, default_y=-875.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=145.01, default_y=-870.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=162.38, default_y=-875.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.76, default_y=-870.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=196.77, default_y=-875.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='9', width=378.03):
            with Note(default_x=12.36, default_y=-875.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=68.88, default_y=-880.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=97.15, default_y=-885.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=125.41, default_y=-890.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=153.67, default_y=-895.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=181.93, default_y=-890.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
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
            with Note(default_x=210.19, default_y=-880.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=238.45, default_y=-875.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=266.72, default_y=-870.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=307.44, default_y=-865.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=335.71, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
        with Measure(number='10', width=124.36):
            with Note(default_x=14.0, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=53.24, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=78.15, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=126.16):
            with Note(default_x=15.8, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=55.04, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=79.95, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
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
            with Note(default_x=125.33, default_y=-850.0, dynamics=71.11):
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
            with Note(default_x=150.01, default_y=-855.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=174.69, default_y=-850.0, dynamics=71.11):
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
            with Note(default_x=199.36, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=224.04, default_y=-865.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=248.72, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
            with Note(default_x=273.4, default_y=-870.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=300.06, default_y=-875.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=324.74, default_y=-870.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=349.42, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=376.08, default_y=-850.0, dynamics=71.11):
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
        with Measure(number='13', width=356.86):
            with Note(default_x=12.36, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=270.59, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=298.81, default_y=-850.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=327.04, default_y=-855.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='14', width=318.27):
            with Note(default_x=12.0, default_y=-850.0, dynamics=71.11):
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
            with Note(default_x=37.13, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=63.8, default_y=-865.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=88.93, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
            with Note(default_x=114.07, default_y=-855.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=139.2, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
            with Note(default_x=164.33, default_y=-865.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=189.47, default_y=-870.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=216.13, default_y=-875.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=241.27, default_y=-870.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=266.4, default_y=-885.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=291.53, default_y=-870.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=110.92, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=152.02, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=244.48, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=100.34, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=128.15, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='17', width=247.17):
            with Note(default_x=18.28, default_y=-865.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=131.74, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='18', width=219.25):
            with Note(default_x=19.12, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=45.24, default_y=-865.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=71.36, default_y=-870.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=97.49, default_y=-865.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=123.25, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=-865.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='21', width=249.58):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='22', width=227.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='23', width=245.36):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=42.25, default_y=-850.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=65.51, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=88.78, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.61, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=126.44, default_y=-850.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=164.1, default_y=-850.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=182.93, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.77, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.6, default_y=-865.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=185.23, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=212.47, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=340.45):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='26', width=305.07):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=134.2, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=157.47, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.73, default_y=-850.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=202.21, default_y=-845.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=225.47, default_y=-840.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=268.43, default_y=-840.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=291.7, default_y=-845.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.96, default_y=-850.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.44, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=250.42):
            with Note(default_x=15.8, default_y=-850.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.58, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=87.5, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=228.11):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=43.78, default_y=-870.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=70.44, default_y=-865.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=87.93, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=105.42, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=122.9, default_y=-850.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=150.88, default_y=-850.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.37, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.85, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.34, default_y=-865.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='30', width=237.76):
            with Note(default_x=12.12, default_y=-870.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=130.22, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=156.88, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=175.87, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=194.86, default_y=-850.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=214.33, default_y=-845.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=244.71, default_y=-850.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=282.7, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=280.06):
            with Note(default_x=12.12, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.43, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=91.48, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='33', width=231.12):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=44.87, default_y=-875.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=62.81, default_y=-870.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=80.76, default_y=-865.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=98.7, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=116.64, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=152.53, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=170.47, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.41, default_y=-865.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.36, default_y=-870.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='34', width=239.86):
            with Note(default_x=15.8, default_y=-865.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-865.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
        with Measure(number='36', width=318.45):
            with Note(default_x=15.8, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='37', width=318.45):
            with Note(default_x=15.8, default_y=-860.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.72, default_y=-867.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='39', width=342.73):
            with Note(default_x=15.44, default_y=-867.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=232.68, default_y=-867.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=259.79, default_y=-872.92, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.9, default_y=-867.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.02, default_y=-872.92, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='40', width=329.62):
            with Note(default_x=15.8, default_y=-867.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.84, default_y=-882.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=119.87, default_y=-867.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.89, default_y=-862.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=171.91, default_y=-857.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=223.94, default_y=-857.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.96, default_y=-862.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.98, default_y=-867.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.0, default_y=-872.92, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=153.53, default_y=-865.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.55, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.57, default_y=-855.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=303.59, default_y=-850.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=483.65, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=583.68, default_y=-865.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-860.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P11'):
        with Measure(number='1', width=255.05):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=120.77, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=171.03, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.42, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=315.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=387.37):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
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
            with Note(default_x=227.69, default_y=-1000.0, dynamics=71.11):
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
                Beam('begin', number=1)
            with Note(default_x=263.62, default_y=-995.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=299.54, default_y=-990.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=328.29, default_y=-985.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=357.03, default_y=-980.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=108.52, default_y=-975.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=170.62, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=205.13, default_y=-965.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=232.73, default_y=-960.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=260.34, default_y=-955.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
            with Note(default_x=287.94, default_y=-960.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=315.54, default_y=-950.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=343.15, default_y=-955.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
            with Note(default_x=370.75, default_y=-960.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=398.35, default_y=-965.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=425.96, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
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
        with Measure(number='5', width=149.49):
            with Note(default_x=14.0, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=64.71, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=90.35, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='6', width=120.23):
            with Note(default_x=14.36, default_y=-975.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
            with Note(default_x=66.32, default_y=-975.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=352.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
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
            with Note(default_x=127.63, default_y=-990.0, dynamics=71.11):
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
                Beam('begin', number=1)
            with Note(default_x=162.38, default_y=-985.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
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
            with Note(default_x=197.13, default_y=-980.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=224.94, default_y=-975.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=252.74, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=280.54, default_y=-965.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=308.34, default_y=-980.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=336.14, default_y=-975.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=363.94, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=391.74, default_y=-965.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=419.54, default_y=-960.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='9', width=378.03):
            with Note(default_x=12.0, default_y=-980.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=181.93, default_y=-980.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=210.19, default_y=-975.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=238.45, default_y=-980.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=266.72, default_y=-985.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
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
            with Note(default_x=307.44, default_y=-990.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=335.71, default_y=-995.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='10', width=124.36):
            with Note(default_x=14.0, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=53.24, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=78.15, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=126.16):
            with Note(default_x=15.8, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=55.04, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=79.95, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
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
            with Note(default_x=199.36, default_y=-945.0, dynamics=71.11):
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
            with Note(default_x=224.04, default_y=-950.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=248.72, default_y=-945.0, dynamics=71.11):
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
            with Note(default_x=273.4, default_y=-955.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=300.06, default_y=-960.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=324.74, default_y=-955.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
            with Note(default_x=349.42, default_y=-965.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=376.08, default_y=-970.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='13', width=356.86):
            with Note(default_x=12.36, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=270.59, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=298.81, default_y=-980.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=327.04, default_y=-970.0, dynamics=71.11):
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
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='14', width=318.27):
            with Note(default_x=12.0, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=88.93, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=114.07, default_y=-985.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=139.2, default_y=-980.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=164.33, default_y=-975.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=189.47, default_y=-965.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=216.13, default_y=-960.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=241.27, default_y=-955.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
            with Note(default_x=266.4, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=291.53, default_y=-965.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=110.92, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=152.02, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=244.48, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=100.34, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=128.15, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='17', width=247.17):
            with Note(default_x=15.32, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='18', width=219.25):
            with Note(default_x=18.76, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=123.61, default_y=-975.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=165.4, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=191.53, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=-985.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='21', width=249.58):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='22', width=227.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='23', width=245.36):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=42.25, default_y=-990.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=65.51, default_y=-985.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=88.78, default_y=-980.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.61, default_y=-975.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=126.44, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=164.1, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=182.93, default_y=-975.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.77, default_y=-980.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.6, default_y=-985.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-980.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=185.23, default_y=-980.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=212.47, default_y=-980.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=340.45):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='26', width=305.07):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=134.2, default_y=-945.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=157.47, default_y=-950.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.73, default_y=-955.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=202.21, default_y=-950.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=225.47, default_y=-945.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=268.43, default_y=-945.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=291.7, default_y=-950.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.96, default_y=-955.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.44, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=250.42):
            with Note(default_x=15.8, default_y=-955.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.58, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=87.5, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=228.11):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=43.78, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=70.44, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=87.93, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=105.42, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=122.9, default_y=-955.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=150.88, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=185.85, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='30', width=237.76):
            with Note(default_x=12.12, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=130.22, default_y=-985.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=156.88, default_y=-980.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=175.87, default_y=-975.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=194.86, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=214.33, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=244.71, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=263.7, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.7, default_y=-975.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=301.69, default_y=-980.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='32', width=280.06):
            with Note(default_x=12.12, default_y=-975.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=69.43, default_y=-980.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=91.48, default_y=-985.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='33', width=231.12):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='34', width=239.86):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=45.93, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=64.53, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=83.14, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=101.75, default_y=-955.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=121.21, default_y=-950.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=158.42, default_y=-950.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.89, default_y=-955.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.49, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.1, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='36', width=318.45):
            with Note(default_x=15.8, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='37', width=318.45):
            with Note(default_x=15.8, default_y=-970.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.72, default_y=-977.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='39', width=342.73):
            with Note(default_x=15.44, default_y=-977.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=232.68, default_y=-977.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=259.79, default_y=-982.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.9, default_y=-977.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.02, default_y=-982.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='40', width=329.62):
            with Note(default_x=15.8, default_y=-987.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.82, default_y=-992.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.84, default_y=-987.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.85, default_y=-982.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.87, default_y=-977.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=171.91, default_y=-962.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=223.94, default_y=-962.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=275.98, default_y=-977.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=203.55, default_y=-955.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=253.57, default_y=-960.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=303.59, default_y=-955.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=-965.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=483.65, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-970.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P12'):
        with Measure(number='1', width=255.05):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(55.55)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=120.77, default_y=-1065.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=171.03, default_y=-1065.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.42, default_y=-1065.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=315.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=387.37):
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
            with Note(default_x=40.86, default_y=-1105.55, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=76.79, default_y=-1100.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
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
            with Note(default_x=112.72, default_y=-1095.55, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=141.46, default_y=-1090.55, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=170.2, default_y=-1085.55, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=198.95, default_y=-1080.55, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
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
            with Note(default_x=227.69, default_y=-1070.55, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=263.62, default_y=-1065.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=299.54, default_y=-1060.55, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=328.29, default_y=-1055.55, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=357.03, default_y=-1050.55, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=108.52, default_y=-1055.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=136.12, default_y=-1060.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=153.37, default_y=-1055.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=170.62, default_y=-1060.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.88, default_y=-1055.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=205.13, default_y=-1060.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=287.94, default_y=-1060.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=315.54, default_y=-1055.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=343.15, default_y=-1060.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=370.75, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=398.35, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=425.96, default_y=-1075.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='5', width=149.49):
            with Note(default_x=14.0, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=64.71, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=90.35, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='6', width=120.23):
            with Note(default_x=14.36, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=66.32, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=352.61):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
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
            with Note(default_x=208.39, default_y=-1100.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=236.43, default_y=-1095.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=264.46, default_y=-1090.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=292.5, default_y=-1085.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=322.97, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
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
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.83, default_y=-1075.0, dynamics=71.11):
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
            with Note(default_x=162.38, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=197.13, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=224.94, default_y=-1060.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=252.74, default_y=-1055.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=280.17, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='9', width=378.03):
            with Note(default_x=12.36, default_y=-1085.0, dynamics=71.11):
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
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=68.88, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
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
            with Note(default_x=97.15, default_y=-1075.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=125.41, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=153.67, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=181.93, default_y=-1070.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=210.19, default_y=-1060.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=238.45, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=266.72, default_y=-1070.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=307.44, default_y=-1075.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=335.71, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
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
        with Measure(number='10', width=124.36):
            with Note(default_x=14.0, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=53.24, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=78.15, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='11', width=126.16):
            with Note(default_x=15.8, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=55.04, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=79.95, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
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
            with Note(default_x=273.4, default_y=-1075.0, dynamics=71.11):
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
                Beam('begin', number=1)
            with Note(default_x=300.06, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
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
            with Note(default_x=324.74, default_y=-1075.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=349.42, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=376.08, default_y=-1090.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='13', width=356.86):
            with Note(default_x=12.72, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=40.95, default_y=-1095.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=73.01, default_y=-1100.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(3)
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
            with Note(default_x=101.24, default_y=-1095.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=129.46, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=157.69, default_y=-1075.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=185.55, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='14', width=318.27):
            with Note(default_x=12.0, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=88.93, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=114.07, default_y=-1060.0, dynamics=71.11):
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
            with Note(default_x=139.2, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=164.33, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=189.47, default_y=-1075.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=216.13, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
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
            with Note(default_x=241.27, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=266.4, default_y=-1090.0, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=291.53, default_y=-1095.0, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=110.92, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=152.02, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=244.48, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=100.34, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=128.15, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='17', width=247.17):
            with Note(default_x=18.28, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=131.74, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='18', width=219.25):
            with Note(default_x=18.76, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=123.61, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=165.4, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='21', width=249.58):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='22', width=227.88):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=40.95, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=58.97, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=76.99, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=95.0, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=113.02, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=149.06, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=167.08, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.1, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.12, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=245.36):
            with Note(default_x=12.12, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=65.51, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=88.78, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='25', width=340.45):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='26', width=305.07):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=52.31, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=77.42, default_y=-1090.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=102.54, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=127.66, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=152.77, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=203.01, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=228.12, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.24, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.36, default_y=-1090.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.83, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=157.47, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=180.73, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=225.47, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=246.95, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=268.43, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=291.7, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=314.96, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='28', width=250.42):
            with Note(default_x=15.8, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=67.58, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=87.5, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=228.11):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=43.78, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=70.44, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=87.93, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=122.9, default_y=-1095.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=150.88, default_y=-1090.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=185.85, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='30', width=237.76):
            with Note(default_x=12.12, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=130.22, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=156.88, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=175.87, default_y=-1060.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=214.33, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=244.71, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=282.7, default_y=-1060.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=280.06):
            with Note(default_x=12.12, default_y=-1060.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.43, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=91.48, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='33', width=231.12):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=44.87, default_y=-1090.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=62.81, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=80.76, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=98.7, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=116.64, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=152.53, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=170.47, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.41, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.36, default_y=-1085.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='34', width=239.86):
            with Note(default_x=15.8, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='36', width=318.45):
            with Note(default_x=15.8, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='37', width=318.45):
            with Note(default_x=15.8, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.72, default_y=-1082.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='39', width=342.73):
            with Note(default_x=15.44, default_y=-1082.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=232.68, default_y=-1082.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=259.79, default_y=-1087.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=286.9, default_y=-1072.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='40', width=329.62):
            with Note(default_x=15.8, default_y=-1092.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.82, default_y=-1087.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.84, default_y=-1092.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.85, default_y=-1097.92, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.87, default_y=-1092.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.89, default_y=-1077.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.91, default_y=-1082.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.93, default_y=-1077.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=223.94, default_y=-1072.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.96, default_y=-1067.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.98, default_y=-1072.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.0, default_y=-1077.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=203.55, default_y=-1060.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=303.59, default_y=-1065.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=-1070.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=433.63, default_y=-1075.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=483.65, default_y=-1080.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-1075.0, dynamics=71.11):
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
    with Part(id='P13'):
        with Measure(number='1', width=255.05):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note(default_x=120.77, default_y=-1140.55, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=171.03, default_y=-1140.55, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.42, default_y=-1140.55, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=315.87):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
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
            with Note(default_x=187.43, default_y=-1180.55, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=212.47, default_y=-1175.55, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
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
            with Note(default_x=237.52, default_y=-1170.55, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
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
            with Note(default_x=264.18, default_y=-1165.55, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=289.23, default_y=-1160.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
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
        with Measure(number='3', width=387.37):
            with Note(default_x=12.12, default_y=-1155.55, dynamics=71.11):
                with Pitch():
                    Step('C')
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
            with Note(default_x=76.79, default_y=-1150.55, dynamics=71.11):
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
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=112.72, default_y=-1145.55, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=141.46, default_y=-1140.55, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=170.2, default_y=-1135.55, dynamics=71.11):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=198.95, default_y=-1160.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=227.69, default_y=-1165.55, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=245.65, default_y=-1160.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=263.62, default_y=-1165.55, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=281.58, default_y=-1160.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=299.54, default_y=-1165.55, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=108.52, default_y=-1165.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=136.12, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=170.62, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
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
            with Note(default_x=205.13, default_y=-1165.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=232.73, default_y=-1170.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=260.34, default_y=-1175.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
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
            with Note(default_x=287.94, default_y=-1140.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=370.75, default_y=-1140.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=398.35, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=425.96, default_y=-1150.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
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
        with Measure(number='5', width=149.49):
            with Note(default_x=14.0, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=64.71, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=90.35, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='6', width=120.23):
            with Note(default_x=14.36, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=66.32, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='7', width=352.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.16)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
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
            with Note(default_x=308.34, default_y=-1180.16, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=336.14, default_y=-1175.16, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
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
            with Note(default_x=363.94, default_y=-1170.16, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
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
            with Note(default_x=391.74, default_y=-1165.16, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=419.54, default_y=-1160.16, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
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
        with Measure(number='9', width=378.03):
            with Note(default_x=12.36, default_y=-1155.16, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
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
            with Note(default_x=40.62, default_y=-1135.16, dynamics=71.11):
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
                Beam('continue', number=1)
            with Note(default_x=68.88, default_y=-1140.16, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
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
            with Note(default_x=97.15, default_y=-1145.16, dynamics=71.11):
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
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=125.41, default_y=-1150.16, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=153.67, default_y=-1155.16, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Tuplet(type='stop')
            with Note(default_x=181.93, default_y=-1155.16, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=266.72, default_y=-1155.16, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=291.78, default_y=-1160.16, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=351.37, default_y=-1165.16, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='10', width=124.36):
            with Note(default_x=14.0, default_y=-1170.16, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=53.24, default_y=-1170.16, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=78.15, default_y=-1170.16, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='11', width=126.16):
            with Note(default_x=15.8, default_y=-1155.16, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=55.04, default_y=-1155.16, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=79.95, default_y=-1155.16, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
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
            with Note(default_x=349.42, default_y=-1135.0, dynamics=71.11):
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
                Beam('begin', number=1)
            with Note(default_x=376.08, default_y=-1140.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
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
        with Measure(number='13', width=356.86):
            with Note(default_x=12.72, default_y=-1135.0, dynamics=71.11):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=40.95, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=73.01, default_y=-1150.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
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
            with Note(default_x=101.24, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=129.46, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=157.69, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(3)
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
            with Note(default_x=185.91, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
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
            with Note(default_x=214.14, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=242.36, default_y=-1150.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
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
            with Note(default_x=270.59, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='14', width=318.27):
            with Note(default_x=12.0, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=37.13, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=63.8, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(3)
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
            with Note(default_x=88.93, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=164.33, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=189.47, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=216.13, default_y=-1140.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
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
            with Note(default_x=241.27, default_y=-1135.0, dynamics=71.11):
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
            with Note(default_x=291.53, default_y=-1140.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
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
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=110.92, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=152.02, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=244.48, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=100.34, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=128.15, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='17', width=247.17):
            with Note(default_x=18.28, default_y=-1140.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=131.74, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='18', width=219.25):
            with Note(default_x=19.12, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=45.24, default_y=-1140.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=71.36, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=97.49, default_y=-1150.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=123.25, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=-1150.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='21', width=249.58):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='22', width=227.88):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=40.95, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=58.97, default_y=-1150.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=76.99, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=95.0, default_y=-1140.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=113.02, default_y=-1135.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=149.06, default_y=-1135.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=167.08, default_y=-1140.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.1, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.12, default_y=-1150.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=245.36):
            with Note(default_x=12.12, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=65.51, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=88.78, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='25', width=340.45):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='26', width=305.07):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=52.31, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=77.42, default_y=-1165.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=102.54, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=152.77, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.01, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=253.24, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.83, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=157.47, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=180.73, default_y=-1170.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=225.47, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=246.95, default_y=-1150.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=268.43, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=314.96, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='28', width=250.42):
            with Note(default_x=15.8, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.58, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=87.5, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=228.11):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=43.78, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=70.44, default_y=-1150.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=87.93, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=122.9, default_y=-1170.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=150.88, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=185.85, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='30', width=237.76):
            with Note(default_x=12.12, default_y=-1165.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=130.22, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=156.88, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=175.87, default_y=-1165.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=214.33, default_y=-1175.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=244.71, default_y=-1170.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=282.7, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='32', width=280.06):
            with Note(default_x=12.12, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.43, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=91.48, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='33', width=231.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=239.86):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=45.93, default_y=-1150.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=64.53, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=83.14, default_y=-1140.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=101.75, default_y=-1135.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=121.21, default_y=-1130.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=158.42, default_y=-1130.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.89, default_y=-1135.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.49, default_y=-1140.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.1, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.88, default_y=-1150.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=207.88, default_y=-1150.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=236.77, default_y=-1155.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=265.66, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.55, default_y=-1165.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=323.43, default_y=-1170.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=352.32, default_y=-1175.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=381.21, default_y=-1165.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=410.1, default_y=-1170.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='36', width=318.45):
            with Note(default_x=15.8, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='37', width=318.45):
            with Note(default_x=15.8, default_y=-1160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.72, default_y=-1167.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='39', width=342.73):
            with Note(default_x=15.44, default_y=-1167.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=232.68, default_y=-1167.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=286.9, default_y=-1167.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='40', width=329.62):
            with Note(default_x=15.8, default_y=-1142.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.82, default_y=-1137.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.84, default_y=-1142.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.85, default_y=-1147.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.87, default_y=-1152.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.89, default_y=-1157.92, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=171.91, default_y=-1152.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=223.94, default_y=-1152.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=249.96, default_y=-1157.92, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.98, default_y=-1152.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.0, default_y=-1147.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=203.55, default_y=-1135.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=303.59, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=-1145.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=483.65, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-1160.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P14'):
        with Measure(number='1', width=255.05):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=120.77, default_y=-1230.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=171.03, default_y=-1230.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.42, default_y=-1230.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=315.87):
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
            with Note(default_x=37.16, default_y=-1265.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=62.21, default_y=-1260.55, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
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
            with Note(default_x=87.25, default_y=-1255.55, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
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
            with Note(default_x=112.3, default_y=-1250.55, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=137.34, default_y=-1245.55, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
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
            with Note(default_x=162.38, default_y=-1240.55, dynamics=71.11):
                with Pitch():
                    Step('G')
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
            with Note(default_x=212.47, default_y=-1235.55, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=237.52, default_y=-1230.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
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
            with Note(default_x=264.18, default_y=-1225.55, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=289.23, default_y=-1220.55, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
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
        with Measure(number='3', width=387.37):
            with Note(default_x=12.12, default_y=-1245.55, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=40.86, default_y=-1250.55, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=58.83, default_y=-1245.55, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=76.79, default_y=-1250.55, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.75, default_y=-1245.55, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=112.36, default_y=-1250.55, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=108.52, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
            with Note(default_x=170.62, default_y=-1255.0, dynamics=71.11):
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
            with Note(default_x=205.13, default_y=-1260.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
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
            with Note(default_x=232.73, default_y=-1265.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=260.34, default_y=-1270.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(2)
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
            with Note(default_x=287.94, default_y=-1265.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
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
            with Note(default_x=315.54, default_y=-1255.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=343.15, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
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
            with Note(default_x=370.75, default_y=-1245.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
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
            with Note(default_x=398.35, default_y=-1240.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=425.96, default_y=-1235.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
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
        with Measure(number='5', width=149.49):
            with Note(default_x=14.0, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
            with Note(default_x=64.71, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=90.35, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='6', width=120.23):
            with Note(default_x=14.36, default_y=-1245.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=66.32, default_y=-1245.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='7', width=352.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(58.99)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=378.03):
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
            with Note(default_x=40.62, default_y=-1264.15, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=68.88, default_y=-1259.15, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
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
            with Note(default_x=97.15, default_y=-1254.15, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
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
            with Note(default_x=125.41, default_y=-1249.15, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=153.67, default_y=-1244.15, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
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
            with Note(default_x=181.93, default_y=-1239.15, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
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
            with Note(default_x=210.19, default_y=-1249.15, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=238.45, default_y=-1244.15, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
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
            with Note(default_x=266.72, default_y=-1239.15, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
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
            with Note(default_x=307.44, default_y=-1234.15, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=335.71, default_y=-1229.15, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
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
        with Measure(number='10', width=124.36):
            with Note(default_x=14.0, default_y=-1234.15, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
            with Note(default_x=53.24, default_y=-1234.15, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=78.15, default_y=-1234.15, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=126.16):
            with Note(default_x=15.8, default_y=-1229.15, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=55.04, default_y=-1229.15, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=79.95, default_y=-1229.15, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(57.65)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=356.86):
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
            with Note(default_x=40.95, default_y=-1242.65, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.01, default_y=-1247.65, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
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
            with Note(default_x=101.24, default_y=-1242.65, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
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
            with Note(default_x=129.46, default_y=-1252.65, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=157.69, default_y=-1257.65, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
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
            with Note(default_x=185.91, default_y=-1252.65, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
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
            with Note(default_x=214.14, default_y=-1262.65, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=242.36, default_y=-1267.65, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(2)
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
            with Note(default_x=270.59, default_y=-1262.65, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
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
            with Note(default_x=298.81, default_y=-1252.65, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=327.04, default_y=-1257.65, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
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
        with Measure(number='14', width=318.27):
            with Note(default_x=12.0, default_y=-1252.65, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
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
            with Note(default_x=37.13, default_y=-1242.65, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=63.8, default_y=-1247.65, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
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
            with Note(default_x=88.93, default_y=-1242.65, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
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
            with Note(default_x=114.07, default_y=-1237.65, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=139.2, default_y=-1242.65, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
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
            with Note(default_x=164.33, default_y=-1247.65, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
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
            with Note(default_x=189.47, default_y=-1252.65, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=216.13, default_y=-1257.65, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
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
            with Note(default_x=241.27, default_y=-1262.65, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
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
            with Note(default_x=266.4, default_y=-1267.65, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=291.53, default_y=-1272.65, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
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
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=110.92, default_y=-1275.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=152.02, default_y=-1275.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=-1275.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=-1240.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=244.48, default_y=-1240.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=-1235.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=100.34, default_y=-1235.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=128.15, default_y=-1235.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='17', width=247.17):
            with Note(default_x=18.28, default_y=-1235.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=131.74, default_y=-1240.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='18', width=219.25):
            with Note(default_x=15.8, default_y=-1225.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('whole')
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=-1230.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='21', width=249.58):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='22', width=227.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='23', width=245.36):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=42.25, default_y=-1215.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=65.51, default_y=-1220.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=88.78, default_y=-1225.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=126.44, default_y=-1230.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.27, default_y=-1235.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=164.1, default_y=-1230.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=201.77, default_y=-1265.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=185.23, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=212.47, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=340.45):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='26', width=305.07):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=52.31, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=77.42, default_y=-1245.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=102.54, default_y=-1240.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=127.66, default_y=-1235.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=152.77, default_y=-1230.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.01, default_y=-1230.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=228.12, default_y=-1235.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.24, default_y=-1240.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.36, default_y=-1245.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.83, default_y=-1240.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=157.47, default_y=-1240.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=180.73, default_y=-1240.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=225.47, default_y=-1240.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=246.95, default_y=-1235.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=268.43, default_y=-1230.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=314.96, default_y=-1265.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='28', width=250.42):
            with Note(default_x=15.8, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.58, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=87.5, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=228.11):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=43.78, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=70.44, default_y=-1245.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=87.93, default_y=-1240.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.9, default_y=-1225.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=150.88, default_y=-1230.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=185.85, default_y=-1240.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='30', width=237.76):
            with Note(default_x=12.12, default_y=-1235.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=130.22, default_y=-1235.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=156.88, default_y=-1240.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=175.87, default_y=-1245.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=214.33, default_y=-1245.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=244.71, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=282.7, default_y=-1260.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=280.06):
            with Note(default_x=12.12, default_y=-1245.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.43, default_y=-1245.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=91.48, default_y=-1245.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='33', width=231.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=239.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=150.1, default_y=-1240.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=178.99, default_y=-1235.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=207.88, default_y=-1230.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=236.77, default_y=-1225.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=265.66, default_y=-1220.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.55, default_y=-1225.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=323.43, default_y=-1215.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=352.32, default_y=-1220.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=381.21, default_y=-1225.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=410.1, default_y=-1230.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='36', width=318.45):
            with Note(default_x=15.8, default_y=-1215.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='37', width=318.45):
            with Note(default_x=15.8, default_y=-1215.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=100.08, default_y=-1222.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=150.66, default_y=-1227.92, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=175.95, default_y=-1232.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=201.24, default_y=-1237.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=226.52, default_y=-1242.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.81, default_y=-1247.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.1, default_y=-1242.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=302.39, default_y=-1237.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=327.68, default_y=-1232.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=352.97, default_y=-1237.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=378.26, default_y=-1232.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='39', width=342.73):
            with Note(default_x=15.8, default_y=-1237.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.91, default_y=-1222.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.02, default_y=-1227.92, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.13, default_y=-1232.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=124.24, default_y=-1237.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=151.35, default_y=-1242.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.46, default_y=-1247.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.57, default_y=-1242.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=232.68, default_y=-1237.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=259.79, default_y=-1232.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.9, default_y=-1242.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.02, default_y=-1237.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='40', width=329.62):
            with Note(default_x=15.8, default_y=-1232.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.84, default_y=-1237.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.85, default_y=-1242.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.87, default_y=-1247.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.89, default_y=-1252.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.91, default_y=-1257.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.93, default_y=-1252.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=223.94, default_y=-1247.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.96, default_y=-1242.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=275.98, default_y=-1237.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=203.55, default_y=-1225.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=303.59, default_y=-1240.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=-1235.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=483.65, default_y=-1230.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-1250.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P15'):
        with Measure(number='1', width=255.05):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=120.77, default_y=-1360.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=171.03, default_y=-1360.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=196.42, default_y=-1360.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='2', width=315.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=387.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=149.49):
            with Note(default_x=14.0, default_y=-1345.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
            with Note(default_x=64.71, default_y=-1345.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=90.35, default_y=-1345.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='6', width=120.23):
            with Note(default_x=14.36, default_y=-1340.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=66.32, default_y=-1375.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=352.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=378.03):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=124.36):
            with Note(default_x=14.0, default_y=-1364.15, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
            with Note(default_x=53.24, default_y=-1364.15, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=78.15, default_y=-1364.15, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='11', width=126.16):
            with Note(default_x=15.8, default_y=-1359.15, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=55.04, default_y=-1359.15, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=79.95, default_y=-1359.15, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=356.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=318.27):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=110.92, default_y=-1370.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=152.02, default_y=-1370.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=-1370.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=-1370.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=244.48, default_y=-1370.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=-1365.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=100.34, default_y=-1365.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=128.15, default_y=-1365.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=247.17):
            with Note(default_x=18.28, default_y=-1365.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=131.74, default_y=-1370.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='18', width=219.25):
            with Note(default_x=15.8, default_y=-1355.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('whole')
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=-1360.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=120.89, default_y=-1310.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.89, default_y=-1345.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='21', width=249.58):
            with Note(default_x=15.8, default_y=-1320.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.8, default_y=-1355.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='22', width=227.88):
            with Note(default_x=12.12, default_y=-1335.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=40.95, default_y=-1370.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=113.02, default_y=-1335.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=131.04, default_y=-1330.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=149.06, default_y=-1325.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=185.1, default_y=-1360.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='23', width=245.36):
            with Note(default_x=12.12, default_y=-1345.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=42.25, default_y=-1310.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=65.51, default_y=-1315.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=88.78, default_y=-1320.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=126.44, default_y=-1325.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.27, default_y=-1330.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=164.1, default_y=-1325.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=201.77, default_y=-1360.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-1345.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=157.99, default_y=-1380.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=340.45):
            with Note(default_x=12.0, default_y=-1355.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=66.48, default_y=-1390.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='26', width=305.07):
            with Note(default_x=12.12, default_y=-1335.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.31, default_y=-1370.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=152.77, default_y=-1335.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.89, default_y=-1330.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=203.01, default_y=-1325.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=253.24, default_y=-1360.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.83, default_y=-1345.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=134.2, default_y=-1310.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=157.47, default_y=-1315.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.73, default_y=-1320.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=225.47, default_y=-1325.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=246.95, default_y=-1330.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=268.43, default_y=-1325.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=314.96, default_y=-1360.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='28', width=250.42):
            with Note(default_x=15.8, default_y=-1345.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=47.67, default_y=-1380.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=130.68, default_y=-1310.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=162.55, default_y=-1315.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=205.73, default_y=-1325.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='29', width=228.11):
            with Note(default_x=15.8, default_y=-1320.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=43.78, default_y=-1355.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=122.9, default_y=-1320.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=150.88, default_y=-1325.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=185.85, default_y=-1335.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='30', width=237.76):
            with Note(default_x=12.12, default_y=-1330.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=40.05, default_y=-1365.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=132.7, default_y=-1330.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=160.63, default_y=-1335.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=195.54, default_y=-1345.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.83, default_y=-1340.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=130.22, default_y=-1375.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=214.33, default_y=-1340.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=244.71, default_y=-1345.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=282.7, default_y=-1355.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=280.06):
            with Note(default_x=12.12, default_y=-1340.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=47.39, default_y=-1375.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=138.01, default_y=-1340.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=160.05, default_y=-1335.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=182.09, default_y=-1330.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=205.36, default_y=-1325.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=228.63, default_y=-1320.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='33', width=231.12):
            with Note(default_x=16.16, default_y=-1350.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=44.87, default_y=-1385.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=116.64, default_y=-1350.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=134.59, default_y=-1345.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=152.53, default_y=-1340.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=170.47, default_y=-1335.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=188.41, default_y=-1330.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='34', width=239.86):
            with Note(default_x=16.16, default_y=-1360.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=45.93, default_y=-1325.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=121.21, default_y=-1360.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.82, default_y=-1355.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=158.42, default_y=-1350.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.89, default_y=-1345.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=196.49, default_y=-1340.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.88, default_y=-1370.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=150.1, default_y=-1335.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=265.66, default_y=-1370.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=294.55, default_y=-1365.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=323.43, default_y=-1360.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=352.32, default_y=-1355.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=381.21, default_y=-1350.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='36', width=318.45):
            with Note(default_x=16.16, default_y=-1380.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=66.28, default_y=-1345.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='37', width=318.45):
            with Note(default_x=16.16, default_y=-1390.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=66.28, default_y=-1355.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=100.08, default_y=-1377.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.37, default_y=-1352.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.66, default_y=-1357.92, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.95, default_y=-1362.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=201.24, default_y=-1367.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=226.52, default_y=-1372.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.81, default_y=-1377.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.1, default_y=-1372.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=302.39, default_y=-1367.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=327.68, default_y=-1362.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=352.97, default_y=-1367.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=378.26, default_y=-1362.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='39', width=342.73):
            with Note(default_x=15.8, default_y=-1367.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.91, default_y=-1352.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.02, default_y=-1357.92, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.13, default_y=-1362.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=124.24, default_y=-1367.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=151.35, default_y=-1372.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.46, default_y=-1377.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.57, default_y=-1372.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=232.68, default_y=-1367.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=259.79, default_y=-1362.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.9, default_y=-1372.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.02, default_y=-1367.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='40', width=329.62):
            with Note(default_x=15.8, default_y=-1362.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=67.84, default_y=-1367.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.85, default_y=-1372.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.87, default_y=-1377.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.89, default_y=-1382.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.91, default_y=-1387.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.93, default_y=-1382.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=223.94, default_y=-1377.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.96, default_y=-1372.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=275.98, default_y=-1367.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-1380.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=203.55, default_y=-1355.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=303.59, default_y=-1370.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=-1365.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=483.65, default_y=-1360.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-1380.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P16'):
        with Measure(number='1', width=255.05):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=120.77, default_y=-1455.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=171.03, default_y=-1455.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=196.42, default_y=-1455.55, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='2', width=315.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=387.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=455.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=149.49):
            with Note(default_x=14.0, default_y=-1440.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
            with Note(default_x=64.71, default_y=-1440.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=90.35, default_y=-1440.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='6', width=120.23):
            with Note(default_x=14.36, default_y=-1435.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=66.32, default_y=-1470.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=352.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=448.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=378.03):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=124.36):
            with Note(default_x=14.0, default_y=-1459.15, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
            with Note(default_x=53.24, default_y=-1459.15, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=78.15, default_y=-1459.15, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='11', width=126.16):
            with Note(default_x=15.8, default_y=-1454.15, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=55.04, default_y=-1454.15, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=79.95, default_y=-1454.15, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='12', width=402.36):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=356.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=318.27):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=287.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=110.92, default_y=-1465.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=152.02, default_y=-1465.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=177.7, default_y=-1465.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=203.39, default_y=-1465.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=244.48, default_y=-1465.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=192.11):
            with Note(default_x=15.8, default_y=-1460.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=100.34, default_y=-1460.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=128.15, default_y=-1460.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=247.17):
            with Note(default_x=18.28, default_y=-1460.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=131.74, default_y=-1465.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='18', width=219.25):
            with Note(default_x=15.8, default_y=-1450.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('whole')
        with Measure(number='19', width=131.79):
            with Note(default_x=15.8, default_y=-1455.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=354.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=120.89, default_y=-1405.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.89, default_y=-1440.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='21', width=249.58):
            with Note(default_x=15.8, default_y=-1415.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.8, default_y=-1450.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='22', width=227.88):
            with Note(default_x=12.12, default_y=-1430.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=40.95, default_y=-1465.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=113.02, default_y=-1430.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=131.04, default_y=-1425.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=149.06, default_y=-1420.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=185.1, default_y=-1455.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='23', width=245.36):
            with Note(default_x=12.12, default_y=-1440.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=42.25, default_y=-1405.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=65.51, default_y=-1410.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=88.78, default_y=-1415.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=126.44, default_y=-1420.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.27, default_y=-1425.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=164.1, default_y=-1420.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=201.77, default_y=-1455.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='24', width=431.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-1440.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=157.99, default_y=-1475.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=340.45):
            with Note(default_x=12.0, default_y=-1450.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=66.48, default_y=-1485.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='26', width=305.07):
            with Note(default_x=12.12, default_y=-1430.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.31, default_y=-1465.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=152.77, default_y=-1430.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.89, default_y=-1425.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=203.01, default_y=-1420.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=253.24, default_y=-1455.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='27', width=361.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.83, default_y=-1440.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=134.2, default_y=-1405.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=157.47, default_y=-1410.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.73, default_y=-1415.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=225.47, default_y=-1420.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=246.95, default_y=-1425.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=268.43, default_y=-1420.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=314.96, default_y=-1455.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='28', width=250.42):
            with Note(default_x=15.8, default_y=-1440.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=47.67, default_y=-1475.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=130.68, default_y=-1405.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=162.55, default_y=-1410.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=205.73, default_y=-1420.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='29', width=228.11):
            with Note(default_x=15.8, default_y=-1415.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=43.78, default_y=-1450.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=122.9, default_y=-1415.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=150.88, default_y=-1420.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=185.85, default_y=-1430.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='30', width=237.76):
            with Note(default_x=12.12, default_y=-1425.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=40.05, default_y=-1460.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=132.7, default_y=-1425.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=160.63, default_y=-1430.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=195.54, default_y=-1440.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=326.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=99.83, default_y=-1435.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=130.22, default_y=-1470.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=214.33, default_y=-1435.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=244.71, default_y=-1440.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=282.7, default_y=-1450.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=280.06):
            with Note(default_x=12.12, default_y=-1435.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=47.39, default_y=-1470.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=138.01, default_y=-1435.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=160.05, default_y=-1430.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=182.09, default_y=-1425.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=205.36, default_y=-1420.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=228.63, default_y=-1415.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='33', width=231.12):
            with Note(default_x=16.16, default_y=-1445.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=44.87, default_y=-1480.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=116.64, default_y=-1445.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=134.59, default_y=-1440.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=152.53, default_y=-1435.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=170.47, default_y=-1430.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=188.41, default_y=-1425.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='34', width=239.86):
            with Note(default_x=16.16, default_y=-1455.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=45.93, default_y=-1420.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=121.21, default_y=-1455.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.82, default_y=-1450.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=158.42, default_y=-1445.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.89, default_y=-1440.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=196.49, default_y=-1435.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='35', width=440.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.88, default_y=-1465.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=150.1, default_y=-1430.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=265.66, default_y=-1465.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=294.55, default_y=-1460.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=323.43, default_y=-1455.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=352.32, default_y=-1450.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=381.21, default_y=-1445.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='36', width=318.45):
            with Note(default_x=16.16, default_y=-1475.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=66.28, default_y=-1440.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='37', width=318.45):
            with Note(default_x=16.16, default_y=-1485.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=66.28, default_y=-1450.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='38', width=405.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=100.08, default_y=-1472.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.37, default_y=-1447.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.66, default_y=-1452.92, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.95, default_y=-1457.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=201.24, default_y=-1462.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=226.52, default_y=-1467.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.81, default_y=-1472.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.1, default_y=-1467.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=302.39, default_y=-1462.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=327.68, default_y=-1457.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=352.97, default_y=-1462.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=378.26, default_y=-1457.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='39', width=342.73):
            with Note(default_x=15.8, default_y=-1462.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.91, default_y=-1447.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.02, default_y=-1452.92, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.13, default_y=-1457.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=124.24, default_y=-1462.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=151.35, default_y=-1467.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.46, default_y=-1472.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.57, default_y=-1467.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=232.68, default_y=-1462.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=259.79, default_y=-1457.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.9, default_y=-1467.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.02, default_y=-1462.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='40', width=329.62):
            with Note(default_x=15.8, default_y=-1457.92, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=67.84, default_y=-1462.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.85, default_y=-1467.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.87, default_y=-1472.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.89, default_y=-1477.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.91, default_y=-1482.92, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.93, default_y=-1477.92, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=223.94, default_y=-1472.92, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.96, default_y=-1467.92, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=275.98, default_y=-1462.92, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='41', width=685.32):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(55.0)
            with Note(default_x=103.52, default_y=-1475.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=203.55, default_y=-1450.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=303.59, default_y=-1465.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=383.61, default_y=-1460.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=483.65, default_y=-1455.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='42', width=392.18):
            with Note(default_x=15.8, default_y=-1475.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')