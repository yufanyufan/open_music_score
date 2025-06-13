with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Süßmayr Sanctus')
    with Identification():
        Creator('Franz Xaver Süßmayr', type='composer')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(4.256)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2625.94)
            PageWidth(2029.14)
            with PageMargins(type='even'):
                LeftMargin(93.9849)
                RightMargin(93.9849)
                TopMargin(93.9849)
                BottomMargin(187.97)
            with PageMargins(type='odd'):
                LeftMargin(93.9849)
                RightMargin(93.9849)
                TopMargin(93.9849)
                BottomMargin(187.97)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('V. Sanctus', default_x=1014.57, default_y=2531.95, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Franz Xaver Süßmayr', default_x=1935.15, default_y=2431.95, justify='right', valign='bottom', font_size='11')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Corni di Bassetto')
            PartAbbreviation('Cor. di B.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Basset Horn')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(72)
                Volume(78.7402)
                Pan(-17.0)
        with ScorePart(id='P2'):
            PartName('Fagotti')
            PartAbbreviation('Fag.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(71)
                Volume(78.7402)
                Pan(-17.0)
        with ScorePart(id='P3'):
            PartName('Trombe in D')
            PartAbbreviation('Tr. in D')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('D Trumpet')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(57)
                Volume(78.7402)
                Pan(26.0)
        with ScorePart(id='P4'):
            PartName('Timpani in D, A')
            PartAbbreviation('Timp.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Timpani')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(5)
                MidiProgram(48)
                Volume(100.0)
                Pan(21.0)
        with PartGroup(type='start', number='2'):
            GroupSymbol('brace')
        with ScorePart(id='P5'):
            PartName('Trombone alto')
            PartAbbreviation('Tbn. A')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Alto Trombone')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(6)
                MidiProgram(58)
                Volume(78.7402)
                Pan(-17.0)
        with ScorePart(id='P6'):
            PartName('Trombone tenore')
            PartAbbreviation('Tbn. T')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Tenor Trombone')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(7)
                MidiProgram(58)
                Volume(78.7402)
                Pan(-20.0)
        with ScorePart(id='P7'):
            PartName('Trombone basso')
            PartAbbreviation('Tbn. B')
            with ScoreInstrument(id='P7-I1'):
                InstrumentName('Bass Trombone')
            MidiDevice(None, id='P7-I1', port=1)
            with MidiInstrument(id='P7-I1'):
                MidiChannel(8)
                MidiProgram(58)
                Volume(78.7402)
                Pan(-20.0)
        PartGroup(type='stop', number='2')
        with PartGroup(type='start', number='2'):
            GroupSymbol('brace')
        with ScorePart(id='P8'):
            PartName('Violino I')
            PartAbbreviation('Vln. I')
            with ScoreInstrument(id='P8-I1'):
                InstrumentName('Violins')
            MidiDevice(None, id='P8-I1', port=1)
            with MidiInstrument(id='P8-I1'):
                MidiChannel(9)
                MidiProgram(49)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P9'):
            PartName('Violino II')
            PartAbbreviation('Vln. II')
            with ScoreInstrument(id='P9-I1'):
                InstrumentName('Violins')
            MidiDevice(None, id='P9-I1', port=1)
            with MidiInstrument(id='P9-I1'):
                MidiChannel(13)
                MidiProgram(49)
                Volume(78.7402)
                Pan(-10.0)
        PartGroup(type='stop', number='2')
        with ScorePart(id='P10'):
            PartName('Viola')
            PartAbbreviation('Vla.')
            with ScoreInstrument(id='P10-I1'):
                InstrumentName('Violas')
            MidiDevice(None, id='P10-I1', port=1)
            with MidiInstrument(id='P10-I1'):
                MidiChannel(16)
                MidiProgram(49)
                Volume(78.7402)
                Pan(7.0)
        with ScorePart(id='P11'):
            PartName('Soprano')
            PartAbbreviation('S.')
            with ScoreInstrument(id='P11-I1'):
                InstrumentName('Soprano')
            MidiDevice(None, id='P11-I1', port=2)
            with MidiInstrument(id='P11-I1'):
                MidiChannel(3)
                MidiProgram(53)
                Volume(100.0)
                Pan(-13.0)
        with ScorePart(id='P12'):
            PartName('Alto')
            PartAbbreviation('A.')
            with ScoreInstrument(id='P12-I1'):
                InstrumentName('Alto')
            MidiDevice(None, id='P12-I1', port=2)
            with MidiInstrument(id='P12-I1'):
                MidiChannel(4)
                MidiProgram(53)
                Volume(100.0)
                Pan(-4.0)
        with ScorePart(id='P13'):
            PartName('Tenore')
            PartAbbreviation('T.')
            with ScoreInstrument(id='P13-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P13-I1', port=2)
            with MidiInstrument(id='P13-I1'):
                MidiChannel(5)
                MidiProgram(53)
                Volume(100.0)
                Pan(6.0)
        with ScorePart(id='P14'):
            PartName('Basso')
            PartAbbreviation('B.')
            with ScoreInstrument(id='P14-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P14-I1', port=2)
            with MidiInstrument(id='P14-I1'):
                MidiChannel(6)
                MidiProgram(53)
                Volume(100.0)
                Pan(12.0)
        with PartGroup(type='start', number='2'):
            GroupSymbol('bracket')
        with ScorePart(id='P15'):
            PartName('Violoncello')
            PartAbbreviation('Vc.')
            with ScoreInstrument(id='P15-I1'):
                InstrumentName('Violoncellos')
            MidiDevice(None, id='P15-I1', port=2)
            with MidiInstrument(id='P15-I1'):
                MidiChannel(7)
                MidiProgram(49)
                Volume(78.7402)
                Pan(13.0)
        with ScorePart(id='P16'):
            PartName('Contrabasso')
            PartAbbreviation('Cb.')
            with ScoreInstrument(id='P16-I1'):
                InstrumentName('Contrabasses')
            MidiDevice(None, id='P16-I1', port=2)
            with MidiInstrument(id='P16-I1'):
                MidiChannel(11)
                MidiProgram(49)
                Volume(78.7402)
                Pan(14.0)
        PartGroup(type='stop', number='2')
        with ScorePart(id='P17'):
            PartName('Organo')
            PartAbbreviation('Org.')
            with ScoreInstrument(id='P17-I1'):
                InstrumentName('Organ')
            MidiDevice(None, id='P17-I1', port=2)
            with MidiInstrument(id='P17-I1'):
                MidiChannel(14)
                MidiProgram(20)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=611.63):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(202.31)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(3)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                with Transpose():
                    Diatonic(-4)
                    Chromatic(-7.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Adagio', default_x=-41.47, default_y=24.04, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=40.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.96, relative_x=6.58, relative_y=-23.67):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=126.66, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=381.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(64.0)
            with Note(default_x=126.66, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=4.34, default_y=-53.25, relative_x=-2.61, relative_y=-15.28):
                    Syllabic('single')
                    Text('.')
            with Note(default_x=381.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(16.0)
        with Measure(number='2', width=523.68):
            with Note(default_x=18.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=281.27, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(64.0)
            with Note(default_x=31.35, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=293.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(16.0)
        with Measure(number='3', width=503.54):
            with Note(default_x=18.56, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=273.84, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(64.0)
            with Note(default_x=18.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=273.84, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(16.0)
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.71)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=104.35, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=206.42, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=308.49, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=410.57, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(64.0)
            with Note(default_x=104.35, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=206.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=308.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=410.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=137.34, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=177.78, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(64.0)
            with Note(default_x=16.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=137.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=177.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(16.0)
        with Measure(number='6', width=454.03):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=168.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=318.7, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=385.57, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(64.0)
            with Forward():
                Duration(32.0)
            with Note(default_x=168.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=318.7, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=385.57, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=435.4):
            with Note(default_x=19.31, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=221.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(64.0)
            with Note(default_x=19.31, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=238.45, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=328.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.71)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=104.35, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=232.56, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=360.77, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=488.98, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(64.0)
            with Note(default_x=104.35, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=232.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=360.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=488.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='9', width=515.8):
            with Note(default_x=21.03, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=143.96, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=390.91, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=452.55, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(64.0)
            with Note(default_x=21.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=144.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=267.25, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='10', width=421.29):
            with Note(default_x=17.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=116.76, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=315.77, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(64.0)
            with Note(default_x=17.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.46, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=117.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=216.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Allegro', default_x=-31.8, default_y=24.04, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=167.0)
            with Note(default_x=36.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(48.0)
            with Note(default_x=36.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(32.0)
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.71)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=160.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=183.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=192.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=181.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=165.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=174.21):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=201.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=207.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.71)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=202.52):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=215.35):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=183.31):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=208.73):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=180.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=207.58):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=197.53):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(128.71)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='30', width=190.32):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=180.55):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=182.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=150.11):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='34', width=151.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='35', width=169.29):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='36', width=170.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='37', width=149.23):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='38', width=92.92):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Fermata(None, type='upright', relative_y=10.0)
    with Part(id='P2'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(83.98)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=5.62, relative_y=-29.43):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=126.66, default_y=-108.98):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=4.13, default_y=-58.05, relative_x=-2.81, relative_y=-20.96):
                    Syllabic('single')
                    Text('.')
            with Note(default_x=126.66, default_y=-98.98):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=381.94, default_y=-108.98):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=381.94, default_y=-98.98):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=523.68):
            with Note(default_x=18.76, default_y=-113.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=18.76, default_y=-103.98):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=281.27, default_y=-113.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=281.27, default_y=-103.98):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=503.54):
            with Note(default_x=18.56, default_y=-113.98):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
            with Note(default_x=18.56, default_y=-98.98):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=273.84, default_y=-113.98):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=273.84, default_y=-98.98):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=104.35, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=206.42, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=206.42, default_y=-80.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=308.49, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=308.49, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=410.57, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=410.57, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=56.47, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=137.34, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=177.78, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(64.0)
            with Note(default_x=16.03, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.47, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=96.91, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=137.34, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=177.78, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(16.0)
        with Measure(number='6', width=454.03):
            with Note(default_x=17.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=76.31, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=122.28, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=168.25, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=318.7, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=385.57, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(64.0)
            with Note(default_x=17.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.31, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.28, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=180.12, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=318.7, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=385.57, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=435.4):
            with Note(default_x=19.31, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=221.92, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=328.65, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(64.0)
            with Note(default_x=19.67, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.84, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=120.01, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=170.17, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=221.92, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=273.67, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=328.65, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=383.63, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.95)
            with Note(default_x=103.99, default_y=-87.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=360.77, default_y=-87.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=488.98, default_y=-82.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(64.0)
            with Note(default_x=104.35, default_y=-112.95):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=168.45, default_y=-122.95):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=232.56, default_y=-107.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=296.66, default_y=-142.95):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=360.77, default_y=-97.95):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=488.98, default_y=-92.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='9', width=515.8):
            with Note(default_x=21.03, default_y=-77.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=143.96, default_y=-82.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=390.91, default_y=-77.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=452.55, default_y=-82.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(64.0)
            with Note(default_x=21.03, default_y=-107.95):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=144.32, default_y=-102.95):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=267.25, default_y=-112.95):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
        with Measure(number='10', width=421.29):
            with Note(default_x=17.8, default_y=-87.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=117.12, default_y=-92.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=216.09, default_y=-87.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(64.0)
            with Note(default_x=17.8, default_y=-107.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.46, default_y=-142.95):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=117.12, default_y=-107.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=166.79, default_y=-107.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=216.45, default_y=-107.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=266.11, default_y=-142.95):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=315.77, default_y=-107.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=365.43, default_y=-107.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-82.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(48.0)
            with Note(default_x=36.8, default_y=-127.95):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.83, default_y=-127.95):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(87.18)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(48.0)
                Voice('1')
            with Backup():
                Duration(48.0)
            with Note(default_x=100.55, default_y=-152.18):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=155.21, default_y=-132.18):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='13', width=160.65):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(48.0)
                Voice('1')
            with Backup():
                Duration(48.0)
            with Note(default_x=18.2, default_y=-137.18):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=65.15, default_y=-147.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=112.1, default_y=-127.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='14', width=183.66):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(48.0)
                Voice('1')
            with Backup():
                Duration(48.0)
            with Note(default_x=18.2, default_y=-122.18):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=82.77, default_y=-127.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=115.87, default_y=-132.18):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=148.96, default_y=-137.18):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=192.78):
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=71.99, default_y=-127.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(48.0)
            with Note(default_x=12.94, default_y=-142.18):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=42.64, default_y=-147.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=72.35, default_y=-152.18):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=102.06, default_y=-147.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=131.77, default_y=-157.18):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=161.47, default_y=-152.18):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='16', width=181.62):
            with Note(default_x=19.01, default_y=-137.18):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.32, default_y=-112.18):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(48.0)
            with Note(default_x=19.01, default_y=-147.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.68, default_y=-157.18):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=126.35, default_y=-142.18):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='17', width=165.05):
            with Note(default_x=15.8, default_y=-117.18):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=65.02, default_y=-127.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=114.24, default_y=-107.18):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-162.18):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=65.02, default_y=-157.18):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=114.24, default_y=-152.18):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=174.21):
            with Note(default_x=15.8, default_y=-102.18):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=88.6, default_y=-107.18):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=116.61, default_y=-112.18):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=144.61, default_y=-117.18):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-147.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=60.6, default_y=-142.18):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=116.61, default_y=-137.18):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='19', width=201.46):
            with Note(default_x=15.8, default_y=-122.18):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=45.55, default_y=-127.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=80.86, default_y=-132.18):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=110.61, default_y=-127.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=140.36, default_y=-137.18):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=170.11, default_y=-132.18):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.44, default_y=-147.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=140.36, default_y=-147.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='20', width=207.81):
            with Note(default_x=19.01, default_y=-127.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=143.81, default_y=-127.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(48.0)
            with Note(default_x=19.01, default_y=-147.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=50.21, default_y=-147.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=81.41, default_y=-152.18):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=112.61, default_y=-147.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=143.81, default_y=-157.18):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=175.01, default_y=-152.18):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(82.39)
            with Note(default_x=100.55, default_y=-122.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=135.65, default_y=-127.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=170.75, default_y=-132.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=205.85, default_y=-127.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=240.95, default_y=-137.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=280.35, default_y=-132.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=100.55, default_y=-142.39):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=252.81, default_y=-142.39):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='22', width=202.52):
            with Note(default_x=15.8, default_y=-127.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=77.51, default_y=-92.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=108.36, default_y=-97.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=139.21, default_y=-102.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=170.06, default_y=-107.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-142.39):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=46.65, default_y=-147.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=77.51, default_y=-152.39):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=108.36, default_y=-147.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=139.21, default_y=-157.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=170.06, default_y=-152.39):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='23', width=215.35):
            with Note(default_x=15.8, default_y=-112.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.79, default_y=-117.39):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=81.78, default_y=-122.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=114.78, default_y=-127.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=147.77, default_y=-132.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=180.76, default_y=-137.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.44, default_y=-162.39):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=147.77, default_y=-157.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=183.31):
            with Note(default_x=19.01, default_y=-142.39):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.13, default_y=-107.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=98.69, default_y=-112.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=125.25, default_y=-117.39):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(48.0)
            with Note(default_x=18.65, default_y=-152.39):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=125.25, default_y=-137.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='25', width=208.73):
            with Note(default_x=15.83, default_y=-122.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=86.26, default_y=-117.39):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=146.69, default_y=-112.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=15.83, default_y=-157.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('2')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('2')
                Type('quarter')
        with Measure(number='26', width=180.39):
            with Note(default_x=15.8, default_y=-107.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=62.37, default_y=-102.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=120.58, default_y=-97.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=149.69, default_y=-102.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(48.0)
                Voice('2')
        with Measure(number='27', width=207.58):
            with Note(default_x=15.8, default_y=-107.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=43.57, default_y=-112.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=94.91, default_y=-117.39):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=122.68, default_y=-112.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=150.44, default_y=-122.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=178.21, default_y=-117.39):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=94.55, default_y=-137.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='28', width=197.53):
            with Note(default_x=19.01, default_y=-112.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.5, default_y=-107.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=77.99, default_y=-102.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=107.47, default_y=-97.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=136.96, default_y=-107.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=166.45, default_y=-102.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=19.01, default_y=-147.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.62, default_y=-122.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.55, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(48.0)
            with Note(default_x=100.55, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=153.53, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=206.17, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='30', width=190.32):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(48.0)
                Voice('1')
            with Backup():
                Duration(48.0)
            with Note(default_x=18.2, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=103.46, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=131.88, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=160.3, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=180.55):
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=66.69, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=41.42, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=67.05, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=92.67, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=118.29, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=143.92, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='32', width=182.65):
            with Note(default_x=19.01, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.2, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(48.0)
            with Note(default_x=19.01, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=43.29, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=67.56, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=91.84, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=116.12, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=146.02, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='33', width=150.11):
            with Note(default_x=15.83, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.63, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=103.44, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=15.83, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=103.44, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='34', width=151.81):
            with Note(default_x=18.65, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(48.0)
            with Note(default_x=18.65, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='35', width=169.29):
            with Note(default_x=18.65, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=118.13, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(48.0)
            with Note(default_x=18.65, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=118.13, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=170.81):
            with Note(default_x=15.8, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=118.19, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=118.19, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='37', width=149.23):
            with Note(default_x=15.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=102.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(48.0)
            with Note(default_x=16.16, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=59.48, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=102.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='38', width=92.92):
            with Note(default_x=15.83, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(48.0)
            with Note(default_x=15.83, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(32.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(0)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                with Transpose():
                    Diatonic(1)
                    Chromatic(2.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=126.66, default_y=-278.98):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=126.66, default_y=-243.98):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=381.94, default_y=-268.98):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=381.94, default_y=-258.98):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=523.68):
            with Note(default_x=18.76, default_y=-258.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=18.76, default_y=-238.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=281.27, default_y=-293.98):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=281.27, default_y=-258.98):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=503.54):
            with Note(default_x=18.56, default_y=-258.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=18.56, default_y=-233.98):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=273.84, default_y=-268.98):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=273.84, default_y=-243.98):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=104.35, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=206.42, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=206.42, default_y=-215.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=308.49, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=410.57, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=410.57, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Backup():
                Duration(64.0)
            with Forward():
                Duration(32.0)
            with Note(default_x=308.49, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(24.0)
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=96.91, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=96.91, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=177.78, default_y=-275.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=177.78, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=210.14, default_y=-275.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=210.14, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=242.49, default_y=-275.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=242.49, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(64.0)
            with Note(default_x=16.03, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(56.0)
        with Measure(number='6', width=454.03):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Direction(placement='above'):
                with DirectionType():
                    Words('ten.', relative_y=40.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-53.98, relative_x=-22.69, relative_y=-30.25):
                        Fz()
                Sound(dynamics=124.44)
            with Note(default_x=168.25, default_y=-275.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=168.25, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='7', width=435.4):
            with Note():
                Rest(measure='yes')
                Duration(64.0)
                Voice('1')
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=360.77, default_y=-242.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=360.77, default_y=-222.95):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=488.98, default_y=-227.95):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=488.98, default_y=-217.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='9', width=515.8):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=144.32, default_y=-262.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=144.32, default_y=-227.95):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=205.97, default_y=-262.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=205.97, default_y=-227.95):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=267.62, default_y=-262.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=267.62, default_y=-227.95):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='10', width=421.29):
            with Note(default_x=17.8, default_y=-277.95):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=17.8, default_y=-242.95):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=117.12, default_y=-277.95):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=117.12, default_y=-242.95):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=216.45, default_y=-277.95):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=216.45, default_y=-242.95):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=315.77, default_y=-277.95):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=315.77, default_y=-242.95):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-262.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=36.8, default_y=-252.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=160.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=183.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=192.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=181.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=165.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=174.21):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=201.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=207.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=202.52):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=215.35):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=183.31):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=208.73):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=180.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=207.58):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=197.53):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=136.96, default_y=-257.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(48.0)
            with Forward():
                Duration(32.0)
            with Note(default_x=136.96, default_y=-257.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.55, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=100.55, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='30', width=190.32):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=180.55):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=182.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=150.11):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='34', width=151.81):
            with Note(default_x=19.01, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=19.01, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='35', width=169.29):
            with Note(default_x=19.01, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(48.0)
            with Note(default_x=19.01, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(32.0)
        with Measure(number='36', width=170.81):
            with Note(default_x=15.8, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=15.8, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=118.19, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=118.19, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='37', width=149.23):
            with Note(default_x=16.16, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.48, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=102.8, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(32.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=102.8, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='38', width=92.92):
            with Note(default_x=15.83, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.83, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=124.44)
            with Note(default_x=127.02, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=191.82, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
            with Note(default_x=207.48, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=223.15, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=238.81, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
            with Note(default_x=254.48, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=319.28, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
            with Note(default_x=334.94, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=350.61, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=366.28, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
            with Note(default_x=381.94, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=523.68):
            with Note(default_x=19.12, default_y=-368.98):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=87.53, default_y=-368.98):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
            with Note(default_x=103.2, default_y=-368.98):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=118.86, default_y=-368.98):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=134.53, default_y=-368.98):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
            with Note(default_x=150.19, default_y=-368.98):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=218.61, default_y=-368.98):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
            with Note(default_x=234.27, default_y=-368.98):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=249.94, default_y=-368.98):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=265.6, default_y=-368.98):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
            with Note(default_x=281.27, default_y=-368.98):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=503.54):
            with Note(default_x=18.92, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=83.72, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
            with Note(default_x=99.39, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=115.05, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=130.72, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
            with Note(default_x=146.38, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=211.18, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
            with Note(default_x=226.85, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=242.51, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=258.18, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
            with Note(default_x=273.84, default_y=-353.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=96.91, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=177.78, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=210.14, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=242.49, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=454.03):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=168.25, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=189.15, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=210.04, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=230.94, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=251.83, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='7', width=435.4):
            with Note():
                Rest(measure='yes')
                Duration(64.0)
                Voice('1')
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=360.77, default_y=-352.95):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=488.98, default_y=-337.95):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='9', width=515.8):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=144.32, default_y=-337.95):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=205.97, default_y=-337.95):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=267.62, default_y=-337.95):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='10', width=421.29):
            with Note(default_x=17.8, default_y=-352.95):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=117.12, default_y=-352.95):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=216.45, default_y=-352.95):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=315.77, default_y=-352.95):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-337.95):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=160.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=183.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=192.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=181.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=165.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=174.21):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=201.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=207.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=202.52):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=215.35):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=183.31):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=208.73):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=180.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=207.58):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=197.53):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=136.96, default_y=-367.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.55, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='30', width=190.32):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=180.55):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=182.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=150.11):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='34', width=151.81):
            with Note(default_x=19.01, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='35', width=169.29):
            with Note(default_x=19.01, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='36', width=170.81):
            with Note(default_x=16.16, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=118.19, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='37', width=149.23):
            with Note(default_x=16.16, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=59.48, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=102.8, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='38', width=92.92):
            with Note(default_x=15.83, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('C')
                    Line(3)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=71.11)
            with Note(default_x=126.66, default_y=-433.98):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=381.94, default_y=-443.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=523.68):
            with Note(default_x=18.76, default_y=-433.98):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=281.27, default_y=-438.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=503.54):
            with Note(default_x=18.56, default_y=-433.98):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=273.84, default_y=-443.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-420.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=206.42, default_y=-415.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=257.46, default_y=-415.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=308.49, default_y=-410.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=410.57, default_y=-415.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-420.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=56.47, default_y=-415.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=137.34, default_y=-415.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=177.42, default_y=-415.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='6', width=454.03):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=168.25, default_y=-415.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=318.7, default_y=-410.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=385.57, default_y=-405.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=435.4):
            with Note(default_x=19.67, default_y=-410.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.01, default_y=-410.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=170.17, default_y=-410.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=221.92, default_y=-415.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=328.65, default_y=-425.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-432.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=232.56, default_y=-432.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=360.77, default_y=-417.95):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=488.98, default_y=-417.95):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=553.08, default_y=-417.95):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='9', width=515.8):
            with Note(default_x=21.03, default_y=-407.95):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=144.32, default_y=-427.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=205.97, default_y=-427.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=267.62, default_y=-412.95):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=390.91, default_y=-412.95):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=452.55, default_y=-412.95):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='10', width=421.29):
            with Note(default_x=14.48, default_y=-417.95):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(64.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-427.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=160.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=183.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=192.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=181.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=165.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=174.21):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=201.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=207.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=202.52):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=215.35):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=183.31):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=208.73):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=180.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=207.58):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=197.53):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='30', width=190.32):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=180.55):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=182.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=150.11):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='34', width=151.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='35', width=169.29):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='36', width=170.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='37', width=149.23):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='38', width=92.92):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P6'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('C')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=71.11)
            with Note(default_x=126.66, default_y=-538.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=381.94, default_y=-548.98):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=523.68):
            with Note(default_x=18.76, default_y=-533.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=281.27, default_y=-543.98):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=503.54):
            with Note(default_x=18.56, default_y=-548.98):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=273.84, default_y=-563.98):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-530.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=206.42, default_y=-535.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=257.46, default_y=-535.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=308.49, default_y=-540.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=410.57, default_y=-530.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-525.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=137.34, default_y=-530.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=177.42, default_y=-535.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='6', width=454.03):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=168.25, default_y=-530.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=318.7, default_y=-530.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=385.57, default_y=-530.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=435.4):
            with Note(default_x=19.67, default_y=-525.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.01, default_y=-525.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=170.17, default_y=-525.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=221.92, default_y=-535.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=328.65, default_y=-540.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-542.95):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=232.56, default_y=-547.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=360.77, default_y=-527.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=488.98, default_y=-522.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=553.08, default_y=-522.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='9', width=515.8):
            with Note(default_x=21.03, default_y=-527.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=144.32, default_y=-532.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=205.97, default_y=-532.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=267.62, default_y=-532.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=390.91, default_y=-517.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='10', width=421.29):
            with Note(default_x=17.8, default_y=-517.95):
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
            with Note(default_x=117.12, default_y=-522.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=166.79, default_y=-522.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=216.09, default_y=-527.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-532.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=160.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=183.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=192.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=181.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=165.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=174.21):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=201.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=207.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=202.52):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=215.35):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=183.31):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=208.73):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=180.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=207.58):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=197.53):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='30', width=190.32):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=180.55):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=182.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=150.11):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='34', width=151.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='35', width=169.29):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='36', width=170.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='37', width=149.23):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='38', width=92.92):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P7'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(71.42)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=71.11)
            with Note(default_x=126.66, default_y=-640.4):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=381.94, default_y=-675.4):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=523.68):
            with Note(default_x=18.76, default_y=-645.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=281.27, default_y=-680.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=503.54):
            with Note(default_x=18.56, default_y=-645.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
            with Note(default_x=273.84, default_y=-680.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-625.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=206.42, default_y=-630.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=257.46, default_y=-630.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=308.49, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=410.57, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.47, default_y=-655.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=96.91, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=137.34, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=177.42, default_y=-630.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='6', width=454.03):
            with Note(default_x=17.8, default_y=-620.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=76.31, default_y=-620.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.28, default_y=-620.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=168.25, default_y=-620.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=318.7, default_y=-625.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=385.57, default_y=-630.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=435.4):
            with Note(default_x=19.67, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.84, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=120.01, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=170.17, default_y=-645.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=221.92, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=273.67, default_y=-630.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=328.65, default_y=-625.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=383.63, default_y=-630.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-637.95):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=232.56, default_y=-632.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=360.77, default_y=-622.95):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=488.98, default_y=-617.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=553.08, default_y=-617.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='9', width=515.8):
            with Note(default_x=21.03, default_y=-632.95):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=144.32, default_y=-627.95):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=205.97, default_y=-627.95):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=267.25, default_y=-637.95):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
        with Measure(number='10', width=421.29):
            with Note(default_x=17.8, default_y=-632.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=117.12, default_y=-632.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=166.79, default_y=-632.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=216.09, default_y=-632.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-652.95):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=160.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=183.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=192.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=181.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=165.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=174.21):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=201.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=207.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=202.52):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=215.35):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=183.31):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=208.73):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=180.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=207.58):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=197.53):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='30', width=190.32):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=180.55):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=182.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=150.11):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='34', width=151.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='35', width=169.29):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='36', width=170.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='37', width=149.23):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='38', width=92.92):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P8'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=381.94, default_y=-805.4):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=410.45, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=438.96, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=467.48, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=495.99, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=524.5, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=553.01, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=581.52, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='2', width=523.68):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=281.27, default_y=-810.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=311.37, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=341.47, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=371.57, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=401.67, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=431.78, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=461.88, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=491.98, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='3', width=503.54):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=273.84, default_y=-810.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=302.36, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.87, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=359.38, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=387.89, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=416.4, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=444.91, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=473.43, default_y=-750.4):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-730.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.87, default_y=-710.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.39, default_y=-710.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.9, default_y=-710.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=206.42, default_y=-760.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=231.94, default_y=-715.0):
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
            with Note(default_x=257.46, default_y=-715.0):
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
            with Note(default_x=282.98, default_y=-715.0):
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
            with Note(default_x=308.49, default_y=-755.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=334.01, default_y=-720.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=359.53, default_y=-720.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=385.05, default_y=-720.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=410.57, default_y=-780.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=436.08, default_y=-725.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=461.6, default_y=-725.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=487.12, default_y=-725.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-765.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.25, default_y=-730.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.47, default_y=-730.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.69, default_y=-730.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=96.91, default_y=-730.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=117.13, default_y=-730.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.34, default_y=-735.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.56, default_y=-735.0):
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
            with Note(default_x=177.78, default_y=-740.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=5.1, relative_y=-28.86):
                        OtherDynamics('.')
                Sound(dynamics=36.67)
            with Note(default_x=210.14, default_y=-795.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=242.49, default_y=-795.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=454.03):
            with Note(default_x=17.8, default_y=-785.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=76.31, default_y=-785.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=122.28, default_y=-785.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=168.25, default_y=-785.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=1.31, relative_y=-31.17):
                        OtherDynamics('.')
                Sound(dynamics=106.67)
            with Note(default_x=210.04, default_y=-735.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.83, default_y=-735.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.27, default_y=-735.0):
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
            with Note(default_x=318.7, default_y=-735.0):
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
            with Note(default_x=352.13, default_y=-735.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=385.57, default_y=-735.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=419.0, default_y=-735.0):
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
        with Measure(number='7', width=435.4):
            with Note(default_x=19.67, default_y=-740.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.76, default_y=-740.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.84, default_y=-740.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.92, default_y=-740.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=120.01, default_y=-740.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.09, default_y=-720.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.17, default_y=-720.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.26, default_y=-720.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=221.92, default_y=-725.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=248.59, default_y=-750.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.67, default_y=-750.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=298.75, default_y=-750.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=328.65, default_y=-755.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=358.55, default_y=-735.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=383.63, default_y=-735.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=408.71, default_y=-735.0):
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
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-722.95):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=136.4, default_y=-747.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.45, default_y=-747.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.51, default_y=-747.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=232.56, default_y=-752.95):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=264.61, default_y=-727.95):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=296.66, default_y=-727.95):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=328.72, default_y=-727.95):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=360.77, default_y=-762.95):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=392.82, default_y=-732.95):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=424.87, default_y=-732.95):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=456.92, default_y=-732.95):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=488.98, default_y=-762.95):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=521.03, default_y=-737.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=553.08, default_y=-737.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=585.13, default_y=-737.95):
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
        with Measure(number='9', width=515.8):
            with Note(default_x=21.03, default_y=-742.95):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=51.85, default_y=-717.95):
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
            with Note(default_x=82.68, default_y=-717.95):
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
            with Note(default_x=113.5, default_y=-717.95):
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
            with Note(default_x=144.32, default_y=-747.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=175.15, default_y=-712.95):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.97, default_y=-712.95):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.79, default_y=-712.95):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=267.62, default_y=-757.95):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=298.44, default_y=-722.95):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=329.26, default_y=-722.95):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=360.08, default_y=-722.95):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=390.91, default_y=-722.95):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=421.73, default_y=-707.95):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=452.55, default_y=-707.95):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=483.38, default_y=-707.95):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='10', width=421.29):
            with Note(default_x=17.8, default_y=-717.95):
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
            with Note(default_x=42.63, default_y=-727.95):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.46, default_y=-727.95):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.29, default_y=-727.95):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=117.12, default_y=-712.95):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.95, default_y=-737.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.79, default_y=-737.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.62, default_y=-737.95):
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
            with Note(default_x=216.45, default_y=-742.95):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=241.28, default_y=-712.95):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.11, default_y=-712.95):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=290.94, default_y=-712.95):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=315.77, default_y=-742.95):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=340.6, default_y=-717.95):
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
            with Note(default_x=365.43, default_y=-717.95):
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
            with Note(default_x=390.26, default_y=-717.95):
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
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-747.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=160.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=183.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=192.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=181.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=165.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=174.21):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=201.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=207.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=202.52):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=215.35):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=81.42, default_y=-777.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='24', width=183.31):
            with Note(default_x=19.01, default_y=-787.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.77, default_y=-762.39):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='25', width=208.73):
            with Note(default_x=15.83, default_y=-767.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=86.26, default_y=-777.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=146.69, default_y=-757.39):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='26', width=180.39):
            with Note(default_x=15.8, default_y=-752.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=91.48, default_y=-757.39):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=120.58, default_y=-762.39):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=149.69, default_y=-767.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='27', width=207.58):
            with Note(default_x=15.8, default_y=-772.39):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=43.57, default_y=-777.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=94.91, default_y=-782.39):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=122.68, default_y=-777.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=150.44, default_y=-787.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=178.21, default_y=-782.39):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=197.53):
            with Note(default_x=19.01, default_y=-777.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=136.96, default_y=-777.39):
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
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.55, default_y=-760.0):
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
            with Note(default_x=127.22, default_y=-765.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=153.53, default_y=-770.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=179.85, default_y=-765.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=206.17, default_y=-775.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=246.86, default_y=-770.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='30', width=190.32):
            with Note(default_x=18.2, default_y=-765.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=75.04, default_y=-730.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=103.46, default_y=-735.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=131.88, default_y=-740.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=160.3, default_y=-745.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='31', width=180.55):
            with Note(default_x=15.8, default_y=-750.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=41.42, default_y=-755.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=67.05, default_y=-760.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=92.67, default_y=-765.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=118.29, default_y=-770.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=143.92, default_y=-775.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='32', width=182.65):
            with Note(default_x=19.01, default_y=-780.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.56, default_y=-745.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=91.84, default_y=-750.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=116.12, default_y=-755.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='33', width=150.11):
            with Note(default_x=15.83, default_y=-760.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=37.73, default_y=-725.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=59.63, default_y=-755.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=81.54, default_y=-725.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=103.44, default_y=-750.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=125.35, default_y=-725.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='34', width=151.81):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-49.6, relative_x=3.18, relative_y=-18.72):
                        OtherDynamics('.')
                Sound(dynamics=124.44)
            with Note(default_x=19.01, default_y=-745.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=40.62, default_y=-760.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=62.22, default_y=-735.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=83.83, default_y=-740.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=105.43, default_y=-745.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=127.04, default_y=-750.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='35', width=169.29):
            with Note(default_x=19.01, default_y=-755.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=43.79, default_y=-730.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=68.57, default_y=-720.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=93.35, default_y=-725.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=118.13, default_y=-730.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=142.91, default_y=-735.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='36', width=170.81):
            with Note(default_x=16.16, default_y=-740.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=41.67, default_y=-735.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=67.18, default_y=-730.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=92.68, default_y=-725.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=118.19, default_y=-720.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=143.7, default_y=-715.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='37', width=149.23):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=37.82, default_y=-710.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=81.14, default_y=-705.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=124.46, default_y=-715.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='38', width=92.92):
            with Note(default_x=15.83, default_y=-710.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P9'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=381.94, default_y=-910.4):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=410.45, default_y=-865.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=438.96, default_y=-865.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=467.48, default_y=-865.4):
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
            with Note(default_x=495.99, default_y=-865.4):
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
            with Note(default_x=524.5, default_y=-865.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=553.01, default_y=-865.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=581.52, default_y=-865.4):
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
        with Measure(number='2', width=523.68):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=281.27, default_y=-915.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=311.37, default_y=-860.4):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=341.47, default_y=-860.4):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=371.57, default_y=-860.4):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=401.67, default_y=-860.4):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=431.78, default_y=-860.4):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=461.88, default_y=-860.4):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=491.98, default_y=-860.4):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='3', width=503.54):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=273.84, default_y=-915.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=302.36, default_y=-865.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.87, default_y=-865.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=359.38, default_y=-865.4):
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
            with Note(default_x=387.89, default_y=-865.4):
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
            with Note(default_x=416.4, default_y=-865.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=444.91, default_y=-865.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=473.43, default_y=-865.4):
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
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-835.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.87, default_y=-835.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.39, default_y=-835.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.9, default_y=-835.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=206.42, default_y=-840.0):
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
            with Note(default_x=231.94, default_y=-875.0):
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
            with Note(default_x=257.46, default_y=-875.0):
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
            with Note(default_x=282.98, default_y=-875.0):
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
            with Note(default_x=308.49, default_y=-880.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=334.01, default_y=-845.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=359.53, default_y=-845.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=385.05, default_y=-845.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=410.57, default_y=-840.0):
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
            with Note(default_x=436.08, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=461.6, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=487.12, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-855.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.25, default_y=-845.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.47, default_y=-845.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.69, default_y=-845.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=96.91, default_y=-845.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=117.13, default_y=-845.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.34, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.56, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=177.78, default_y=-855.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=7.95, relative_y=-1.62):
                        OtherDynamics('.')
                Sound(dynamics=36.67)
            with Note(default_x=210.14, default_y=-900.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=242.49, default_y=-900.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=454.03):
            with Note(default_x=17.8, default_y=-890.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=76.31, default_y=-890.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=122.28, default_y=-890.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=168.25, default_y=-890.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=16.05, relative_x=2.3, relative_y=14.41):
                        OtherDynamics('.')
                Sound(dynamics=106.67)
            with Note(default_x=210.04, default_y=-850.0):
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
            with Note(default_x=251.83, default_y=-850.0):
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
            with Note(default_x=285.27, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=318.7, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=352.13, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=385.57, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=419.0, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='7', width=435.4):
            with Note(default_x=19.67, default_y=-845.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.76, default_y=-860.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.84, default_y=-860.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.92, default_y=-860.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=120.01, default_y=-860.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.09, default_y=-835.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.17, default_y=-835.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.26, default_y=-835.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=221.92, default_y=-840.0):
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
            with Note(default_x=248.59, default_y=-865.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.67, default_y=-865.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=298.75, default_y=-865.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=328.65, default_y=-885.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=358.55, default_y=-850.0):
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
            with Note(default_x=383.63, default_y=-850.0):
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
            with Note(default_x=408.71, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-852.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=136.4, default_y=-862.95):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.45, default_y=-862.95):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.51, default_y=-862.95):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=232.56, default_y=-867.95):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=264.61, default_y=-857.95):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=296.66, default_y=-857.95):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=328.72, default_y=-857.95):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=360.77, default_y=-872.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=392.82, default_y=-847.95):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=424.87, default_y=-847.95):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=456.92, default_y=-847.95):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=488.98, default_y=-877.95):
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
            with Note(default_x=521.03, default_y=-852.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=553.08, default_y=-852.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=585.13, default_y=-852.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='9', width=515.8):
            with Note(default_x=21.03, default_y=-857.95):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=51.85, default_y=-837.95):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=82.68, default_y=-837.95):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=113.5, default_y=-837.95):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=144.32, default_y=-882.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=175.15, default_y=-842.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.97, default_y=-842.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.79, default_y=-842.95):
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
            with Note(default_x=267.62, default_y=-887.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=298.44, default_y=-842.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=329.26, default_y=-842.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=360.08, default_y=-842.95):
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
            with Note(default_x=390.91, default_y=-847.95):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=421.73, default_y=-827.95):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=452.55, default_y=-827.95):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=483.38, default_y=-827.95):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='10', width=421.29):
            with Note(default_x=17.8, default_y=-867.95):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.63, default_y=-837.95):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.46, default_y=-837.95):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.29, default_y=-837.95):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=117.12, default_y=-842.95):
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
            with Note(default_x=141.95, default_y=-852.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.79, default_y=-852.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.62, default_y=-852.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=216.45, default_y=-852.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=241.28, default_y=-847.95):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.11, default_y=-847.95):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=290.94, default_y=-847.95):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=315.77, default_y=-857.95):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=340.6, default_y=-847.95):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=365.43, default_y=-847.95):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=390.26, default_y=-847.95):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-852.95):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=160.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=183.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=192.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=181.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=165.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=174.21):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=201.46):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=80.5, default_y=-907.18):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='20', width=207.81):
            with Note(default_x=19.01, default_y=-912.18):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.05, default_y=-892.18):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.55, default_y=-892.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=170.75, default_y=-902.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=240.95, default_y=-882.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='22', width=202.52):
            with Note(default_x=15.8, default_y=-877.39):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=108.36, default_y=-882.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=139.21, default_y=-887.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=170.06, default_y=-892.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='23', width=215.35):
            with Note(default_x=15.8, default_y=-897.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=48.79, default_y=-902.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=81.78, default_y=-907.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=114.78, default_y=-902.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=147.77, default_y=-912.39):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=180.76, default_y=-907.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='24', width=183.31):
            with Note(default_x=19.01, default_y=-902.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=45.57, default_y=-897.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=72.13, default_y=-892.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=98.69, default_y=-897.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=125.25, default_y=-892.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=155.15, default_y=-887.39):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='25', width=208.73):
            with Note(default_x=15.83, default_y=-882.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=146.69, default_y=-882.39):
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
        with Measure(number='26', width=180.39):
            with Note(default_x=15.8, default_y=-882.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=62.37, default_y=-887.39):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=120.58, default_y=-882.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=149.69, default_y=-887.39):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='27', width=207.58):
            with Note(default_x=15.8, default_y=-892.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=43.57, default_y=-897.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=94.91, default_y=-902.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=122.68, default_y=-907.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=150.44, default_y=-902.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=197.53):
            with Note(default_x=19.01, default_y=-897.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=48.5, default_y=-902.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=77.99, default_y=-907.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=107.47, default_y=-902.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=136.96, default_y=-912.39):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=166.45, default_y=-907.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.55, default_y=-885.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=153.53, default_y=-900.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=206.17, default_y=-885.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='30', width=190.32):
            with Note(default_x=18.2, default_y=-885.0):
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
            with Note(default_x=46.62, default_y=-890.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=75.04, default_y=-895.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=103.46, default_y=-890.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=131.88, default_y=-900.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=160.3, default_y=-895.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='31', width=180.55):
            with Note(default_x=15.8, default_y=-905.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='32', width=182.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=150.11):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=7.5, relative_x=74.37, relative_y=-14.28):
                        OtherDynamics('.')
                Sound(dynamics=124.44)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='34', width=151.81):
            with Note(default_x=19.01, default_y=-865.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=62.22, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=83.83, default_y=-855.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=105.43, default_y=-860.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=127.04, default_y=-865.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='35', width=169.29):
            with Note(default_x=19.01, default_y=-870.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=43.79, default_y=-860.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=68.57, default_y=-835.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=93.35, default_y=-840.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=118.13, default_y=-845.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=142.91, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='36', width=170.81):
            with Note(default_x=16.16, default_y=-855.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=41.67, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=67.18, default_y=-845.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=92.68, default_y=-840.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=118.19, default_y=-835.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=143.7, default_y=-845.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='37', width=149.23):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=37.82, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=81.14, default_y=-860.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=81.14, default_y=-835.0):
                Chord()
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
            with Note(default_x=124.46, default_y=-865.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=124.46, default_y=-835.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='38', width=92.92):
            with Note(default_x=15.83, default_y=-865.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.83, default_y=-840.0):
                Chord()
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
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P10'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('C')
                    Line(3)
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=381.94, default_y=-1020.4):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=410.45, default_y=-950.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=438.96, default_y=-950.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=467.48, default_y=-950.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=495.99, default_y=-950.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=524.5, default_y=-950.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=553.01, default_y=-950.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=581.52, default_y=-950.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='2', width=523.68):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=281.27, default_y=-1025.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=311.37, default_y=-945.4):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=341.47, default_y=-945.4):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=371.57, default_y=-945.4):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=401.67, default_y=-945.4):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=431.78, default_y=-945.4):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=461.88, default_y=-945.4):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=491.98, default_y=-945.4):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='3', width=503.54):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=273.84, default_y=-1025.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=302.36, default_y=-950.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.87, default_y=-950.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=359.38, default_y=-950.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=387.89, default_y=-950.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=416.4, default_y=-950.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=444.91, default_y=-950.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=473.43, default_y=-950.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-935.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.87, default_y=-935.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.39, default_y=-935.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.9, default_y=-935.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=206.42, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=231.94, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=257.46, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.98, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=308.49, default_y=-945.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=334.01, default_y=-945.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=359.53, default_y=-945.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=385.05, default_y=-945.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=410.57, default_y=-950.0):
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
            with Note(default_x=436.08, default_y=-950.0):
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
            with Note(default_x=461.6, default_y=-950.0):
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
            with Note(default_x=487.12, default_y=-950.0):
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
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-955.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.25, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.47, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.69, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=96.91, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=117.13, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.34, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.56, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=177.78, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-51.35, relative_x=-3.65, relative_y=-19.98):
                        OtherDynamics('.')
                Sound(dynamics=36.67)
            with Note(default_x=210.14, default_y=-975.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=242.49, default_y=-975.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=454.03):
            with Note(default_x=17.8, default_y=-965.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=76.31, default_y=-965.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=122.28, default_y=-965.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=168.25, default_y=-965.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-49.93, relative_x=1.97, relative_y=-6.69):
                        OtherDynamics('.')
                Sound(dynamics=106.67)
            with Note(default_x=210.04, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.83, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.27, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=318.7, default_y=-935.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=352.13, default_y=-935.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=385.57, default_y=-930.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=419.0, default_y=-930.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='7', width=435.4):
            with Note(default_x=19.67, default_y=-935.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.76, default_y=-935.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.84, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.92, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=120.01, default_y=-945.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.09, default_y=-955.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.17, default_y=-955.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.26, default_y=-955.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=221.92, default_y=-965.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=248.59, default_y=-950.0):
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
            with Note(default_x=273.67, default_y=-950.0):
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
            with Note(default_x=298.75, default_y=-950.0):
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
            with Note(default_x=328.65, default_y=-950.0):
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
            with Note(default_x=358.55, default_y=-960.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=383.63, default_y=-960.0):
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
            with Note(default_x=408.71, default_y=-960.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.14)
            with Note(default_x=104.35, default_y=-958.09):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=136.4, default_y=-948.09):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.45, default_y=-948.09):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.51, default_y=-948.09):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=232.56, default_y=-958.09):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=264.61, default_y=-923.09):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=296.66, default_y=-923.09):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=328.72, default_y=-923.09):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=360.77, default_y=-958.09):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=392.82, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=424.87, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=456.92, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=488.98, default_y=-928.09):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=521.03, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=553.08, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=585.13, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='9', width=515.8):
            with Note(default_x=21.03, default_y=-948.09):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=51.85, default_y=-923.09):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=82.68, default_y=-923.09):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=113.5, default_y=-923.09):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=144.32, default_y=-953.09):
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
            with Note(default_x=175.15, default_y=-938.09):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.97, default_y=-938.09):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.79, default_y=-938.09):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=267.62, default_y=-948.09):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=298.44, default_y=-928.09):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=329.26, default_y=-928.09):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=360.08, default_y=-928.09):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=390.91, default_y=-948.09):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=421.73, default_y=-938.09):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=452.55, default_y=-938.09):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=483.38, default_y=-938.09):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='10', width=421.29):
            with Note(default_x=17.8, default_y=-958.09):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.63, default_y=-933.09):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.46, default_y=-933.09):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.29, default_y=-933.09):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=117.12, default_y=-928.09):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.95, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.79, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.62, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=216.45, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=241.28, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.11, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=290.94, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=315.77, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=340.6, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=365.43, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=390.26, default_y=-943.09):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-953.09):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=160.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=183.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=192.78):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=71.99, default_y=-997.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='16', width=181.62):
            with Note(default_x=19.01, default_y=-1007.18):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.32, default_y=-982.18):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='17', width=165.05):
            with Note(default_x=15.8, default_y=-987.18):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=65.02, default_y=-997.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.24, default_y=-977.18):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='18', width=174.21):
            with Note(default_x=15.8, default_y=-972.18):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=88.6, default_y=-977.18):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=116.61, default_y=-982.18):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=144.61, default_y=-987.18):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='19', width=201.46):
            with Note(default_x=15.8, default_y=-992.18):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=45.55, default_y=-997.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=80.86, default_y=-1002.18):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=110.61, default_y=-997.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=140.36, default_y=-1007.18):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=170.11, default_y=-1002.18):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=207.81):
            with Note(default_x=19.01, default_y=-997.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=143.81, default_y=-997.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.55, default_y=-992.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=135.65, default_y=-997.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=170.75, default_y=-1002.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=205.85, default_y=-997.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=240.95, default_y=-1007.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=280.35, default_y=-1002.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='22', width=202.52):
            with Note(default_x=15.8, default_y=-997.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=77.51, default_y=-962.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=108.36, default_y=-967.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=139.21, default_y=-972.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=170.06, default_y=-977.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='23', width=215.35):
            with Note(default_x=15.8, default_y=-982.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=48.79, default_y=-987.39):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=81.78, default_y=-992.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=114.78, default_y=-997.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=147.77, default_y=-1002.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=180.76, default_y=-1007.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='24', width=183.31):
            with Note(default_x=19.01, default_y=-1012.39):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.13, default_y=-972.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=98.69, default_y=-977.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=125.25, default_y=-987.39):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='25', width=208.73):
            with Note(default_x=15.83, default_y=-992.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=86.26, default_y=-987.39):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=146.69, default_y=-982.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='26', width=180.39):
            with Note(default_x=15.8, default_y=-977.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=62.37, default_y=-972.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.58, default_y=-967.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=149.69, default_y=-972.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='27', width=207.58):
            with Note(default_x=15.8, default_y=-977.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=43.57, default_y=-982.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=94.91, default_y=-987.39):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=122.68, default_y=-982.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=150.44, default_y=-992.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=178.21, default_y=-987.39):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=197.53):
            with Note(default_x=19.01, default_y=-982.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.5, default_y=-977.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=77.99, default_y=-972.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=107.47, default_y=-967.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=136.96, default_y=-977.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=166.45, default_y=-972.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.55, default_y=-950.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='30', width=190.32):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=180.55):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=66.69, default_y=-975.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='32', width=182.65):
            with Note(default_x=19.01, default_y=-985.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.2, default_y=-960.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='33', width=150.11):
            with Note(default_x=15.83, default_y=-965.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.63, default_y=-975.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=103.44, default_y=-955.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='34', width=151.81):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-49.53, relative_x=3.92, relative_y=-8.79):
                        OtherDynamics('.')
                Sound(dynamics=124.44)
            with Note(default_x=19.01, default_y=-950.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=40.62, default_y=-965.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=62.22, default_y=-960.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=83.83, default_y=-955.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=105.43, default_y=-950.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=127.04, default_y=-940.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='35', width=169.29):
            with Note(default_x=19.01, default_y=-960.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=68.57, default_y=-955.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=93.35, default_y=-950.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=118.13, default_y=-945.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=142.91, default_y=-935.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='36', width=170.81):
            with Note(default_x=16.16, default_y=-945.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=41.67, default_y=-950.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=67.18, default_y=-955.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=92.68, default_y=-960.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=118.19, default_y=-965.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=143.7, default_y=-945.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='37', width=149.23):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=37.82, default_y=-950.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=81.14, default_y=-945.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=124.46, default_y=-955.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='38', width=92.92):
            with Note(default_x=15.83, default_y=-960.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P11'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('C')
                    Line(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=8.4, relative_x=-15.33, relative_y=2.97):
                        F()
                Sound(dynamics=141.11)
            with Note(default_x=126.66, default_y=-1075.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-41.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text('San')
            with Note(default_x=381.94, default_y=-1090.4):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.83, default_y=-41.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('ctus,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=523.68):
            with Note(default_x=18.76, default_y=-1070.4):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-41.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text('san')
            with Note(default_x=281.27, default_y=-1090.4):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.83, default_y=-41.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('ctus,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=503.54):
            with Note(default_x=18.56, default_y=-1065.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-41.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text('san')
            with Note(default_x=273.84, default_y=-1075.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('ctus')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-1035.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=206.42, default_y=-1040.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mi')
            with Note(default_x=257.46, default_y=-1040.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('nus')
            with Note(default_x=308.49, default_y=-1045.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('De')
            with Note(default_x=410.57, default_y=-1050.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('us')
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-1055.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
            with Note(default_x=56.47, default_y=-1035.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=137.34, default_y=-1040.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ba')
            with Note(default_x=177.42, default_y=-1045.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=8.62, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('oth.')
        with Measure(number='6', width=454.03):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=168.25, default_y=-1040.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ple')
            with Note(default_x=318.7, default_y=-1040.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ni')
            with Note(default_x=385.57, default_y=-1040.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('sunt')
        with Measure(number='7', width=435.4):
            with Note(default_x=19.67, default_y=-1045.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('cae')
            with Note(default_x=120.01, default_y=-1045.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('li')
            with Note(default_x=170.17, default_y=-1045.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('et')
            with Note(default_x=221.92, default_y=-1045.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ter')
            with Note(default_x=328.65, default_y=-1050.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-1053.09):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=232.56, default_y=-1058.09):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Note(default_x=360.77, default_y=-1048.09):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
            with Note(default_x=488.98, default_y=-1053.09):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=553.08, default_y=-1053.09):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('a,')
        with Measure(number='9', width=515.8):
            with Note(default_x=21.03, default_y=-1038.09):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
            with Note(default_x=144.32, default_y=-1043.09):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=205.97, default_y=-1043.09):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('a,')
            with Note(default_x=267.62, default_y=-1043.09):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
            with Note(default_x=390.91, default_y=-1048.09):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=452.55, default_y=-1053.09):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('a')
        with Measure(number='10', width=421.29):
            with Note(default_x=17.8, default_y=-1058.09):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tu')
            with Note(default_x=116.76, default_y=-1053.09):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=315.77, default_y=-1058.09):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-1053.09):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.46, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('a.')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=160.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=183.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=192.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=181.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=165.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=174.21):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=201.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=207.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=202.52):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=215.35):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=81.42, default_y=-1082.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('O')
        with Measure(number='24', width=183.31):
            with Note(default_x=19.01, default_y=-1092.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('san')
            with Note(default_x=71.77, default_y=-1067.39):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='25', width=208.73):
            with Note(default_x=15.83, default_y=-1072.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-42.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                    Extend()
            with Note(default_x=86.26, default_y=-1082.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=146.69, default_y=-1062.39):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('ex')
        with Measure(number='26', width=180.39):
            with Note(default_x=15.8, default_y=-1057.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-42.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cel')
            with Note(default_x=91.48, default_y=-1062.39):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=120.58, default_y=-1067.39):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=149.69, default_y=-1072.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='27', width=207.58):
            with Note(default_x=15.8, default_y=-1077.39):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=43.57, default_y=-1082.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=94.91, default_y=-1087.39):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=122.68, default_y=-1082.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=150.44, default_y=-1092.39):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=178.21, default_y=-1087.39):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=197.53):
            with Note(default_x=19.01, default_y=-1082.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.11, default_y=-42.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('sis,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=136.96, default_y=-1082.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-42.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('o')
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.55, default_y=-1065.0):
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
            with Note(default_x=127.22, default_y=-1070.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=153.53, default_y=-1075.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=179.85, default_y=-1070.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=206.17, default_y=-1080.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=246.86, default_y=-1075.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='30', width=190.32):
            with Note(default_x=18.2, default_y=-1070.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-43.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('san')
            with Note(default_x=75.04, default_y=-1035.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=103.46, default_y=-1040.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=131.88, default_y=-1045.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=160.3, default_y=-1050.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=180.55):
            with Note(default_x=15.8, default_y=-1055.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=41.42, default_y=-1060.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=67.05, default_y=-1065.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=92.67, default_y=-1070.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=118.29, default_y=-1075.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=143.92, default_y=-1080.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=182.65):
            with Note(default_x=19.01, default_y=-1085.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=67.56, default_y=-1050.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=91.84, default_y=-1055.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=116.12, default_y=-1060.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ex')
        with Measure(number='33', width=150.11):
            with Note(default_x=15.83, default_y=-1065.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cel')
            with Note(default_x=59.63, default_y=-1060.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=103.44, default_y=-1055.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.11, default_y=-43.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('sis,')
        with Measure(number='34', width=151.81):
            with Note(default_x=18.65, default_y=-1050.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('o')
        with Measure(number='35', width=169.29):
            with Note(default_x=18.65, default_y=-1060.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('san')
            with Note(default_x=118.13, default_y=-1045.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='36', width=170.81):
            with Note(default_x=15.8, default_y=-1055.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('in')
            with Note(default_x=118.19, default_y=-1035.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ex')
        with Measure(number='37', width=149.23):
            with Note(default_x=16.16, default_y=-1040.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cel')
            with Note(default_x=59.12, default_y=-1045.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='38', width=92.92):
            with Note(default_x=15.83, default_y=-1050.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.77, default_y=-43.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('sis.')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P12'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(87.01)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('C')
                    Line(3)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=8.4, relative_x=-18.62, relative_y=2.97):
                        F()
                Sound(dynamics=141.11)
            with Note(default_x=126.66, default_y=-1197.41):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('San')
            with Note(default_x=381.94, default_y=-1207.41):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.83, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ctus,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=523.68):
            with Note(default_x=18.76, default_y=-1197.41):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('san')
            with Note(default_x=281.27, default_y=-1202.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.83, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ctus,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=503.54):
            with Note(default_x=18.56, default_y=-1197.41):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('san')
            with Note(default_x=273.84, default_y=-1207.41):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ctus')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(85.12)
            with Note(default_x=104.35, default_y=-1175.12):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=206.42, default_y=-1170.12):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mi')
            with Note(default_x=257.46, default_y=-1170.12):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('nus')
            with Note(default_x=308.49, default_y=-1165.12):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('De')
            with Note(default_x=410.57, default_y=-1170.12):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('us')
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-1175.12):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
            with Note(default_x=56.47, default_y=-1170.12):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=137.34, default_y=-1170.12):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ba')
            with Note(default_x=177.42, default_y=-1170.12):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=8.62, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('oth.')
        with Measure(number='6', width=454.03):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=168.25, default_y=-1170.12):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ple')
            with Note(default_x=318.7, default_y=-1165.12):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ni')
            with Note(default_x=385.57, default_y=-1160.12):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('sunt')
        with Measure(number='7', width=435.4):
            with Note(default_x=19.67, default_y=-1165.12):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('cae')
            with Note(default_x=120.01, default_y=-1165.12):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('li')
            with Note(default_x=170.17, default_y=-1165.12):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('et')
            with Note(default_x=221.92, default_y=-1170.12):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ter')
            with Note(default_x=328.65, default_y=-1180.12):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(80.06)
            with Note(default_x=104.35, default_y=-1183.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=232.56, default_y=-1183.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Note(default_x=360.77, default_y=-1168.15):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
            with Note(default_x=488.98, default_y=-1168.15):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=553.08, default_y=-1168.15):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('a,')
        with Measure(number='9', width=515.8):
            with Note(default_x=21.03, default_y=-1158.15):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
            with Note(default_x=144.32, default_y=-1178.15):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=205.97, default_y=-1178.15):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('a,')
            with Note(default_x=267.62, default_y=-1163.15):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
            with Note(default_x=390.91, default_y=-1163.15):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=452.55, default_y=-1163.15):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('a')
        with Measure(number='10', width=421.29):
            with Note(default_x=14.48, default_y=-1168.15):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(64.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tu')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-1178.15):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.46, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('a.')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=160.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=183.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=192.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=181.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=165.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=174.21):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=201.46):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=80.5, default_y=-1192.18):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('O')
        with Measure(number='20', width=207.81):
            with Note(default_x=19.01, default_y=-1197.18):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('san')
            with Note(default_x=81.05, default_y=-1177.18):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(93.65)
            with Note(default_x=100.55, default_y=-1206.04):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                    Extend()
            with Note(default_x=170.75, default_y=-1216.04):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=240.95, default_y=-1196.04):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('ex')
        with Measure(number='22', width=202.52):
            with Note(default_x=15.8, default_y=-1191.04):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.09, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cel')
            with Note(default_x=108.36, default_y=-1196.04):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=139.21, default_y=-1201.04):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=170.06, default_y=-1206.04):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='23', width=215.35):
            with Note(default_x=15.8, default_y=-1211.04):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=48.79, default_y=-1216.04):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=81.78, default_y=-1221.04):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=114.78, default_y=-1216.04):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=147.77, default_y=-1226.04):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=180.76, default_y=-1221.04):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='24', width=183.31):
            with Note(default_x=19.01, default_y=-1216.04):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.57, default_y=-1211.04):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=72.13, default_y=-1206.04):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=98.69, default_y=-1211.04):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=125.25, default_y=-1206.04):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=155.15, default_y=-1201.04):
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
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='25', width=208.73):
            with Note(default_x=15.83, default_y=-1196.04):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.11, default_y=-47.09, relative_y=-30.0):
                    Syllabic('end')
                    Text('sis,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=146.69, default_y=-1196.04):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.09, relative_y=-30.0):
                    Syllabic('begin')
                    Text('o')
        with Measure(number='26', width=180.39):
            with Note(default_x=15.8, default_y=-1196.04):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-47.09, relative_y=-30.0):
                    Syllabic('middle')
                    Text('san')
            with Note(default_x=62.37, default_y=-1201.04):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=120.58, default_y=-1196.04):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=149.69, default_y=-1201.04):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='27', width=207.58):
            with Note(default_x=15.8, default_y=-1206.04):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=43.57, default_y=-1211.04):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=94.91, default_y=-1216.04):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=122.68, default_y=-1221.04):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=150.44, default_y=-1216.04):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.09, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='28', width=197.53):
            with Note(default_x=19.01, default_y=-1211.04):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                    Extend()
            with Note(default_x=48.5, default_y=-1216.04):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=77.99, default_y=-1221.04):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=107.47, default_y=-1216.04):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=136.96, default_y=-1226.04):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.09, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ex')
            with Note(default_x=166.45, default_y=-1221.04):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.9)
            with Note(default_x=100.55, default_y=-1199.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-43.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cel')
            with Note(default_x=153.53, default_y=-1214.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=206.17, default_y=-1199.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='30', width=190.32):
            with Note(default_x=18.2, default_y=-1199.9):
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
            with Note(default_x=46.62, default_y=-1204.9):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=75.04, default_y=-1209.9):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=103.46, default_y=-1204.9):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=131.88, default_y=-1214.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=160.3, default_y=-1209.9):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='31', width=180.55):
            with Note(default_x=15.8, default_y=-1219.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.35, default_y=-43.4, relative_x=1.24, relative_y=-48.96):
                    Syllabic('end')
                    Text('sis,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='32', width=182.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=150.11):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='34', width=151.81):
            with Note(default_x=18.65, default_y=-1179.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('o')
        with Measure(number='35', width=169.29):
            with Note(default_x=18.65, default_y=-1184.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('san')
            with Note(default_x=118.13, default_y=-1174.9):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='36', width=170.81):
            with Note(default_x=15.8, default_y=-1184.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=118.19, default_y=-1169.9):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ex')
        with Measure(number='37', width=149.23):
            with Note(default_x=16.16, default_y=-1164.9):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cel')
            with Note(default_x=59.48, default_y=-1174.9):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=102.8, default_y=-1179.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='38', width=92.92):
            with Note(default_x=15.83, default_y=-1179.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.77, default_y=-43.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('sis.')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P13'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(85.6)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('C')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=8.4, relative_x=-15.33, relative_y=2.97):
                        F()
                Sound(dynamics=141.11)
            with Note(default_x=126.66, default_y=-1323.01):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('San')
            with Note(default_x=381.94, default_y=-1333.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.83, default_y=-45.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('ctus,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=523.68):
            with Note(default_x=18.76, default_y=-1318.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('san')
            with Note(default_x=281.27, default_y=-1328.01):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.83, default_y=-45.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('ctus,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=503.54):
            with Note(default_x=18.56, default_y=-1333.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('san')
            with Note(default_x=273.84, default_y=-1348.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('ctus')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-1285.12):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=206.42, default_y=-1290.12):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mi')
            with Note(default_x=257.46, default_y=-1290.12):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('nus')
            with Note(default_x=308.49, default_y=-1295.12):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('De')
            with Note(default_x=410.57, default_y=-1285.12):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('us')
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-1280.12):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
            with Note(default_x=137.34, default_y=-1285.12):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ba')
            with Note(default_x=177.42, default_y=-1290.12):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=8.62, default_y=-42.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('oth.')
        with Measure(number='6', width=454.03):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=168.25, default_y=-1285.12):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ple')
            with Note(default_x=318.7, default_y=-1285.12):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('ni')
            with Note(default_x=385.57, default_y=-1285.12):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('sunt')
        with Measure(number='7', width=435.4):
            with Note(default_x=19.67, default_y=-1280.12):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('cae')
            with Note(default_x=120.01, default_y=-1280.12):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('li')
            with Note(default_x=170.17, default_y=-1280.12):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('et')
            with Note(default_x=221.92, default_y=-1290.12):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-42.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ter')
            with Note(default_x=328.65, default_y=-1295.12):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(89.28)
            with Note(default_x=104.35, default_y=-1317.43):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=232.56, default_y=-1322.43):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Note(default_x=360.77, default_y=-1302.43):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
            with Note(default_x=488.98, default_y=-1297.43):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.85, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=553.08, default_y=-1297.43):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-41.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('a,')
        with Measure(number='9', width=515.8):
            with Note(default_x=21.03, default_y=-1302.43):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
            with Note(default_x=144.32, default_y=-1307.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.85, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=205.97, default_y=-1307.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-41.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('a,')
            with Note(default_x=267.62, default_y=-1307.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-41.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
            with Note(default_x=390.91, default_y=-1292.43):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='10', width=421.29):
            with Note(default_x=17.8, default_y=-1292.43):
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
                    Slur(type='stop', number=1)
            with Note(default_x=117.12, default_y=-1297.43):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.85, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=166.79, default_y=-1297.43):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('a')
            with Note(default_x=216.09, default_y=-1302.43):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-41.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tu')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-1307.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.46, default_y=-41.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('a.')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(89.11)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=160.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=183.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=192.78):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=71.99, default_y=-1326.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('O')
        with Measure(number='16', width=181.62):
            with Note(default_x=19.01, default_y=-1336.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.49, relative_y=-30.0):
                    Syllabic('middle')
                    Text('san')
            with Note(default_x=72.32, default_y=-1311.29):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='17', width=165.05):
            with Note(default_x=15.8, default_y=-1316.29):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                    Extend()
            with Note(default_x=65.02, default_y=-1326.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.24, default_y=-1306.29):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ex')
        with Measure(number='18', width=174.21):
            with Note(default_x=15.8, default_y=-1301.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.49, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cel')
            with Note(default_x=88.6, default_y=-1306.29):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=116.61, default_y=-1311.29):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=144.61, default_y=-1316.29):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='19', width=201.46):
            with Note(default_x=15.8, default_y=-1321.29):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=45.55, default_y=-1326.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=80.86, default_y=-1331.29):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=110.61, default_y=-1326.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=140.36, default_y=-1336.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=170.11, default_y=-1331.29):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=207.81):
            with Note(default_x=19.01, default_y=-1326.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.11, default_y=-46.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('sis,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=143.81, default_y=-1326.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('o')
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(83.04)
            with Note(default_x=100.55, default_y=-1344.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=135.65, default_y=-1349.08):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=170.75, default_y=-1354.08):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=205.85, default_y=-1349.08):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=240.95, default_y=-1359.08):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=280.35, default_y=-1354.08):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='22', width=202.52):
            with Note(default_x=15.8, default_y=-1349.08):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-46.49, relative_y=-30.0):
                    Syllabic('middle')
                    Text('san')
            with Note(default_x=77.51, default_y=-1314.08):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=108.36, default_y=-1319.08):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=139.21, default_y=-1324.08):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=170.06, default_y=-1329.08):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='23', width=215.35):
            with Note(default_x=15.8, default_y=-1334.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=48.79, default_y=-1339.08):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=81.78, default_y=-1344.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=114.78, default_y=-1349.08):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=147.77, default_y=-1354.08):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=180.76, default_y=-1359.08):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='24', width=183.31):
            with Note(default_x=19.01, default_y=-1364.08):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.13, default_y=-1324.08):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=98.69, default_y=-1329.08):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=125.25, default_y=-1339.08):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
        with Measure(number='25', width=208.73):
            with Note(default_x=15.83, default_y=-1344.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                    Extend()
            with Note(default_x=86.26, default_y=-1339.08):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=146.69, default_y=-1334.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ex')
        with Measure(number='26', width=180.39):
            with Note(default_x=15.8, default_y=-1329.08):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-46.49, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cel')
            with Note(default_x=62.37, default_y=-1324.08):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.58, default_y=-1319.08):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=149.69, default_y=-1324.08):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='27', width=207.58):
            with Note(default_x=15.8, default_y=-1329.08):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=43.57, default_y=-1334.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=94.91, default_y=-1339.08):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=122.68, default_y=-1334.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=150.44, default_y=-1344.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=178.21, default_y=-1339.08):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=197.53):
            with Note(default_x=19.01, default_y=-1334.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.5, default_y=-1329.08):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=77.99, default_y=-1324.08):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=107.47, default_y=-1319.08):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=136.96, default_y=-1329.08):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=166.45, default_y=-1324.08):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(81.08)
            with Note(default_x=100.55, default_y=-1300.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.11, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('sis,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='30', width=190.32):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=180.55):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=66.69, default_y=-1325.98):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('o')
        with Measure(number='32', width=182.65):
            with Note(default_x=19.01, default_y=-1335.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('san')
            with Note(default_x=67.2, default_y=-1310.98):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='33', width=150.11):
            with Note(default_x=15.83, default_y=-1315.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                    Extend()
            with Note(default_x=59.63, default_y=-1325.98):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=103.44, default_y=-1305.98):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ex')
        with Measure(number='34', width=151.81):
            with Note(default_x=18.65, default_y=-1300.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cel')
        with Measure(number='35', width=169.29):
            with Note(default_x=18.65, default_y=-1310.98):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=118.13, default_y=-1295.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.11, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('sis,')
        with Measure(number='36', width=170.81):
            with Note(default_x=15.8, default_y=-1305.98):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=118.19, default_y=-1305.98):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ex')
        with Measure(number='37', width=149.23):
            with Note(default_x=15.8, default_y=-1310.98):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cel')
            with Note(default_x=102.8, default_y=-1315.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='38', width=92.92):
            with Note(default_x=15.83, default_y=-1310.98):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.77, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('sis.')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P14'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(101.16)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=18.8, relative_x=-15.33, relative_y=2.97):
                        F()
                Sound(dynamics=141.11)
            with Note(default_x=126.66, default_y=-1454.17):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('San')
            with Note(default_x=381.94, default_y=-1489.17):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.83, default_y=-45.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('ctus,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=523.68):
            with Note(default_x=18.76, default_y=-1459.17):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('san')
            with Note(default_x=281.27, default_y=-1494.17):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.83, default_y=-45.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('ctus,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=503.54):
            with Note(default_x=18.56, default_y=-1459.17):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('san')
            with Note(default_x=273.84, default_y=-1494.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('ctus')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(73.16)
            with Note(default_x=104.35, default_y=-1388.28):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.9, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=206.42, default_y=-1393.28):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.9, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mi')
            with Note(default_x=257.46, default_y=-1393.28):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.9, relative_y=-30.0):
                    Syllabic('end')
                    Text('nus')
            with Note(default_x=308.49, default_y=-1398.28):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.9, relative_y=-30.0):
                    Syllabic('begin')
                    Text('De')
            with Note(default_x=410.57, default_y=-1403.28):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.9, relative_y=-30.0):
                    Syllabic('end')
                    Text('us')
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-1398.28):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-50.9, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
            with Note(default_x=56.47, default_y=-1418.28):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=96.91, default_y=-1413.28):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=137.34, default_y=-1413.28):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.9, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ba')
            with Note(default_x=177.42, default_y=-1393.28):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=8.62, default_y=-50.9, relative_y=-30.0):
                    Syllabic('end')
                    Text('oth.')
        with Measure(number='6', width=454.03):
            with Note(default_x=17.8, default_y=-1383.28):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.9, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ple')
            with Note(default_x=76.31, default_y=-1383.28):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.9, relative_y=-30.0):
                    Syllabic('end')
                    Text('ni')
            with Note(default_x=122.28, default_y=-1383.28):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.9, relative_y=-30.0):
                    Syllabic('single')
                    Text('sunt')
            with Note(default_x=168.25, default_y=-1383.28):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-50.9, relative_y=-30.0):
                    Syllabic('begin')
                    Text('cae')
            with Note(default_x=318.7, default_y=-1388.28):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=385.57, default_y=-1393.28):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=435.4):
            with Note(default_x=19.67, default_y=-1398.28):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.84, default_y=-1403.28):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=120.01, default_y=-1398.28):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.9, relative_y=-30.0):
                    Syllabic('end')
                    Text('li')
            with Note(default_x=170.17, default_y=-1408.28):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.9, relative_y=-30.0):
                    Syllabic('single')
                    Text('et')
            with Note(default_x=221.92, default_y=-1403.28):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-50.9, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ter')
            with Note(default_x=273.67, default_y=-1393.28):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=328.65, default_y=-1388.28):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=383.63, default_y=-1393.28):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(80.58)
            with Note(default_x=104.35, default_y=-1428.01):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=232.56, default_y=-1423.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Note(default_x=360.77, default_y=-1413.01):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
            with Note(default_x=488.98, default_y=-1408.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.49, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=553.08, default_y=-1408.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-46.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('a,')
        with Measure(number='9', width=515.8):
            with Note(default_x=21.03, default_y=-1423.01):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
            with Note(default_x=144.32, default_y=-1418.01):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.49, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=205.97, default_y=-1418.01):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-46.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('a,')
            with Note(default_x=267.25, default_y=-1428.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
        with Measure(number='10', width=421.29):
            with Note(default_x=17.8, default_y=-1423.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=117.12, default_y=-1423.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.49, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=166.79, default_y=-1423.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('a')
            with Note(default_x=216.09, default_y=-1423.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tu')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-1443.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.46, default_y=-46.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('a.')
            with Note(default_x=75.83, default_y=-1443.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('O')
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(88.61)
            with Note(default_x=100.55, default_y=-1459.9):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.15, relative_y=-30.0):
                    Syllabic('middle')
                    Text('san')
            with Note(default_x=155.21, default_y=-1439.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='13', width=160.65):
            with Note(default_x=18.2, default_y=-1444.9):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                    Extend()
            with Note(default_x=65.15, default_y=-1454.9):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=112.1, default_y=-1434.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ex')
        with Measure(number='14', width=183.66):
            with Note(default_x=18.2, default_y=-1429.9):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.15, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cel')
            with Note(default_x=82.77, default_y=-1434.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=115.87, default_y=-1439.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=148.96, default_y=-1444.9):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=192.78):
            with Note(default_x=12.94, default_y=-1449.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=42.64, default_y=-1454.9):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=72.35, default_y=-1459.9):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=102.06, default_y=-1454.9):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=131.77, default_y=-1464.9):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=161.47, default_y=-1459.9):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='16', width=181.62):
            with Note(default_x=19.01, default_y=-1454.9):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.11, default_y=-47.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('sis,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=126.35, default_y=-1449.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('o')
        with Measure(number='17', width=165.05):
            with Note(default_x=15.8, default_y=-1469.9):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.15, relative_y=-30.0):
                    Syllabic('middle')
                    Text('san')
            with Note(default_x=65.02, default_y=-1464.9):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.24, default_y=-1459.9):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='18', width=174.21):
            with Note(default_x=15.8, default_y=-1454.9):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('in')
                    Extend()
            with Note(default_x=60.6, default_y=-1449.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=116.61, default_y=-1444.9):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ex')
        with Measure(number='19', width=201.46):
            with Note(default_x=15.44, default_y=-1454.9):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-47.15, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cel')
            with Note(default_x=140.36, default_y=-1449.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='20', width=207.81):
            with Note(default_x=19.01, default_y=-1449.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=50.21, default_y=-1454.9):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=81.41, default_y=-1459.9):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=112.61, default_y=-1454.9):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=143.81, default_y=-1464.9):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=175.01, default_y=-1459.9):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.08)
            with Note(default_x=100.55, default_y=-1458.16):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=240.95, default_y=-1458.16):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='22', width=202.52):
            with Note(default_x=15.8, default_y=-1458.16):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=46.65, default_y=-1463.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=77.51, default_y=-1468.16):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=108.36, default_y=-1463.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=139.21, default_y=-1473.16):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=170.06, default_y=-1468.16):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='23', width=215.35):
            with Note(default_x=15.44, default_y=-1478.16):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=147.77, default_y=-1473.16):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=183.31):
            with Note(default_x=18.65, default_y=-1468.16):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=125.25, default_y=-1453.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='25', width=208.73):
            with Note(default_x=15.83, default_y=-1473.16):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.11, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('sis,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='26', width=180.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=207.58):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=94.55, default_y=-1453.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('o')
        with Measure(number='28', width=197.53):
            with Note(default_x=19.01, default_y=-1463.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('san')
            with Note(default_x=77.62, default_y=-1438.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.7)
            with Note(default_x=100.55, default_y=-1442.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                    Extend()
            with Note(default_x=153.53, default_y=-1452.68):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=206.17, default_y=-1432.68):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ex')
        with Measure(number='30', width=190.32):
            with Note(default_x=18.2, default_y=-1427.68):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.49, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cel')
            with Note(default_x=103.46, default_y=-1432.68):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=131.88, default_y=-1437.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=160.3, default_y=-1442.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=180.55):
            with Note(default_x=15.8, default_y=-1447.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=41.42, default_y=-1452.68):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=67.05, default_y=-1457.68):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=92.67, default_y=-1452.68):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=118.29, default_y=-1462.68):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=143.92, default_y=-1457.68):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='32', width=182.65):
            with Note(default_x=19.01, default_y=-1452.68):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=43.29, default_y=-1447.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=67.56, default_y=-1442.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=91.84, default_y=-1447.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=116.12, default_y=-1442.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=146.02, default_y=-1437.68):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='33', width=150.11):
            with Note(default_x=15.83, default_y=-1432.68):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.11, default_y=-46.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('sis,')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=103.44, default_y=-1432.68):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('o')
        with Measure(number='34', width=151.81):
            with Note(default_x=18.65, default_y=-1417.68):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.49, relative_y=-30.0):
                    Syllabic('middle')
                    Text('san')
        with Measure(number='35', width=169.29):
            with Note(default_x=18.65, default_y=-1437.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='36', width=170.81):
            with Note(default_x=15.8, default_y=-1432.68):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=118.19, default_y=-1432.68):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ex')
        with Measure(number='37', width=149.23):
            with Note(default_x=16.16, default_y=-1427.68):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.49, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cel')
            with Note(default_x=59.48, default_y=-1437.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=102.8, default_y=-1432.68):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='38', width=92.92):
            with Note(default_x=15.83, default_y=-1452.68):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.77, default_y=-46.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('sis.')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P15'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=127.02, default_y=-1594.17):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=163.3, default_y=-1574.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=254.48, default_y=-1584.17):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=290.77, default_y=-1574.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=381.94, default_y=-1594.17):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=438.96, default_y=-1584.17):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=495.99, default_y=-1574.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=553.01, default_y=-1559.17):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=523.68):
            with Note(default_x=19.12, default_y=-1599.17):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=57.43, default_y=-1574.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=150.19, default_y=-1589.17):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=188.51, default_y=-1574.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=281.27, default_y=-1599.17):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=341.47, default_y=-1589.17):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=401.67, default_y=-1574.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=461.88, default_y=-1564.17):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='3', width=503.54):
            with Note(default_x=18.92, default_y=-1599.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.21, default_y=-1574.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=146.38, default_y=-1584.17):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=182.67, default_y=-1574.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=273.84, default_y=-1599.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=330.87, default_y=-1584.17):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=387.89, default_y=-1574.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=444.91, default_y=-1564.17):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(91.02)
            with Note(default_x=104.35, default_y=-1554.3):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=155.39, default_y=-1519.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=206.42, default_y=-1524.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=257.46, default_y=-1559.3):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=308.49, default_y=-1564.3):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=359.53, default_y=-1529.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=410.57, default_y=-1534.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=461.6, default_y=-1569.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-1539.3):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.47, default_y=-1549.3):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=96.91, default_y=-1544.3):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=137.34, default_y=-1509.3):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=177.78, default_y=-1559.3):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=210.14, default_y=-1549.3):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=242.49, default_y=-1539.3):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=274.84, default_y=-1524.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='6', width=454.03):
            with Note(default_x=17.8, default_y=-1514.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=76.31, default_y=-1514.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=122.28, default_y=-1514.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=168.25, default_y=-1514.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=251.83, default_y=-1514.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=318.7, default_y=-1519.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=385.57, default_y=-1524.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=435.4):
            with Note(default_x=19.67, default_y=-1529.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.84, default_y=-1534.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=120.01, default_y=-1529.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=170.17, default_y=-1539.3):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=221.92, default_y=-1534.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=273.67, default_y=-1524.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=328.65, default_y=-1519.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=383.63, default_y=-1524.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(91.13)
            with Note(default_x=104.35, default_y=-1559.14):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=168.45, default_y=-1569.14):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=232.56, default_y=-1554.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=296.66, default_y=-1589.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=360.77, default_y=-1579.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=424.87, default_y=-1554.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=488.98, default_y=-1574.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=553.08, default_y=-1539.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='9', width=515.8):
            with Note(default_x=21.03, default_y=-1554.14):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=82.68, default_y=-1589.14):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=144.32, default_y=-1584.14):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=205.97, default_y=-1549.14):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=267.62, default_y=-1559.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=329.26, default_y=-1594.14):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=390.91, default_y=-1559.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=452.55, default_y=-1559.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='10', width=421.29):
            with Note(default_x=17.8, default_y=-1554.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.46, default_y=-1589.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=117.12, default_y=-1554.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=166.79, default_y=-1554.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=216.45, default_y=-1554.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=266.11, default_y=-1589.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=315.77, default_y=-1554.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=365.43, default_y=-1554.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-1574.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(97.24)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=160.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=183.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=192.78):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=71.99, default_y=-1572.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='16', width=181.62):
            with Note(default_x=19.01, default_y=-1582.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.32, default_y=-1557.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='17', width=165.05):
            with Note(default_x=15.8, default_y=-1562.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=65.02, default_y=-1572.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=114.24, default_y=-1552.14):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='18', width=174.21):
            with Note(default_x=15.8, default_y=-1547.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=88.6, default_y=-1552.14):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=116.61, default_y=-1557.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=144.61, default_y=-1562.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='19', width=201.46):
            with Note(default_x=15.8, default_y=-1567.14):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=45.55, default_y=-1572.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=80.86, default_y=-1577.14):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=110.61, default_y=-1572.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=140.36, default_y=-1582.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=170.11, default_y=-1577.14):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=207.81):
            with Note(default_x=19.01, default_y=-1572.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=143.81, default_y=-1572.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.55, default_y=-1543.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=240.95, default_y=-1563.16):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='22', width=202.52):
            with Note(default_x=15.8, default_y=-1563.16):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=46.65, default_y=-1568.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=77.51, default_y=-1573.16):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=108.36, default_y=-1568.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=139.21, default_y=-1578.16):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=170.06, default_y=-1573.16):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='23', width=215.35):
            with Note(default_x=15.44, default_y=-1583.16):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=147.77, default_y=-1578.16):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=183.31):
            with Note(default_x=18.65, default_y=-1573.16):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=125.25, default_y=-1558.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='25', width=208.73):
            with Note(default_x=15.83, default_y=-1578.16):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Attributes():
                with Clef():
                    Sign('C')
                    Line(4)
            with Note(default_x=86.26, default_y=-1558.16):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=146.69, default_y=-1553.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='26', width=180.39):
            with Note(default_x=15.8, default_y=-1548.16):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=62.37, default_y=-1543.16):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.58, default_y=-1538.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=149.69, default_y=-1543.16):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='27', width=207.58):
            with Note(default_x=15.8, default_y=-1548.16):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=43.57, default_y=-1553.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Attributes():
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=94.55, default_y=-1558.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='28', width=197.53):
            with Note(default_x=19.01, default_y=-1568.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=77.62, default_y=-1543.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(88.35)
            with Note(default_x=100.55, default_y=-1571.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=153.53, default_y=-1581.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=206.17, default_y=-1561.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='30', width=190.32):
            with Note(default_x=18.2, default_y=-1556.03):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=103.46, default_y=-1561.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=131.88, default_y=-1566.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=160.3, default_y=-1571.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=180.55):
            with Note(default_x=15.8, default_y=-1576.03):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=41.42, default_y=-1581.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=67.05, default_y=-1586.03):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=92.67, default_y=-1581.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=118.29, default_y=-1591.03):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=143.92, default_y=-1586.03):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='32', width=182.65):
            with Note(default_x=19.01, default_y=-1581.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=43.29, default_y=-1576.03):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=67.56, default_y=-1571.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=91.84, default_y=-1576.03):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=116.12, default_y=-1571.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=146.02, default_y=-1566.03):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='33', width=150.11):
            with Note(default_x=15.83, default_y=-1561.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=59.63, default_y=-1596.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.44, default_y=-1561.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='34', width=151.81):
            with Note(default_x=19.01, default_y=-1581.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=105.43, default_y=-1581.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='35', width=169.29):
            with Note(default_x=19.01, default_y=-1566.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=118.13, default_y=-1566.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=170.81):
            with Note(default_x=16.16, default_y=-1561.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=118.19, default_y=-1561.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='37', width=149.23):
            with Note(default_x=16.16, default_y=-1556.03):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=59.48, default_y=-1566.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=102.8, default_y=-1561.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='38', width=92.92):
            with Note(default_x=15.83, default_y=-1581.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P16'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
                    ClefOctaveChange(-1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=127.02, default_y=-1699.17):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=163.3, default_y=-1679.17):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=254.48, default_y=-1689.17):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=290.77, default_y=-1679.17):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=381.94, default_y=-1699.17):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=438.96, default_y=-1689.17):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=495.99, default_y=-1679.17):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=553.01, default_y=-1664.17):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=523.68):
            with Note(default_x=19.12, default_y=-1704.17):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=57.43, default_y=-1679.17):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=150.19, default_y=-1694.17):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=188.51, default_y=-1679.17):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=281.27, default_y=-1704.17):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=341.47, default_y=-1694.17):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=401.67, default_y=-1679.17):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=461.88, default_y=-1669.17):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='3', width=503.54):
            with Note(default_x=18.92, default_y=-1704.17):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.21, default_y=-1679.17):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=146.38, default_y=-1689.17):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=182.67, default_y=-1679.17):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=273.84, default_y=-1704.17):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=330.87, default_y=-1689.17):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=387.89, default_y=-1679.17):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=444.91, default_y=-1669.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-1659.3):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=155.39, default_y=-1624.3):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=206.42, default_y=-1629.3):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=257.46, default_y=-1664.3):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=308.49, default_y=-1669.3):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=359.53, default_y=-1634.3):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=410.57, default_y=-1639.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=461.6, default_y=-1674.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-1644.3):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.47, default_y=-1654.3):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=96.91, default_y=-1649.3):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=137.34, default_y=-1614.3):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=177.78, default_y=-1664.3):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=210.14, default_y=-1654.3):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=242.49, default_y=-1644.3):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=274.84, default_y=-1629.3):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='6', width=454.03):
            with Note(default_x=17.8, default_y=-1619.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=76.31, default_y=-1619.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=122.28, default_y=-1619.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=168.25, default_y=-1619.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=251.83, default_y=-1619.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=318.7, default_y=-1624.3):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=385.57, default_y=-1629.3):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=435.4):
            with Note(default_x=19.67, default_y=-1634.3):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.84, default_y=-1639.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=120.01, default_y=-1634.3):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=170.17, default_y=-1644.3):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=221.92, default_y=-1639.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=273.67, default_y=-1629.3):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=328.65, default_y=-1624.3):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=383.63, default_y=-1629.3):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-1664.14):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=168.45, default_y=-1674.14):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=232.56, default_y=-1659.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=296.66, default_y=-1694.14):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=360.77, default_y=-1684.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=424.87, default_y=-1659.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=488.98, default_y=-1679.14):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=553.08, default_y=-1644.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='9', width=515.8):
            with Note(default_x=21.03, default_y=-1659.14):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=82.68, default_y=-1694.14):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=144.32, default_y=-1689.14):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=205.97, default_y=-1654.14):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=267.62, default_y=-1664.14):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=329.26, default_y=-1699.14):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=390.91, default_y=-1664.14):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=452.55, default_y=-1664.14):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='10', width=421.29):
            with Note(default_x=17.8, default_y=-1659.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.46, default_y=-1694.14):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=117.12, default_y=-1659.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=166.79, default_y=-1659.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=216.45, default_y=-1659.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=266.11, default_y=-1694.14):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=315.77, default_y=-1659.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=365.43, default_y=-1659.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-1679.14):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.83, default_y=-1679.14):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.55, default_y=-1702.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=155.21, default_y=-1682.14):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='13', width=160.65):
            with Note(default_x=18.2, default_y=-1687.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=65.15, default_y=-1697.14):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=112.1, default_y=-1677.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='14', width=183.66):
            with Note(default_x=18.2, default_y=-1672.14):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=82.77, default_y=-1677.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=115.87, default_y=-1682.14):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=148.96, default_y=-1687.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=192.78):
            with Note(default_x=12.94, default_y=-1692.14):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=42.64, default_y=-1697.14):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=72.35, default_y=-1702.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=102.06, default_y=-1697.14):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=131.77, default_y=-1707.14):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=161.47, default_y=-1702.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='16', width=181.62):
            with Note(default_x=19.01, default_y=-1697.14):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.68, default_y=-1707.14):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=126.35, default_y=-1692.14):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='17', width=165.05):
            with Note(default_x=15.8, default_y=-1712.14):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=65.02, default_y=-1707.14):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=114.24, default_y=-1702.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='18', width=174.21):
            with Note(default_x=15.8, default_y=-1697.14):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=60.6, default_y=-1692.14):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=116.61, default_y=-1687.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='19', width=201.46):
            with Note(default_x=15.44, default_y=-1697.14):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=140.36, default_y=-1692.14):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='20', width=207.81):
            with Note(default_x=19.01, default_y=-1692.14):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=50.21, default_y=-1697.14):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=81.41, default_y=-1702.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=112.61, default_y=-1697.14):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=143.81, default_y=-1707.14):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=175.01, default_y=-1702.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.55, default_y=-1668.16):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=240.95, default_y=-1668.16):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='22', width=202.52):
            with Note(default_x=15.8, default_y=-1668.16):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=46.65, default_y=-1673.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=77.51, default_y=-1678.16):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=108.36, default_y=-1673.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=139.21, default_y=-1683.16):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=170.06, default_y=-1678.16):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='23', width=215.35):
            with Note(default_x=15.44, default_y=-1688.16):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=147.77, default_y=-1683.16):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=183.31):
            with Note(default_x=18.65, default_y=-1678.16):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=125.25, default_y=-1663.16):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='25', width=208.73):
            with Note(default_x=15.83, default_y=-1683.16):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='26', width=180.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=207.58):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=94.55, default_y=-1663.16):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='28', width=197.53):
            with Note(default_x=19.01, default_y=-1673.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=77.62, default_y=-1648.16):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.55, default_y=-1676.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=153.53, default_y=-1686.03):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=206.17, default_y=-1666.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='30', width=190.32):
            with Note(default_x=18.2, default_y=-1661.03):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=103.46, default_y=-1666.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=131.88, default_y=-1671.03):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=160.3, default_y=-1676.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=180.55):
            with Note(default_x=15.8, default_y=-1681.03):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=41.42, default_y=-1686.03):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=67.05, default_y=-1691.03):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=92.67, default_y=-1686.03):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=118.29, default_y=-1696.03):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=143.92, default_y=-1691.03):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='32', width=182.65):
            with Note(default_x=19.01, default_y=-1686.03):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=43.29, default_y=-1681.03):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=67.56, default_y=-1676.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=91.84, default_y=-1681.03):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=116.12, default_y=-1676.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=146.02, default_y=-1671.03):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='33', width=150.11):
            with Note(default_x=15.83, default_y=-1666.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=59.63, default_y=-1701.03):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.44, default_y=-1666.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='34', width=151.81):
            with Note(default_x=19.01, default_y=-1686.03):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=105.43, default_y=-1686.03):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='35', width=169.29):
            with Note(default_x=19.01, default_y=-1671.03):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=118.13, default_y=-1671.03):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=170.81):
            with Note(default_x=16.16, default_y=-1666.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=118.19, default_y=-1666.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='37', width=149.23):
            with Note(default_x=16.16, default_y=-1661.03):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=59.48, default_y=-1671.03):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=102.8, default_y=-1666.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='38', width=92.92):
            with Note(default_x=15.83, default_y=-1686.03):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P17'):
        with Measure(number='1', width=611.63):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(2)
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
            with Note(default_x=123.7, default_y=-1829.17):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(64.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=123.7, default_y=-1819.17):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(64.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=123.7, default_y=-1809.17):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(64.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(64.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=127.02, default_y=-1909.17):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=163.3, default_y=-1889.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=254.48, default_y=-1899.17):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=290.77, default_y=-1889.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=381.94, default_y=-1909.17):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=438.96, default_y=-1899.17):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=495.99, default_y=-1889.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=553.01, default_y=-1874.17):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='2', width=523.68):
            with Note(default_x=15.8, default_y=-1834.17):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(64.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=15.8, default_y=-1814.17):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(64.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=34.31, default_y=-1809.17):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(64.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(64.0)
            with Note(default_x=19.12, default_y=-1914.17):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=57.43, default_y=-1889.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=150.19, default_y=-1904.17):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=188.51, default_y=-1889.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=281.27, default_y=-1914.17):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=341.47, default_y=-1904.17):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=401.67, default_y=-1889.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=461.88, default_y=-1879.17):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='3', width=503.54):
            with Note(default_x=15.6, default_y=-1834.17):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(64.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                Staff(1)
            with Note(default_x=34.11, default_y=-1829.17):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(64.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=15.6, default_y=-1819.17):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(64.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(64.0)
            with Note(default_x=18.92, default_y=-1914.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=55.21, default_y=-1889.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=146.38, default_y=-1899.17):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=182.67, default_y=-1889.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=273.84, default_y=-1914.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=330.87, default_y=-1899.17):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=387.89, default_y=-1889.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=444.91, default_y=-1879.17):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='4', width=514.24):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-1789.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=104.35, default_y=-1779.3):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=104.35, default_y=-1764.3):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=206.42, default_y=-1794.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=206.42, default_y=-1784.3):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=206.42, default_y=-1769.3):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=308.49, default_y=-1799.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=308.49, default_y=-1789.3):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=308.49, default_y=-1774.3):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=410.57, default_y=-1804.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=410.57, default_y=-1794.3):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=410.57, default_y=-1779.3):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(64.0)
            with Note(default_x=104.35, default_y=-1869.3):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=155.39, default_y=-1834.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=206.42, default_y=-1839.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=257.46, default_y=-1874.3):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=308.49, default_y=-1879.3):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=359.53, default_y=-1844.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=410.57, default_y=-1849.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=461.6, default_y=-1884.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='5', width=308.79):
            with Note(default_x=16.03, default_y=-1784.3):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=16.03, default_y=-1774.3):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=16.03, default_y=-1764.3):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=56.47, default_y=-1784.3):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=56.47, default_y=-1764.3):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=68.33, default_y=-1759.3):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=96.91, default_y=-1779.3):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=108.77, default_y=-1774.3):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=96.91, default_y=-1764.3):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=137.34, default_y=-1779.3):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=137.34, default_y=-1769.3):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=137.34, default_y=-1744.3):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=177.42, default_y=-1794.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=177.42, default_y=-1784.3):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=177.42, default_y=-1774.3):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(64.0)
            with Note(default_x=16.03, default_y=-1854.3):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=56.47, default_y=-1864.3):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.91, default_y=-1859.3):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=137.34, default_y=-1824.3):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=177.78, default_y=-1874.3):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=210.14, default_y=-1864.3):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=242.49, default_y=-1854.3):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=274.84, default_y=-1839.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='6', width=454.03):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note(default_x=168.25, default_y=-1784.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=180.12, default_y=-1779.3):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=168.25, default_y=-1769.3):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=168.25, default_y=-1759.3):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=318.7, default_y=-1789.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=318.7, default_y=-1779.3):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=318.7, default_y=-1769.3):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=385.57, default_y=-1794.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=385.57, default_y=-1784.3):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=397.43, default_y=-1779.3):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=385.57, default_y=-1769.3):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(64.0)
            with Note(default_x=17.8, default_y=-1829.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=76.31, default_y=-1829.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=122.28, default_y=-1829.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=168.25, default_y=-1829.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=251.83, default_y=-1829.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=318.7, default_y=-1834.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=385.57, default_y=-1839.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='7', width=435.4):
            with Note(default_x=19.31, default_y=-1789.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=19.31, default_y=-1774.3):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=221.92, default_y=-1794.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=221.92, default_y=-1784.3):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=221.92, default_y=-1774.3):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=328.65, default_y=-1779.3):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=328.65, default_y=-1769.3):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(64.0)
            with Note(default_x=19.67, default_y=-1844.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=69.84, default_y=-1849.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=120.01, default_y=-1844.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=170.17, default_y=-1854.3):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=221.92, default_y=-1849.3):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=273.67, default_y=-1839.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=328.65, default_y=-1834.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=383.63, default_y=-1839.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='8', width=618.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=104.35, default_y=-1829.14):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=104.35, default_y=-1809.14):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=116.22, default_y=-1804.14):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=232.56, default_y=-1824.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=232.56, default_y=-1814.14):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=232.56, default_y=-1804.14):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=360.77, default_y=-1814.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=360.77, default_y=-1794.14):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=372.63, default_y=-1789.14):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=488.98, default_y=-1809.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=488.98, default_y=-1799.14):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=488.98, default_y=-1789.14):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(64.0)
            with Note(default_x=104.35, default_y=-1874.14):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=168.45, default_y=-1884.14):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=232.56, default_y=-1869.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=296.66, default_y=-1904.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=360.77, default_y=-1894.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=424.87, default_y=-1869.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=488.98, default_y=-1889.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=553.08, default_y=-1854.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='9', width=515.8):
            with Note(default_x=21.03, default_y=-1824.14):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=21.03, default_y=-1814.14):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=21.03, default_y=-1804.14):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=21.03, default_y=-1794.14):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=144.32, default_y=-1819.14):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=144.32, default_y=-1809.14):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=144.32, default_y=-1799.14):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=267.62, default_y=-1829.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=267.62, default_y=-1819.14):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=267.62, default_y=-1809.14):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=267.62, default_y=-1799.14):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=390.91, default_y=-1829.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=390.91, default_y=-1819.14):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=390.91, default_y=-1804.14):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=452.55, default_y=-1829.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=452.55, default_y=-1819.14):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=452.55, default_y=-1809.14):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(64.0)
            with Note(default_x=21.03, default_y=-1869.14):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=82.68, default_y=-1904.14):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=144.32, default_y=-1899.14):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=205.97, default_y=-1864.14):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=267.62, default_y=-1874.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=329.26, default_y=-1909.14):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=390.91, default_y=-1874.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=452.55, default_y=-1874.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='10', width=421.29):
            with Note(default_x=17.8, default_y=-1824.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=17.8, default_y=-1814.14):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=17.8, default_y=-1804.14):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=17.8, default_y=-1794.14):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=117.12, default_y=-1824.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=117.12, default_y=-1809.14):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=117.12, default_y=-1799.14):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=216.45, default_y=-1824.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=216.45, default_y=-1809.14):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=228.31, default_y=-1804.14):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=315.77, default_y=-1824.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=315.77, default_y=-1814.14):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=315.77, default_y=-1804.14):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(64.0)
            with Note(default_x=17.8, default_y=-1869.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=67.46, default_y=-1904.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=117.12, default_y=-1869.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=166.79, default_y=-1869.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=216.45, default_y=-1869.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=266.11, default_y=-1904.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=315.77, default_y=-1869.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=365.43, default_y=-1869.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=156.58):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=36.8, default_y=-1809.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=36.8, default_y=-1799.14):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=36.8, default_y=-1789.14):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=36.8, default_y=-1889.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=75.83, default_y=-1889.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(32.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='12', width=245.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=100.55, default_y=-1912.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=155.21, default_y=-1892.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='13', width=160.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=18.2, default_y=-1897.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=65.15, default_y=-1907.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=112.1, default_y=-1887.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='14', width=183.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=18.2, default_y=-1882.14):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=82.77, default_y=-1887.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=115.87, default_y=-1892.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=148.96, default_y=-1897.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='15', width=192.78):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=71.99, default_y=-1842.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=12.94, default_y=-1902.14):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=42.64, default_y=-1907.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=72.35, default_y=-1912.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=102.06, default_y=-1907.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=131.77, default_y=-1917.14):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=161.47, default_y=-1912.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='16', width=181.62):
            with Note(default_x=19.01, default_y=-1852.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=72.32, default_y=-1827.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=19.01, default_y=-1907.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=72.68, default_y=-1917.14):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=126.35, default_y=-1902.14):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=165.05):
            with Note(default_x=15.8, default_y=-1832.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=65.02, default_y=-1842.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=114.24, default_y=-1822.14):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-1922.14):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=65.02, default_y=-1917.14):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=114.24, default_y=-1912.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='18', width=174.21):
            with Note(default_x=15.8, default_y=-1817.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=88.6, default_y=-1822.14):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=116.61, default_y=-1827.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=144.61, default_y=-1832.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-1907.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=60.6, default_y=-1902.14):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=116.61, default_y=-1897.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='19', width=201.46):
            with Note(default_x=15.8, default_y=-1837.14):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=45.55, default_y=-1842.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=80.86, default_y=-1847.14):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=110.61, default_y=-1842.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=140.36, default_y=-1852.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=170.11, default_y=-1847.14):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.44, default_y=-1907.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(32.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=140.36, default_y=-1902.14):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='20', width=207.81):
            with Note(default_x=19.01, default_y=-1842.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=81.05, default_y=-1812.14):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Forward():
                Duration(32.0)
            with Note(default_x=143.81, default_y=-1842.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=19.01, default_y=-1902.14):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=50.21, default_y=-1907.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=81.41, default_y=-1912.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=112.61, default_y=-1907.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=143.81, default_y=-1917.14):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=175.01, default_y=-1912.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='21', width=317.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=100.55, default_y=-1813.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=100.55, default_y=-1788.16):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=240.95, default_y=-1798.16):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=240.95, default_y=-1778.16):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=100.55, default_y=-1878.16):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=240.95, default_y=-1878.16):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='22', width=202.52):
            with Note(default_x=15.8, default_y=-1783.16):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-1773.16):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=108.36, default_y=-1803.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=108.36, default_y=-1788.16):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=108.36, default_y=-1778.16):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=139.21, default_y=-1813.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=139.21, default_y=-1803.16):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=139.21, default_y=-1793.16):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=139.21, default_y=-1783.16):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=170.06, default_y=-1808.16):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=170.06, default_y=-1798.16):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=170.06, default_y=-1788.16):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-1878.16):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=46.65, default_y=-1883.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=77.51, default_y=-1888.16):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=108.36, default_y=-1883.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=139.21, default_y=-1893.16):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=170.06, default_y=-1888.16):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='23', width=215.35):
            with Note(default_x=15.8, default_y=-1818.16):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-1808.16):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-1793.16):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=81.78, default_y=-1818.16):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=93.65, default_y=-1813.16):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=81.78, default_y=-1803.16):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=147.77, default_y=-1813.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=147.77, default_y=-1803.16):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=147.77, default_y=-1793.16):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.44, default_y=-1898.16):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=147.77, default_y=-1893.16):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='24', width=183.31):
            with Note(default_x=18.65, default_y=-1808.16):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=18.65, default_y=-1798.16):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=18.65, default_y=-1788.16):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=125.25, default_y=-1808.16):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=125.25, default_y=-1798.16):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=137.12, default_y=-1793.16):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=125.25, default_y=-1783.16):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=18.65, default_y=-1888.16):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=125.25, default_y=-1873.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='25', width=208.73):
            with Note(default_x=15.83, default_y=-1813.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.83, default_y=-1803.16):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.83, default_y=-1793.16):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=86.26, default_y=-1798.16):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=86.26, default_y=-1788.16):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=86.26, default_y=-1778.16):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=146.69, default_y=-1793.16):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=146.69, default_y=-1778.16):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.83, default_y=-1893.16):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=86.26, default_y=-1853.16):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=146.69, default_y=-1848.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=180.39):
            with Note(default_x=15.8, default_y=-1798.16):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-1788.16):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=62.37, default_y=-1798.16):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=62.37, default_y=-1783.16):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=91.48, default_y=-1793.16):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=120.58, default_y=-1798.16):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=120.58, default_y=-1788.16):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=120.58, default_y=-1778.16):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=149.69, default_y=-1803.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=149.69, default_y=-1793.16):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=149.69, default_y=-1783.16):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-1843.16):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=62.37, default_y=-1838.16):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=120.58, default_y=-1833.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=149.69, default_y=-1838.16):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='27', width=207.58):
            with Note(default_x=15.8, default_y=-1808.16):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-1798.16):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-1788.16):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=43.57, default_y=-1813.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=43.57, default_y=-1803.16):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=43.57, default_y=-1793.16):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=94.55, default_y=-1808.16):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=94.55, default_y=-1798.16):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=107.14, default_y=-1793.16):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=94.55, default_y=-1783.16):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-1843.16):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=43.57, default_y=-1848.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=94.55, default_y=-1873.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='28', width=197.53):
            with Note(default_x=19.01, default_y=-1803.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=19.01, default_y=-1793.16):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=19.01, default_y=-1778.16):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=77.62, default_y=-1813.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=77.62, default_y=-1803.16):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=77.62, default_y=-1793.16):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=19.01, default_y=-1883.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=77.62, default_y=-1858.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='29', width=274.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=100.55, default_y=-1816.03):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=100.55, default_y=-1806.03):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=100.55, default_y=-1796.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=153.53, default_y=-1831.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=153.53, default_y=-1816.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=153.53, default_y=-1806.03):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=206.17, default_y=-1831.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=206.17, default_y=-1816.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=218.03, default_y=-1811.03):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=246.86, default_y=-1831.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=246.86, default_y=-1816.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=246.86, default_y=-1806.03):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=100.55, default_y=-1886.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=153.53, default_y=-1896.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=206.17, default_y=-1876.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='30', width=190.32):
            with Note(default_x=18.2, default_y=-1826.03):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=18.2, default_y=-1816.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=18.2, default_y=-1801.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=103.46, default_y=-1821.03):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=103.46, default_y=-1806.03):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=103.46, default_y=-1796.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=131.88, default_y=-1831.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=131.88, default_y=-1811.03):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=131.88, default_y=-1801.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=160.3, default_y=-1826.03):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=160.3, default_y=-1816.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=160.3, default_y=-1806.03):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=18.2, default_y=-1871.03):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=103.46, default_y=-1876.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=131.88, default_y=-1881.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=160.3, default_y=-1886.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='31', width=180.55):
            with Note(default_x=15.8, default_y=-1821.03):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-1811.03):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-1801.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=41.42, default_y=-1826.03):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=41.42, default_y=-1816.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=41.42, default_y=-1801.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=67.05, default_y=-1811.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=67.05, default_y=-1796.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=118.29, default_y=-1826.03):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=118.29, default_y=-1816.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=118.29, default_y=-1806.03):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=118.29, default_y=-1796.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=143.92, default_y=-1821.03):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=143.92, default_y=-1801.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=155.78, default_y=-1796.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-1891.03):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=41.42, default_y=-1896.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=67.05, default_y=-1901.03):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.67, default_y=-1896.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=118.29, default_y=-1906.03):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=143.92, default_y=-1901.03):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='32', width=182.65):
            with Note(default_x=19.01, default_y=-1806.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=19.01, default_y=-1796.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=67.56, default_y=-1816.03):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=67.56, default_y=-1796.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=116.12, default_y=-1826.03):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=116.12, default_y=-1816.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=116.12, default_y=-1806.03):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=146.02, default_y=-1816.03):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=157.88, default_y=-1811.03):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=146.02, default_y=-1801.03):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=19.01, default_y=-1896.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=43.29, default_y=-1891.03):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=67.56, default_y=-1886.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.84, default_y=-1891.03):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=116.12, default_y=-1886.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=146.02, default_y=-1881.03):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='33', width=150.11):
            with Note(default_x=15.83, default_y=-1831.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.83, default_y=-1821.03):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.83, default_y=-1811.03):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=59.63, default_y=-1831.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=71.5, default_y=-1826.03):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=59.63, default_y=-1811.03):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=103.44, default_y=-1831.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=103.44, default_y=-1821.03):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=103.44, default_y=-1811.03):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.83, default_y=-1876.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=59.63, default_y=-1911.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=103.44, default_y=-1876.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='34', width=151.81):
            with Note(default_x=18.65, default_y=-1816.03):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=18.65, default_y=-1806.03):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=18.65, default_y=-1796.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=19.01, default_y=-1896.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=105.43, default_y=-1896.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='35', width=169.29):
            with Note(default_x=18.65, default_y=-1836.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=18.65, default_y=-1826.03):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=18.65, default_y=-1816.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=18.65, default_y=-1801.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=118.13, default_y=-1836.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=118.13, default_y=-1826.03):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=118.13, default_y=-1811.03):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=118.13, default_y=-1801.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=19.01, default_y=-1881.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=118.13, default_y=-1881.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='36', width=170.81):
            with Note(default_x=15.8, default_y=-1831.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-1821.03):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-1811.03):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-1796.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=118.19, default_y=-1831.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=118.19, default_y=-1821.03):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=118.19, default_y=-1811.03):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=118.19, default_y=-1801.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=16.16, default_y=-1876.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=118.19, default_y=-1876.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='37', width=149.23):
            with Note(default_x=16.16, default_y=-1826.03):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=16.16, default_y=-1816.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=16.16, default_y=-1806.03):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=59.48, default_y=-1836.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=59.48, default_y=-1826.03):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=59.48, default_y=-1816.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=71.35, default_y=-1811.03):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=102.8, default_y=-1831.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=102.8, default_y=-1821.03):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=102.8, default_y=-1811.03):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=102.8, default_y=-1796.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=16.16, default_y=-1871.03):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=59.48, default_y=-1881.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=102.8, default_y=-1876.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='38', width=92.92):
            with Note(default_x=15.83, default_y=-1831.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.83, default_y=-1816.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.83, default_y=-1806.03):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.83, default_y=-1896.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Fermata(None, type='inverted', default_y=-40.0, relative_y=-10.0)